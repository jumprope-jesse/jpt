---
type: link
source: notion
url: https://github.com/blixt/sol-mate-eink
notion_type: Software Repo
tags: ['Running']
created: 2024-06-07T15:28:00.000Z
---

# GitHub - blixt/sol-mate-eink: The Sol Mate GPT but on your e-Paper display!

## AI Summary (from Notion)
- Project Overview: The repository is for the "Sol Mate GPT" adapted for e-Paper displays, allowing weather reports to be shown on a Raspberry Pi.
- Creation Date: The project was created on June 7, 2024.
- Status: The project is currently marked as "Not started."
- Key Hardware:
- Raspberry Pi 5
- Waveshare e-Paper 7.3" display (code may need updates for different sizes)
- Software Setup:
- Recommended to use a Python virtual environment, specifically uv.
- Instructions provided for setting up the environment and installing necessary packages.
- Usage Instructions:
- Users must set an OPENAI_API_KEY environment variable.
- The control.py script can be used to generate and display weather images.
- Commands for showing and clearing images are provided.
- Automated Updates: A cron job example is given for updating the display twice daily and clearing it overnight.
- Support: Users can reach out via Twitter or create issues in the repository for assistance.
- Interesting Fact: The project showcases how to integrate AI with physical display technology, allowing dynamic weather reporting.

## Content (from Notion)

# Sol Mate e-Paper Display ☀️

I initially made the ☀️ Sol Mate GPT, but it didn't take too long until I wondered what it would look like on an e-Paper display.

This repository contains all the code that was needed to generate and display a weather report for any specified location on a Raspberry Pi with an attached Waveshare e-Paper display.

## Hardware

- Raspberry Pi 5
- Waveshare e-Paper 7.3" display (code needs to be updated for other sizes)
## More pictures

- 4 examples, some with more color
- The setup, without the box
- Video of the thinness of the display
## Software & Usage

This should all run on your Raspberry Pi.

I recommend setting up a virtual environment for Python, such as uv, first. Here are the instructions for if you're using uv (to be run inside the clone of this repo):

```plain text
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

Without uv:

```plain text
python -m venv .
source .venv/bin/activate
pip install -r requirements.txt
```

You will need to specify an OPENAI_API_KEY environment variable. For your convenience, the code will load environment variables from a .env file in the current working directory.

Now you can use the control.py script to generate an image and show it on the screen:

```plain text
python control.py show Barcelona
```

Don't leave the same image on the display for too long. Use the clear command to clear it:

```plain text
python control.py clear
```

I set up a cron job (crontab -e) to update the image two times per day, but keep in mind this can end up costing a non-trivial amount:

```plain text
0 8 * * * cd ~/src/sol-mate-eink && .venv/bin/python control.py show Barcelona
0 18 * * * cd ~/src/sol-mate-eink && .venv/bin/python control.py show Barcelona
0 2 * * * cd ~/src/sol-mate-eink && .venv/bin/python control.py clear

```

(You'll need to tweak the paths for your setup, of course.)

## Having issues?

I'd love to help if I can – reach out on Twitter or create an issue in this repo!


