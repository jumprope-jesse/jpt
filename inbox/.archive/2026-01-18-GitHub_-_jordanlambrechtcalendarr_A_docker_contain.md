---
type: link
source: notion
url: https://github.com/jordanlambrecht/calendarr
notion_type: Software Repo
tags: ['Running']
created: 2025-05-21T04:25:00.000Z
---

# GitHub - jordanlambrecht/calendarr: A docker container that will publish Sonarr and Radarr's release calendar to Discord + Slack on a weekly/daily basis

## Overview (from Notion)
- Automating reminders for your family's favorite TV shows and movies can help streamline your household schedule.
- Integrating notifications into Discord or Slack can keep your family updated on upcoming releases without needing constant manual checks.
- The tool can be a fun way to engage with your kids about their favorite shows, fostering shared interests and discussions.
- Consider using it as a teaching moment about technology, Docker, and automation, showcasing how software can simplify daily life.
- The project reflects current trends in personalizing digital experiences and leveraging community tools, aligning with your role as a founder in tech.
- Explore the possibility of expanding it to include custom features relevant to your family's interests, like integrating with other services or platforms.
- Think about how managing such notifications can enhance quality time by reducing the chaos of overlapping schedules.

## AI Summary (from Notion)
A Docker container that fetches TV and movie release calendars from Sonarr and Radarr, posting updates to Discord and Slack on a customizable schedule. Features include grouping by day, deduplication of events, and extensive configuration options for notifications.

## Content (from Notion)

# 📆 Calendarr

A simple Docker container that fetches upcoming airings/releases for TV shows and movies from Sonarr and Radarr calendars and posts them to Discord on a schedule.

## ✨ Features

- Combines multiple Sonarr and Radarr calendar feeds
- Groups shows and movies by day of the week
- Runs on a customizable schedule (daily or weekly)
- Supports both Discord and Slack notifications
- Highly customizable configuration
## 🚀 Usage

Images available via either ghcr.io/jordanlambrecht/calendarr:latest or jordyjordyjordy/calendarr:latest

### With Docker Compose (Recommended)

1. 
1. 
```plain text
DISCORD_WEBHOOK_URL=your_discord_webhook_url
SLACK_WEBHOOK_URL=your_discord_webhook_url
ICS_URL_SONARR_1=your_sonarr_calendar_url
ICS_URL_SONARR_2=your_anime_sonarr_calendar_url
ICS_URL_RADARR_1=your_radarr_calendar_url

...and so on and so on and turtles all the way down
```

### With Docker Run (If you like pain)

```plain text
docker run -d \
  --name calandarr \
  -e DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/your_webhook" \
  -e CALENDAR_URLS='[{"url":"https://sonarr.example.com/feed/calendar/api.ics","type":"tv"},{"url":"https://radarr.example.com/feed/calendar/api.ics","type":"movie"}]' \
  -e CUSTOM_HEADER="My Media Guide" \
  -e SHOW_DATE_RANGE="true" \
  -e START_WEEK_ON_MONDAY="true" \
  -e RUN_ON_STARTUP="true" \
  jordyjordyjordy/calendarr:latest
```

### To Run Offschedule

1. Start the container via the compose file with docker compose up -d
1. Use the command docker exec calandarr python /app/main.py as willy nilly as you wish
## 🛠️ Configuration

- Required. ** Required if USE_DISCORD is true. *** Required if USE_SLACK is true.
## Schedule Configuration

Set when and how often the calendar runs:

- RUN_TIME: When to run each day (format: HH:MM in 24-hour time, e.g., "09:30")
- SCHEDULE_TYPE: Either "DAILY" or "WEEKLY"
- CALENDAR_RANGE: "AUTO", "DAY", or "WEEK" - controls how many days of events to show 
You can also use CRON_SCHEDULE for direct cron expressions (overrides all other schedule settings. Don't use this unless you have a good reason and know what you're doing)

## ✍️ Custom Footers

You can add custom text to the end of your Discord and Slack announcements using Markdown files.

