---
type: link
source: notion
url: https://github.com/Yooooomi/your_spotify
notion_type: Software Repo
tags: ['Running']
created: 2024-04-05T04:39:00.000Z
---

# GitHub - Yooooomi/your_spotify: Self hosted Spotify tracking dashboard

## AI Summary (from Notion)
- Project Overview: The document outlines a self-hosted application called YourSpotify, which tracks users' listening habits and provides a dashboard for statistics.
- Creation Date: The project was created on April 5, 2024.
- Status: The project is currently not started.
- Core Components:
- A web server that polls the Spotify API for data.
- A web application for users to explore their listening statistics.
- Installation Options:
- Using Docker: Recommended method with a provided docker-compose example.
- Local Installation: Not recommended due to complexity.
- Prerequisites:
- Requires a Spotify application ID and associated keys.
- Needs an authorized redirect URI.
- Configuration Options: Various environment variables must be set for proper functionality, including API endpoints and Spotify keys.
- Data Import: Users can import historical data from Spotify via privacy settings.
- Supported Methods: Privacy data and full privacy data (recommended).
- Troubleshooting: Guidance for failed imports and potential issues.
- FAQ Section: Addresses common user questions regarding app functionality and data syncing.
- Contributions: Encourages community involvement for improvements and bug reporting.
- Sponsoring: The creator seeks support for ongoing development and maintenance.

## Content (from Notion)

# Your Spotify

YourSpotify is a self-hosted application that tracks what you listen and offers you a dashboard to explore statistics about it! It's composed of a web server which polls the Spotify API every now and then and a web application on which you can explore your statistics.

# Table of contents

- Prerequisites
- Installation 
- Creating the Spotify application
- Importing past history 
- FAQ
- External guides
- Contributing
- Sponsoring
# Prerequisites

1. You have to own a Spotify application ID that you can create through their dashboard.
1. You need to provide the Server environment the public AND secret key of the application (cf. Installation).
1. You need to provide an authorized redirect URI to the docker-compose file.
> 

# Installation

## Using docker-compose

Follow the docker-compose-example.yml to host your application through docker.

```plain text
version: "3"

services:
  server:
    image: yooooomi/your_spotify_server
    restart: always
    ports:
      - "8080:8080"
    links:
      - mongo
    depends_on:
      - mongo
    environment:
      API_ENDPOINT: http://localhost:8080 # This MUST be included as a valid URL in the spotify dashboard (see below)
      CLIENT_ENDPOINT: http://localhost:3000
      SPOTIFY_PUBLIC: __your_spotify_client_id__
      SPOTIFY_SECRET: __your_spotify_secret__
  mongo:
    container_name: mongo
    image: mongo:6
    volumes:
      - ./your_spotify_db:/data/db

  web:
    image: yooooomi/your_spotify_client
    restart: always
    ports:
      - "3000:3000"
    environment:
      API_ENDPOINT: http://localhost:8080
```

> 

## Installing locally (not recommended)

You can follow the instructions here. Note that you will still have to do the steps below.

## Environment

## CORS

- Not defining it will default to authorize only the CLIENT_ENDPOINT origin.
- origin1,origin2 will allow origin1 and origin2.
> 

# Creating the Spotify Application

For YourSpotify to work you need to provide a Spotify application public AND secret to the server environment. To do so, you need to create a Spotify application here.

1. Click on Create app.
1. Fill out all the information.
1. Set the redirect URI, corresponding to your server location on the internet (or your local network) adding the suffix /oauth/spotify/callback (/api/oauth/spotify/callback if using the linuxserver image).
- i.e: http://localhost:8080/oauth/spotify/callback or http://home.mydomain.com/your_spotify_backend/oauth/spotify/callback
1. Check Web API
1. Check I understand and agree
1. Hit Settings at the top right corner
1. Copy the public and the secret key into your docker-compose file under the name of SPOTIFY_PUBLIC and SPOTIFY_SECRET respectively.
1. Once you have created your application, Spotify wants you to register the users that will be able to access the application. (You don't need to do that for the account that created the application) 
# Importing past history

By default, YourSpotify will only retrieve data for the past 24 hours once registered. This is a technical limitation. However, you can import previous data by two ways.

The import process uses cache to limit requests to the Spotify API. By default, the cache size is unlimited, but you can limit is with the MAX_IMPORT_CACHE_SIZE env variable in the server.

## Supported import methods

### Privacy data

> 

- Request your privacy data at Spotify to have access to your history for the past year here.
- Head to the Settings page and choose the Account data method.
- Input your files starting with StreamingHistoryX.json.
- Start your import.
### Full privacy data (recommended)

> 

- Request your Full privacy data to have access to your history data since the creation of the account here.
- Head to the Settings page and choose the Extended streaming history method.
- Input your files starting with endsongX.json.
- Start your import.
## Troubleshoot

An import can fail:

- If the server reboots.
- If a request fails 10 times in a row.
A failed import can be retried in the Settings page. Be sure to clean your failed imports if you do not want to retry it as it will remove the files used for it.

It is safer to import data at account creation. Though YourSpotify detects duplicates, some may still be inserted.

# FAQ

> 

From an admin account, go to the Settings page and hit the Disable new registrations button.

> 

This can happen if you revoked access on your Spotify account. To re-sync the songs, go to settings and hit the Relog to Spotify button.

> 

This means that your web application can't connect to the backend. Check that your API_ENDPOINT env variable is reachable from the device you're using the platform from.

> 

Any user can set his proper timezone in the settings, it will be used for any computed statistics. The timezone of the device will be used for everything else, such as song history.

# External guides

- BreadNet installation tutorial
# Contributing

If you have any issue or any idea that could make the project better, feel free to open an issue. I'd love to hear about new ideas or bugs you are encountering.

# Sponsoring

I work on this project on my spare time and try to fix issues as soon as I can. If you feel generous and think this project and my investment are worth a few cents, you can consider sponsoring it with the button on the right, many thanks.


