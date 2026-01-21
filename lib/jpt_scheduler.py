#!/usr/bin/env python3
"""
JPT Unified Scheduler

Single scheduler that manages all background tasks:
- Polling tasks (run at intervals)
- Scheduled tasks (run at specific times)

Usage:
    python3 jpt_scheduler.py status   # Show task states and last runs
    python3 jpt_scheduler.py run      # Single dispatch cycle
    python3 jpt_scheduler.py daemon   # Continuous mode (for launchd)
    python3 jpt_scheduler.py trigger <task>  # Force run a specific task
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional

# Paths
JPT_ROOT = Path.home() / "jpt"
LOG_FILE = JPT_ROOT / "lib" / ".scheduler.log"
STATE_FILE = JPT_ROOT / "lib" / ".scheduler_state.json"

# Environment for subprocesses
ENV = os.environ.copy()
ENV["PATH"] = "/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/jesse/Library/pnpm:/Users/jesse/.local/bin"
ENV["HOME"] = str(Path.home())

# Task definitions
TASKS = {
    # Polling tasks (run on interval)
    "inbox-fetcher": {
        "type": "interval",
        "interval_seconds": 60,
        "command": ["/usr/bin/python3", str(JPT_ROOT / "inbox" / "auto_fetch.py")],
        "log": str(JPT_ROOT / "inbox" / ".fetcher.log"),
    },
    "inbox-processor": {
        "type": "interval",
        "interval_seconds": 120,
        "command": ["/usr/bin/python3", str(JPT_ROOT / "inbox" / "inbox_processor.py")],
        "log": str(JPT_ROOT / "inbox" / ".processor.log"),
    },
    "meeting-processor": {
        "type": "interval",
        "interval_seconds": 120,
        "command": ["/usr/bin/python3", str(JPT_ROOT / "meetings" / "process_meeting.py")],
        "log": str(JPT_ROOT / "meetings" / ".processor.log"),
    },
    "notion-agent": {
        "type": "interval",
        "interval_seconds": 60,
        "command": ["/usr/bin/python3", str(JPT_ROOT / "lib" / "notion_agent.py"), "once"],
        "log": str(JPT_ROOT / "lib" / ".agent.log"),
    },

    # Scheduled tasks (run at specific times)
    "digest-daily": {
        "type": "schedule",
        "schedule": {"hour": 18, "minute": 0},  # 6 PM
        "command": ["/usr/bin/python3", str(JPT_ROOT / "lib" / "digest_processor.py"), "daily"],
        "log": str(JPT_ROOT / "lib" / ".digest.log"),
    },
    "digest-weekly": {
        "type": "schedule",
        "schedule": {"weekday": 6, "hour": 10, "minute": 0},  # Sunday 10 AM
        "command": ["/usr/bin/python3", str(JPT_ROOT / "lib" / "digest_processor.py"), "weekly"],
        "log": str(JPT_ROOT / "lib" / ".digest.log"),
    },
    "digest-monthly": {
        "type": "schedule",
        "schedule": {"day": 1, "hour": 9, "minute": 0},  # 1st of month 9 AM
        "command": ["/usr/bin/python3", str(JPT_ROOT / "lib" / "digest_processor.py"), "monthly"],
        "log": str(JPT_ROOT / "lib" / ".digest.log"),
    },
    "knowledge-curator": {
        "type": "schedule",
        "schedule": {"hour": 2, "minute": 0},  # 2 AM daily
        "command": ["/usr/bin/python3", str(JPT_ROOT / "lib" / "knowledge_curator.py"), "run"],
        "log": str(JPT_ROOT / "lib" / ".curator.log"),
    },
    "knowledge-reviewer": {
        "type": "schedule",
        "schedule": {"weekday": 6, "hour": 3, "minute": 0},  # Sunday 3 AM
        "command": ["/usr/bin/python3", str(JPT_ROOT / "lib" / "knowledge_reviewer.py"), "run"],
        "log": str(JPT_ROOT / "lib" / ".curator.log"),
    },
    "people-curator": {
        "type": "schedule",
        "schedule": {"weekday": 6, "hour": 4, "minute": 0},  # Sunday 4 AM
        "command": ["/usr/bin/python3", str(JPT_ROOT / "lib" / "people_curator.py"), "run"],
        "log": str(JPT_ROOT / "lib" / ".curator.log"),
    },
    "agenda-check": {
        "type": "schedule",
        "schedule": {"hour": 7, "minute": 0},  # 7 AM daily
        "command": ["/usr/bin/python3", str(JPT_ROOT / "lib" / "agenda_processor.py"), "check"],
        "log": str(JPT_ROOT / "agendas" / ".agenda.log"),
    },
}


def log(message: str):
    """Log a message with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    print(log_line)
    try:
        with open(LOG_FILE, "a") as f:
            f.write(log_line + "\n")
    except Exception:
        pass


