**Platform Supported**

![Generic badge](https://img.shields.io/badge/Platform-Linux|MacOS|Windows-1f425f.svg)

**Deployments**

[![pages-build-deployment](https://github.com/thevickypedia/pynotification/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/thevickypedia/pynotification/actions/workflows/pages/pages-build-deployment)
[![pypi-publish](https://github.com/thevickypedia/pynotification/actions/workflows/python-publish.yml/badge.svg)](https://github.com/thevickypedia/pynotification/actions/workflows/python-publish.yml)

# PyNotification
Python module to trigger OS-agnostic system notifications.

### Installation
```shell
python -m pip install pynotification
```

### Usage
```python
from pynotification import pynotifier

pynotifier(title="Test title", message="Test message")
```

### Optional arguments
- **icon:** Custom icon to be used for `Linux` and `Windows` operating systems.
  - Linux: Choose any [pre-defined icons](https://wiki.ubuntu.com/Artwork/BreatheIconSet/Icons) or a `.png` file as icon.
  - Windows: Choose any `.ico` file as icon. Defaults to [notification.ico](https://github.com/thevickypedia/pynotification/tree/main/pynotification/notification.ico)
- **destroy:** Boolean value to destroy the notification box on `Windows` operating system after notifying.
- **debug:** Display logs in the form of `info`, `warnings` and `errors` messages.
- **logger:** Bring your own [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger) for custom logging.

## Coding Standards
Docstring format: [`Google`](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) <br>
Styling conventions: [`PEP 8`](https://www.python.org/dev/peps/pep-0008/) <br>
Clean code with pre-commit hooks: [`flake8`](https://flake8.pycqa.org/en/latest/) and 
[`isort`](https://pycqa.github.io/isort/)

## [Release Notes](https://github.com/thevickypedia/pynotification/blob/main/release_notes.rst)
**Requirement**
```shell
python -m pip install changelog-generator
```

**Usage**
```shell
changelog reverse -f release_notes.rst -t 'Release Notes'
```

## Linting
`PreCommit` will ensure linting, and the doc creation are run on every commit.

**Requirement**
```shell
pip install sphinx==5.1.1 pre-commit recommonmark
```

**Usage**
```shell
pre-commit run --all-files
```

## Pypi Package
[![pypi-module](https://img.shields.io/badge/Software%20Repository-pypi-1f425f.svg)](https://packaging.python.org/tutorials/packaging-projects/)

[https://pypi.org/project/pynotification/](https://pypi.org/project/pynotification/)

## Runbook
[![made-with-sphinx-doc](https://img.shields.io/badge/Code%20Docs-Sphinx-1f425f.svg)](https://www.sphinx-doc.org/en/master/man/sphinx-autogen.html)

[https://thevickypedia.github.io/pynotification/](https://thevickypedia.github.io/pynotification/)

## License & copyright

&copy; Vignesh Rao

Licensed under the [MIT License](https://github.com/thevickypedia/pynotification/blob/main/LICENSE)
