---
type: link
source: notion
url: https://github.com/darrenapfel/claudecode-orchestrator
notion_type: Software Repo
tags: ['Running']
created: 2025-08-03T15:51:00.000Z
---

# GitHub - darrenapfel/claudecode-orchestrator: Complete Multi-Agent Orchestration for Claude Code Enables 24 hour Autonomous Coding

## Overview (from Notion)
- This orchestration framework can streamline your software development process, making it easier to manage multiple projects while balancing family life.
- The emphasis on evidence-based development promotes transparency and accountability, which can inspire a culture of honesty in both work and home life.
- The integration of feedback loops allows for continuous improvement, aligning with the values of nurturing both personal and professional relationships.
- Features like global installation protection can resonate with your desire for security and stability in both your personal and professional endeavors.
- The focus on parallel execution aligns with the multitasking demands of parenting, providing insights on managing multiple responsibilities effectively.
- Consider how the structured approach to development can influence your leadership style, fostering collaboration and innovation within your team.
- Alternate views could challenge the reliance on automation and structured workflows, advocating for a more flexible, intuitive approach to both software development and family dynamics.

## AI Summary (from Notion)
The orchestration framework enables Claude Code to function as a full software development team with features like milestone completion protocols, enhanced parallel execution, and evidence-based validation. Key improvements include structured user feedback collection, global install protection, and comprehensive documentation. The system emphasizes honest development practices, ensuring quality through validation and continuous delivery of running software.

## Content (from Notion)

# Claude Code Orchestration System v5.0.0

A comprehensive orchestration framework that enables Claude Code to operate as a full software development team through parallel execution, structured workflows, and evidence-based validation.

## 🎯 Core Philosophy

Quality Through Truth: The system enforces honest development practices where every claim requires evidence, every test result must be shown, and validation failures are documented and fixed rather than hidden. This approach paradoxically saves tokens by catching issues early rather than building on broken foundations.

## ✨ What's New in v5.0.0

### 🚀 Milestone Completion Protocol

- Service Startup & Validation: Services are started and smoke-tested before declaring completion
- User Testing Materials: Auto-generated testing guides from user stories
- Human Feedback Loop: Structured feedback collection and processing
- Live Deployment: Milestones end with running, accessible services
### ⚡ Enhanced Parallel Execution

- Visual Execution Guides: Clear indicators for parallel vs sequential tasks
- Parallel Execution Detector: System-level warnings against sequential execution
- One Message Rule: Multiple independent tasks MUST be created simultaneously
### 🔒 Global Install Protection

- Confirmation Prompts: Prevents accidental overwrite of global configurations
- Safe Defaults: Cancels on any input except explicit 'y' confirmation
### 📚 Documentation Improvements

- Single Source of Truth: Master reference documents eliminate contradictions
- Organized Structure: Guides separated from patterns for clarity
- Quick References: Fast access to common commands and paths
## 🚀 Quick Start

### Global Installation (Recommended)

```plain text
# Install globally for use across all projects
./orchestrator.sh global
# ⚠️ WARNING: This will replace ~/.claude/claude.md - confirm carefully!

# Then in any project:
./orchestrator.sh local
```

### Local Installation Only

```plain text
# Install directly in current project
./orchestrator.sh local
```

## 🏗️ System Architecture

### Parallel Execution Model

The orchestrator manages multiple specialized personas working simultaneously:

```plain text
FOUNDATION STEP
╔═══════════════════════════════════════════════════════════╗
║  ⚡ PARALLEL: ONE MESSAGE - BOTH TASKS TOGETHER! ⚡      ║
╚═══════════════════════════════════════════════════════════╝
├── Task: @architect - Design architecture
└── Task: @ux-designer - Create user flows

```

### Milestone-Based Development

Work is organized into major development phases with service delivery:

```plain text
.work/
├── milestones/
│   └── 20250105-user-authentication/
│       ├── sprint-001/
│       │   ├── tasks/
│       │   ├── integration/
│       │   ├── validation-1/
│       │   ├── fixes/cycle-1/
│       │   ├── validation-2/
│       │   └── completion/
│       │       ├── MILESTONE-COMPLETION.md
│       │       ├── USER-STORIES-TESTING-GUIDE.md
│       │       └── USER-FEEDBACK-FORM.md
│       └── milestone-completion-summary.md
└── foundation/
    ├── architecture/
    ├── product/
    └── ux/

```

### Git Integration

Every validated task is automatically committed with file isolation:

- Task-level commits: Each task commits only its specific files
- Orchestrator announces: All git actions visible in chat
- File tracking: Prevents cross-contamination between parallel work
- Integration commits: Connect separate features cleanly
## 🎉 Milestone Completion Process

### 1. Service Startup & Validation

When a milestone completes, the system:

