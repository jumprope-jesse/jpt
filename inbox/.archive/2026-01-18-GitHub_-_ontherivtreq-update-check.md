---
type: link
source: notion
url: https://github.com/ontherivt/req-update-check
notion_type: Software Repo
tags: ['Running']
created: 2025-05-09T02:08:00.000Z
---

# GitHub - ontherivt/req-update-check

## Overview (from Notion)
- Keeping dependencies updated is crucial for maintaining software security and performance, especially for projects that might impact your business or responsibilities.
- The tool simplifies the process of checking for package updates, saving time that can be better spent on family or innovative projects.
- Understanding how to leverage Python tools can enhance your skills, potentially leading to better solutions for your software projects.
- Emphasizing the importance of documentation and community contributions can foster a collaborative culture, both in your team and in your personal projects.
- The project’s open-source nature aligns with a spirit of sharing and collaboration, which can be a great example to set for your children about the value of community and teamwork.
- Consider the potential for using this tool to teach your kids about programming and software maintenance in a practical, engaging way.
- An alternate view is to assess whether the time spent on maintaining dependencies detracts from more strategic areas of development—balancing between maintenance and innovation is key.

## AI Summary (from Notion)
A Python tool to check for package updates in requirements.txt files, featuring update severity display, optional file caching, and support for comments. Install via PyPI or directly from the repo, with command line options for customization.

## Content (from Notion)

# req-update-check

A Python tool to check your requirements.txt file for package updates, with optional file caching for better performance.

## Features

- Check for available updates in your requirements.txt file
- Show update severity (major/minor/patch)
- Display package homepages and changelogs when available
- Optional file caching for faster repeated checks
- Support for comments and inline comments in requirements.txt
- Ignores pre-release versions (alpha, beta, release candidates)
## Installation

Install from PyPI:

```plain text
pip install req-update-check
```

Or install from the repo directly:

```plain text
pip install git+https://github.com/ontherivt/req-update-check.git
```

Or install from source:

```plain text
git clone https://github.com/ontherivt/req-update-check.git
cd req-update-check
pip install -e .
```

## Usage

Basic usage:

```plain text
req-update-check requirements.txt
```

### Command Line Options

```plain text
req-update-check [-h] [--no-cache] [--cache-dir CACHE_DIR] requirements_file
```

Arguments:

- requirements_file: Path to your requirements.txt file
Options:

- -no-cache: Disable file caching
- -cache-dir: Custom cache directory (default: ~/.req-update-check-cache)
### Example Output

```plain text
File caching enabled
The following packages need to be updated:

requests: 2.28.0 -> 2.31.0 [minor]
    Pypi page: https://pypi.python.org/project/requests/
    Homepage: https://requests.readthedocs.io
    Changelog: https://requests.readthedocs.io/en/latest/community/updates/#release-history

redis: 4.5.0 -> 5.0.1 [major]
    Pypi page: https://pypi.python.org/project/redis/
    Homepage: https://github.com/redis/redis-py
    Changelog: https://github.com/redis/redis-py/blob/master/CHANGES

```

### Using file Caching

The tool supports file caching to improve performance when checking multiple times. You can configure the cache storage:

```plain text
req-update-check --cache-dir ~/.your-cache-dir requirements.txt
```

## Requirements.txt Format

The tool supports requirements.txt files with the following formats:

```plain text
package==1.2.3
package == 1.2.3  # with spaces
package==1.2.3  # with inline comments
# Full line comments

```

Note: Currently only supports exact version specifiers (==). Support for other specifiers (like >=, ~=) is planned for future releases.

## Python API

You can also use req-update-check as a Python library:

```plain text
from req_update_check import Requirements

# Without file cache
req = Requirements('requirements.txt', allow_cache=False)
req.check_packages()
req.report()

# With file cache defaults
req = Requirements('requirements.txt')
req.check_packages()
req.report()
```

## Development

To set up for development:

1. Clone the repository
1. Create a virtual environment: python -m venv venv
1. Activate the virtual environment: source venv/bin/activate (Unix) or venv\Scripts\activate (Windows)
1. Install development dependencies: pip install -e ".[dev]"
To run tests:

1. python -m unittest
## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


