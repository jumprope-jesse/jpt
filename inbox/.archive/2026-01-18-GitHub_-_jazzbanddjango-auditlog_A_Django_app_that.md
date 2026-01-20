---
type: link
source: notion
url: https://github.com/jazzband/django-auditlog
notion_type: Software Repo
tags: ['Running']
created: 2024-05-25T14:40:00.000Z
---

# GitHub - jazzband/django-auditlog: A Django app that keeps a log of changes made to an object.

## AI Summary (from Notion)
- Project Overview: django-auditlog is a Django app designed to log changes made to objects, focusing on simplicity and performance.
- Core Functionality:
- Logs changes to models along with the user (actor) who made these changes.
- Saves change summaries in JSON format for easy tracking.
- Comparative Advantage: Offers more flexibility than Django’s built-in admin logging feature.
- Documentation: Available online, with source files in the docs folder.
- License: MIT license, allowing for extensive use and modification.
- Contribution Welcome: Users are encouraged to fork the repository or create pull requests for improvements.
- Release Process:
- Ensure tests are passing on the master branch before creating a new version branch.
- Update the CHANGELOG and merge pull requests to manage releases.
- Notifications are sent out upon release to inform users of new package availability.
- Initial Release Date: May 25, 2024, with the status currently listed as "Not started."

## Content (from Notion)

# django-auditlog

Migrate to V3

Check the Upgrading to version 3 doc before upgrading to V3.

django-auditlog (Auditlog) is a reusable app for Django that makes logging object changes a breeze. Auditlog tries to use as much as Python and Django's built in functionality to keep the list of dependencies as short as possible. Also, Auditlog aims to be fast and simple to use.

Auditlog is created out of the need for a simple Django app that logs changes to models along with the user who made the changes (later referred to as actor). Existing solutions seemed to offer a type of version control, which was found excessive and expensive in terms of database storage and performance.

The core idea of Auditlog is similar to the log from Django's admin. Unlike the log from Django's admin (django.contrib.admin) Auditlog is much more flexible. Also, Auditlog saves a summary of the changes in JSON format, so changes can be tracked easily.

## Documentation

The documentation for django-auditlog can be found on https://django-auditlog.readthedocs.org. The source files are available in the docs folder.

## License

Auditlog is licensed under the MIT license (see the LICENSE file for details).

## Contribute

If you have great ideas for Auditlog, or if you like to improve something, feel free to fork this repository and/or create a pull request. I'm open for suggestions. If you like to discuss something with me (about Auditlog), please open an issue.

## Releases

1. Make sure all tests on master are green
1. Create a new branch vX.Y.Z from master for that specific release
1. Update the CHANGELOG release date
1. Pull request vX.Y.Z -> master
1. As a project lead, once the PR is merged, create and push a tag vX.Y.Z: this will trigger the release build and a notification will be sent from Jazzband of the availability of two packages (tgz and wheel)
1. Test the install
1. Publish the release to PyPI