1. 
1.  
1.  
If the footer files are missing or cannot be read, the app will log a warning and omit the footer without failing.

## 🤝 Obtaining Calendar URLs

### Sonarr

1. Go to Calendar > iCal Link
1. Leave all three checkboxes blank
1. Optionally set tags for shows you want to announce
1. Copy the ical link
Alternatively:

1. Go to Settings > General
1. Under "Security" section, look for "API Key"
1. Copy the API key
1. Your calendar URL will be: http://your-sonarr-url/feed/v3/calendar/Sonarr.ics?apikey=YOUR_API_KEY
### Radarr

1. Go to Calendar > iCal Link
1. Leave all three checkboxes blank
1. Optionally set tags for movies you want to announce
1. Copy the ical link
Alternatively:

1. Go to Settings > General
1. Under "Security" section, look for "API Key"
1. Copy the API key
1. Your calendar URL will be: http://your-radarr-url/feed/v3/calendar/Radarr.ics?apikey=YOUR_API_KEY
## Slack Webhooks Setup

More info here on how to obtain a slack webhook URL if you get lost.

You can set up the Slack app using the provided manifest file:

1. Go to https://api.slack.com/apps
1. Click "Create New App" and select "From an app manifest"
1. Select your workspace and click "Next"
1. Copy and paste the contents of the slack-manifest.yaml file from this repository
1. Click "Next" and then "Create"
1. Once created, navigate to "Incoming Webhooks" in the sidebar
1. Toggle "Activate Incoming Webhooks" to On
1. Click "Add New Webhook to Workspace"
1. Select the channel where you want to receive updates
1. Copy the Webhook URL provided and use it as your SLACK_WEBHOOK_URL environment variable
## 🌟 First Timers

If you're new to Docker, it's fairly easy to get this going. I won't post an in-depth guide- there's Plenty on the internet. The general gist is:

1. Install Docker Desktop for your platform (Windows, Mac, or Linux)
1. Create a new folder for your Calendarr setup via Terminal: mkdir calendarr && cd calendarr
1. Create these two files:
- A .env file with your configuration (see example above)
- A docker-compose.yml file with, at a minimum:
```plain text
---
name: calendarr
services:
  calendarr:
    image: ghcr.io/jordanlambrecht/calendarr:latest
    restart: "unless-stopped"
    container_name: calendarr
    environment:
      USE_DISCORD: "true"
      DISCORD_WEBHOOK_URL: ${DISCORD_WEBHOOK_URL} # Reference the .env.example for more info
      CALENDAR_URLS: >
        [{
          "url":"${ICS_URL_SONARR_1}",
          "type":"tv"
        },
        {
          "url":"${ICS_URL_RADARR_1}",
          "type":"movie"
        }]
      CUSTOM_HEADER: "TV Guide - What's Up This Week"
      TZ: "America/Chicago"  # Change to your timezone
      SCHEDULE_TYPE: "WEEKLY" # Or "DAILY"
      RUN_TIME: "09:00"       # Time to run the job (HH:MM)
    volumes:
      - ./logs:/app/logs:rw
```

1. Open a terminal in that folder and run: docker compose up -d
1. Check if it's working: docker logs calendarr -f
That's it! The container will immediately run once (if RUN_ON_STARTUP is true) and then according to the schedule you've set.

## 🧑‍💻 Contributing

The two biggest things I need help with right now are:

- Adding friendly timezone names to the TIMEZONE_NAME_MAP in the constants.py file
- Translations. There is no localization structure implemented yet, but it would be great to get a head start in things like spanish, etc
## 🛒 ToDo

Features I'd like to maybe implement:

- Localization
- More platform integrations
- Potentially a web ui
## 🚧 Development

If you want to build the container yourself:

```plain text
git clone https://github.com/jordanlambrecht/calendarr.git
cd calendarr
docker build -t calendarr .
```

## 🧑‍⚖️ License

GNU GENERAL PUBLIC LICENSE