- Starts the service in the background
- Validates endpoints are responding
- Runs smoke tests to ensure basic functionality
- Provides the running URL to the user
### 2. User Testing Materials

Automatically generates three documents:

- MILESTONE-COMPLETION.md: Overview and testing instructions
- USER-STORIES-TESTING-GUIDE.md: Test scenarios from original requirements
- USER-FEEDBACK-FORM.md: Structured feedback collection
### 3. Human Feedback Loop

```plain text
User: "The login button is hard to find"
System: Creates feedback sprint → Implements fix → Re-validates → Updates service

```

### 4. Completion Announcement

```plain text
🎉 MILESTONE [Authentication System] COMPLETE - Service Running & Ready for Testing

✅ VALIDATION: All validators passed
✅ SERVICE: Running and validated at http://localhost:3000
✅ DOCUMENTATION: All testing materials prepared

🎯 USER TESTING - READY NOW:
   ✅ Service URL: http://localhost:3000 (already running)
   📖 Test scenarios: See USER-STORIES-TESTING-GUIDE.md
   📝 Report issues: Fill out USER-FEEDBACK-FORM.md
   🔄 Submit feedback: "Please process the user feedback file"

Just open http://localhost:3000 and start testing!

```

## 📋 Key Features

### Evidence-Based Development

- Every task produces EVIDENCE.md with reproducible proof
- Test outputs must be complete, not summarized
- Screenshots require timestamps
- Commands must show actual execution
### Fix Cycle Protocol

- Validation failures trigger fix cycles (normal and expected)
- Each fix cycle is documented and committed
- Multiple cycles show honest development progress
- Success is achieving 100% pass, not avoiding failures
### Master Reference Documents

- MASTER-DIRECTORY-STRUCTURE.md - Single source of truth for organization
- GIT-COMMIT-STRATEGY.md - Authoritative git workflow
- PARALLEL-EXECUTION-GUIDE.md - Visual guide to parallel execution
## 👥 Available Personas

### Core Team

- Orchestrator - Manages parallel execution and git operations
- Product Manager - Defines requirements and validates user value
- Architect - Designs system structure and technical approach
- Software Engineer - Implements features following architecture
- UX Designer - Creates user experiences and interfaces
### Quality Assurance

- SDET - Writes comprehensive test suites
- Test Engineer - Validates end-to-end functionality & starts services
- Integration Engineer - Ensures components work together
- Performance Engineer - Optimizes speed and scalability
- Security Engineer - Validates security and compliance
### Support Roles

- DevOps - Handles deployment and infrastructure
- Documentation Writer - Creates user and technical docs
## 🔄 Workflow Overview

1. Discovery (if needed) - Gather clarifying questions
1. Requirements - PM defines scope and acceptance criteria
1. Foundation Design - Architect and UX Designer create blueprint
1. Implementation - Engineers build in parallel batches
1. Integration - Connect all components and fix issues
1. Validation - Four validators verify quality
1. Fix Cycles - Address any validation failures
1. Milestone Completion - Start service and prepare for user testing
1. Feedback Processing - Implement user-reported improvements
## 📁 Project Structure

```plain text
your-project/
├── .claude/                 # Orchestration configuration
│   ├── personas/           # AI role definitions
│   ├── patterns/           # Workflow patterns
│   ├── guides/             # How-to documentation
│   ├── validators/         # Validation protocols
│   └── preferences/        # Project settings
├── .work/                  # Orchestration workspace
│   ├── foundation/         # Core architecture/design
│   ├── milestones/         # Development phases
│   └── discovery/          # Project understanding
├── CLAUDE.md               # Project-specific instructions
└── src/                    # Your actual code

```

## 🔍 Validation Process

Four validators work in parallel to ensure quality:

1. Product Manager - Validates user stories work end-to-end
1. Test Engineer - Runs comprehensive test suites & service startup
1. Performance Engineer - Checks speed and scalability
1. Security Engineer - Validates security compliance
Any validation failure triggers fix cycles until all pass.

## 💡 Best Practices

### For Maximum Effectiveness

1. Trust the Process - Multiple fix cycles are normal, not failures
1. Let Services Run - Milestones deliver running software, not just code
1. Provide Feedback - Use the structured feedback forms for improvements
1. Review Evidence - Check the .work/ directory to see actual outputs
1. Watch Git Actions - All commits are announced in chat
### Common Patterns

- New Project: Discovery → Full implementation → Running service
- Add Feature: Skip discovery → Start at requirements → Update service
- Fix Bugs: Create fix tasks → Validate thoroughly → Deploy fixes
- User Feedback: Process feedback form → Sprint for fixes → Re-validate
## 🐛 Troubleshooting

### Service Won't Start

- Check logs in .work/milestones/*/sprint-*/completion/service.log
- Verify all dependencies installed
- Test engineer will diagnose and create fix tasks
### Parallel Execution Issues