def load_state() -> dict:
    """Load scheduler state."""
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            pass
    return {"last_run": {}, "run_count": {}}


def save_state(state: dict):
    """Save scheduler state."""
    try:
        STATE_FILE.write_text(json.dumps(state, indent=2))
    except Exception as e:
        log(f"Failed to save state: {e}")


def should_run_interval_task(task_name: str, task: dict, state: dict) -> bool:
    """Check if an interval-based task should run."""
    last_run_str = state.get("last_run", {}).get(task_name)
    if not last_run_str:
        return True

    try:
        last_run = datetime.fromisoformat(last_run_str)
        interval = timedelta(seconds=task["interval_seconds"])
        return datetime.now() >= last_run + interval
    except Exception:
        return True


def should_run_scheduled_task(task_name: str, task: dict, state: dict) -> bool:
    """Check if a scheduled task should run based on its schedule."""
    schedule = task["schedule"]
    now = datetime.now()

    # Check if we already ran today/this week/this month
    last_run_str = state.get("last_run", {}).get(task_name)
    if last_run_str:
        try:
            last_run = datetime.fromisoformat(last_run_str)

            # For monthly tasks
            if "day" in schedule:
                if last_run.year == now.year and last_run.month == now.month:
                    return False

            # For weekly tasks
            elif "weekday" in schedule:
                # Same week check (using isocalendar)
                if last_run.isocalendar()[:2] == now.isocalendar()[:2]:
                    return False

            # For daily tasks
            else:
                if last_run.date() == now.date():
                    return False
        except Exception:
            pass

    # Check if it's time to run
    target_hour = schedule.get("hour", 0)
    target_minute = schedule.get("minute", 0)

    # Check day of month if specified
    if "day" in schedule:
        if now.day != schedule["day"]:
            return False

    # Check weekday if specified (0=Monday, 6=Sunday)
    if "weekday" in schedule:
        if now.weekday() != schedule["weekday"]:
            return False

    # Check time window (within 5 minutes of target)
    target_time = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
    time_diff = abs((now - target_time).total_seconds())

    return time_diff < 300  # Within 5 minute window


def run_task(task_name: str, task: dict) -> bool:
    """Run a single task."""
    log(f"Running task: {task_name}")

    try:
        result = subprocess.run(
            task["command"],
            env=ENV,
            cwd=str(JPT_ROOT),
            capture_output=True,
            text=True,
            timeout=900  # 15 minute timeout
        )

        # Append output to task-specific log if specified
        if "log" in task and result.stdout:
            try:
                with open(task["log"], "a") as f:
                    f.write(result.stdout)
                if result.stderr:
                    with open(task["log"], "a") as f:
                        f.write(result.stderr)
            except Exception:
                pass

        if result.returncode == 0:
            log(f"Task {task_name} completed successfully")
            return True
        else:
            log(f"Task {task_name} failed with code {result.returncode}")
            if result.stderr:
                log(f"  stderr: {result.stderr[:200]}")
            return False

    except subprocess.TimeoutExpired:
        log(f"Task {task_name} timed out")
        return False
    except Exception as e:
        log(f"Task {task_name} error: {e}")
        return False


