[![REUSE status](https://api.reuse.software/badge/github.com/SAP/invoke-plugin-for-sphinx)](https://api.reuse.software/info/github.com/SAP/invoke-plugin-for-sphinx)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![PyPI version](https://badge.fury.io/py/invoke-plugin-for-sphinx.svg)](https://badge.fury.io/py/invoke-plugin-for-sphinx)

# Invoke Plugin for Sphinx
This is a plugin which allows the documentation of invoke tasks with sphinx `autodoc`.
An invoke task looks like a normal function but the `@task` decorator creates a `Task` object behind the scenes.
Documenting these with `autodoc` can lead to errors or unexpected results.

## Installation
`pip install invoke-plugin-for-sphinx`, that's it.

## Usage
Add the plugin to the extensions list:

```py
extensions = ["invoke_plugin_for_sphinx"]
```

Then you can use `.. automodule::` as usual.
Behind the scenes, the function documenter of `autodoc` is extended to also handle tasks equal to functions.
Therefore the same configurations, limitations and features apply.

## Build and Publish

This project uses `setuptools` as the dependency management and build tool.
To publish a new release, follow these steps:
* Update the version in the `pyproject.toml`
* Add an entry in the changelog
* Push a new tag like `vX.X.X` to trigger the release

## Support, Feedback, Contributing

This project is open to feature requests/suggestions, bug reports etc. via [GitHub issues](https://github.com/SAP/invoke-plugin-for-sphinx/issues). Contribution and feedback are encouraged and always welcome. For more information about how to contribute, the project structure, as well as additional contribution information, see our [Contribution Guidelines](CONTRIBUTING.md).

## Code of Conduct

We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for everyone. By participating in this project, you agree to abide by its [Code of Conduct](CODE_OF_CONDUCT.md) at all times.

## Licensing

Copyright 2023 SAP SE or an SAP affiliate company and invoke-plugin-for-sphinx contributors. Please see our [LICENSE](LICENSE) for copyright and license information. Detailed information including third-party components and their licensing/copyright information is available [via the REUSE tool](https://api.reuse.software/info/github.com/SAP/invoke-plugin-for-sphinx).
