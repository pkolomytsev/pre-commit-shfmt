# pre-commit-shfmt

This package provides a pip-installable [shfmt][1] binary (mostly for
pre-commit purposes). It uses a custom build-backend, [pre-commit-download][2],
so downloading the executable is done during the wheel build process.

## Installation

<!-- markdownlint-disable MD013 -->

```bash
pip install git+https://github.com/pkolomytsev/pre-commit-shfmt.git@v3.8.0.0
```

<!-- markdownlint-enable MD013 -->

## Usage

As a regular executable from your environment:

```bash
shfmt -V
```

As a [pre-commit][3] hook:

```yaml
repos:
  - repo: https://github.com/pkolomytsev/pre-commit-shfmt
    rev: v3.8.0.0
    hooks:
      - id: shfmt
```

[1]: https://github.com/mvdan/sh
[2]: https://github.com/pkolomytsev/pre-commit-download
[3]: https://pre-commit.com/