def dispatch_cycle():
    """Run one dispatch cycle - check all tasks and run those that are due."""
    state = load_state()
    tasks_run = 0

    for task_name, task in TASKS.items():
        should_run = False

        if task["type"] == "interval":
            should_run = should_run_interval_task(task_name, task, state)
        elif task["type"] == "schedule":
            should_run = should_run_scheduled_task(task_name, task, state)

        if should_run:
            success = run_task(task_name, task)
            state["last_run"][task_name] = datetime.now().isoformat()
            state["run_count"][task_name] = state.get("run_count", {}).get(task_name, 0) + 1
            tasks_run += 1

    save_state(state)
    return tasks_run


def cmd_status():
    """Show status of all tasks."""
    state = load_state()
    now = datetime.now()

    print(f"\n{'Task':<25} {'Type':<10} {'Last Run':<20} {'Runs':<6} {'Next'}")
    print("-" * 90)

    for task_name, task in sorted(TASKS.items()):
        task_type = task["type"]
        last_run_str = state.get("last_run", {}).get(task_name, "Never")
        run_count = state.get("run_count", {}).get(task_name, 0)

        # Calculate next run
        next_run = "—"
        if task_type == "interval":
            if last_run_str != "Never":
                try:
                    last_run = datetime.fromisoformat(last_run_str)
                    next_time = last_run + timedelta(seconds=task["interval_seconds"])
                    if next_time > now:
                        delta = next_time - now
                        next_run = f"in {int(delta.total_seconds())}s"
                    else:
                        next_run = "now"
                except Exception:
                    next_run = "now"
            else:
                next_run = "now"
        elif task_type == "schedule":
            schedule = task["schedule"]
            hour = schedule.get("hour", 0)
            minute = schedule.get("minute", 0)

            if "day" in schedule:
                next_run = f"1st @ {hour}:{minute:02d}"
            elif "weekday" in schedule:
                days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
                next_run = f"{days[schedule['weekday']]} @ {hour}:{minute:02d}"
            else:
                next_run = f"Daily @ {hour}:{minute:02d}"

        # Format last run
        if last_run_str != "Never":
            try:
                last_dt = datetime.fromisoformat(last_run_str)
                last_run_str = last_dt.strftime("%Y-%m-%d %H:%M")
            except Exception:
                pass

        print(f"{task_name:<25} {task_type:<10} {last_run_str:<20} {run_count:<6} {next_run}")

    print()


def cmd_daemon():
    """Run as a daemon - continuous dispatch cycles."""
    log("Scheduler daemon starting")

    while True:
        try:
            dispatch_cycle()
        except Exception as e:
            log(f"Dispatch cycle error: {e}")

        time.sleep(60)  # Check every minute


def cmd_trigger(task_name: str):
    """Force run a specific task."""
    if task_name not in TASKS:
        print(f"Unknown task: {task_name}")
        print(f"Available tasks: {', '.join(TASKS.keys())}")
        return

    state = load_state()
    success = run_task(task_name, TASKS[task_name])
    state["last_run"][task_name] = datetime.now().isoformat()
    state["run_count"][task_name] = state.get("run_count", {}).get(task_name, 0) + 1
    save_state(state)

    if success:
        print(f"Task {task_name} completed successfully")
    else:
        print(f"Task {task_name} failed")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "status":
        cmd_status()
    elif cmd == "run":
        tasks = dispatch_cycle()
        print(f"Ran {tasks} task(s)")
    elif cmd == "daemon":
        cmd_daemon()
    elif cmd == "trigger":
        if len(sys.argv) < 3:
            print("Usage: jpt_scheduler.py trigger <task_name>")
            sys.exit(1)
        cmd_trigger(sys.argv[2])
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)