- Look for "Let me create the first task..." - this indicates sequential execution
- Check PARALLEL-EXECUTION-GUIDE.md for visual examples
- Orchestrator should create ALL independent tasks in ONE message
### Git Conflicts

- Orchestrator tracks file ownership to prevent conflicts
- Integration commits handle shared file updates
- Check GIT-TROUBLESHOOTING.md for solutions
## 📚 Documentation

Core documentation in .claude/:

### Guides (How-To)

- guides/TASK-EXECUTION-GUIDE.md - Comprehensive task execution
- guides/deployment-setup-guide.md - Deployment configuration
- guides/existing-project-onboarding.md - Adding to existing projects
### Patterns (Protocols)

- patterns/standard-workflow.md - Complete workflow with visual diagrams
- patterns/GIT-COMMIT-STRATEGY.md - Master git workflow reference
- patterns/PARALLEL-EXECUTION-GUIDE.md - Visual parallel execution guide
- patterns/milestone-completion-protocol.md - Service delivery process
### Quick References

- patterns/GIT-QUICK-REFERENCE.md - Common git commands
- patterns/DIRECTORY-QUICK-REFERENCE.md - Quick navigation guide
- patterns/COMMON-PATHS.md - Frequently used paths
## 🤝 Contributing

The orchestration system is built from the orchestrator-files/ directory:

1. Modify files in orchestrator-files/
1. Run node build-orchestrator.js to rebuild
1. Test with ./orchestrator.sh local
1. Submit improvements via pull request
See .ignore-working-docs/HOW-TO-BUILD-AND-TEST-ORCHESTRATOR-SH.md for details.

## 📈 Version History

### v5.0.0 (Current Release)

- Milestone Completion Protocol: Services start and run for user testing
- Human Feedback Loop: Structured feedback collection and processing
- Enhanced Parallel Execution: Visual guides and system-level enforcement
- Global Install Protection: Confirmation prompts prevent accidents
- Documentation Overhaul: Single source of truth, better organization
### v4.x

- Task-level git commits with file isolation
- Orchestrator announces all git actions
- Master reference documents
- Numbered validation cycles
### v3.x

- Parallel execution model
- Evidence-based validation
- Session management
## 🎯 Why It Works

The orchestration system succeeds by:

1. Delivering Running Software - Milestones end with live services
1. Enforcing Parallelism - Multiple tasks progress simultaneously
1. Validating Continuously - Catch issues early, fix immediately
1. Collecting Human Feedback - Structured process for improvements
1. Tracking Everything - Complete audit trail of all work
## 📞 Support

- Issues: GitHub Issues
- Discussions: GitHub Discussions
- Wiki: Documentation Wiki
Built with the principle that honest development with visible evidence produces better software faster than hiding failures and building on broken foundations. Now with live service delivery and human feedback integration.

## Summary

This PR introduces v4.5.0, a major evolution of the orchestration system that includes all improvements from v4.0 through v4.5.

### 🔍 Discovery Step (NEW in v4.5)

- One-time clarifying questions from 6 personas (0-3 each)
- Prevents building the wrong thing by gathering context upfront
- Context stored and used throughout all sprints
- Never repeated - applies to entire project lifecycle
### 📝 Streamlined Orchestrator (v4.5)

- 40% reduction in orchestrator.md for better clarity
- Clear separation between workflow and execution
- References standard-workflow.md as authoritative source
- Removed redundancies and overly specific examples
### 🚀 Core v4.0 Features Included

- PM-first development with requirements driving architecture
- Mandatory testing infrastructure as first implementation task
- Integration reconciliation step catches mismatches early
- 4 parallel validators enforce quality (no shortcuts)
- Fix→Integration→Validation cycle prevents false victories
- Continuous execution until 100% features work
### 📊 Comprehensive Changes

- 43 files changed
- 4,533 insertions, 3,177 deletions
- Sprint/milestone/batch terminology throughout
- New discovery question templates for all personas
- Enhanced validation preventing 'page loads = working' theater
- Complete E2E testing requirements
### ✅ Testing

- Build script validated and updated to v4.5.0
- Generated orchestrator.sh tested with local install
- All 80 files install correctly including discovery templates
- Backwards compatible with existing projects
## Breaking Changes

None - fully backward compatible. Existing PROJECT-STATE.md and work history preserved.

## Key Improvements Since v3.9

1. Discovery Step - Clarifies vague requirements upfront
1. PM-First Workflow - User needs drive all development
1. Mandatory Testing - Can't skip to features without test infrastructure
1. Integration Reconciliation - Dedicated step to fix mismatches
1. Honest Validation - 'Working' means end-to-end functionality
1. Continuous Delivery - Automatically continues through all milestones

