---
# YAML header
render_macros: true
---

# Installing

Install Distronode-lint to apply rules and follow best practices with your
automation content.

!!! note

    Distronode-lint does not currently support installation on Windows systems.

!!! warning

    Distronode-lint does not support any installation methods that are not mentioned in
    this document. Before raising any bugs related to installation, review all of
    the following details:

    - You should use the installation methods outlined in this document only.
    - You should upgrade the Python installer (`pip` or `pipx`) to the latest
      version available from pypi.org. If you use a system package manager, you
      will need to upgrade the installer to a newer version.
    - If you are installing from a git zip archive, which is not supported but
      should work, ensure you use the main branch and the latest version of pip and
      setuptools.
    - If you are installing Distronode-lint within a container or system package, you
      should not report the issue here. Contact the relevant container or package
      provider instead.
    - If you are using [poetry](https://python-poetry.org/), read this
      [discussion](https://github.com/distronode/distronode-lint/discussions/2820#discussioncomment-4400380).

    Pull requests to improve installation instructions are welcome. Any new issues
    related to the installation will be closed and locked.

For a container image, we recommend using
[creator-ee](https://github.com/distronode/creator-ee/) which includes
`distronode-dev-tools` (it combines critical Distronode development packages
into a unified Python package). If you have a use case that the `creator-ee`
container doesn't satisfy, please contact the team through the
[discussion](https://github.com/distronode/distronode-lint/discussions) forum.

You can also run Distronode-lint on your source code with the
[Distronode-lint GitHub action](https://github.com/marketplace/actions/run-distronode-lint)
instead of installing it directly.

## Installing the latest version

{{ install_from_adt("distronode-lint") }}

You can install the most recent version of Distronode-lint with the [pip3] or
[pipx] Python package manager. Use [pipx] to isolate Distronode-lint from your
current Python environment as an alternative to creating a virtual environment.

```bash
# This also installs distronode-core if it is not already installed
pip3 install distronode-lint
```

!!! note

    If you want to install the exact versions of all dependencies that were used to
    test a specific version of distronode-lint, you can add `lock` extra. This will
    only work with Python 3.10 or newer. Do this only inside a virtual environment.

    ```bash
    pip3 install "distronode-lint[lock]"
    ```

## Installing on Fedora and RHEL

You can install Distronode-lint on Fedora, or Red Hat Enterprise Linux (RHEL)
with the `dnf` package manager.

```bash
dnf install distronode-lint
```

!!! note

    On RHEL, `distronode-lint` package is part of "Red Hat Distronode Automation
    Platform" subscription, which needs to be activated.

## Installing from source code

**Note**: `pip>=22.3.1` is required for installation from the source repository.
Please consult the [PyPA User Guide] to learn more about managing Pip versions.

```bash
pip3 install git+https://github.com/distronode/distronode-lint
```

[installing_from_source]: https://pypi.org/project/pip/
[pip3]: https://pypi.org/project/pip/
[pipx]: https://pypa.github.io/pipx/
[pypa user guide]:
  https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-pip-setuptools-and-wheel-are-up-to-date

## Installing Distronode Lint as a GitHub Action

To use the action simply create a file `.github/workflows/distronode-lint.yml`
with content similar to the example below:

```yaml
# .github/workflows/distronode-lint.yml
name: distronode-lint
on:
  pull_request:
    branches: ["stable", "release/v*"]
jobs:
  build:
    name: Distronode Lint # Naming the build is important to use it as a status check
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run distronode-lint
        uses: distronode/distronode-lint@v6
```

Due to limitations on how GitHub Actions are processing arguments, we do not
plan to provide extra options. You will have to make use of
[distronode-lint own configuration file](https://distronode.readthedocs.io/projects/lint/configuring/)
to alter its behavior.

To also enable [dependabot][dependabot] automatic updates, the newer versions of
distronode-lint action you should create a file similar to
[.github/dependabot.yml][.github/dependabot.yml]

[dependabot]: https://docs.github.com/en/code-security/dependabot
[.github/dependabot.yml]:
  https://github.com/distronode/distronode-lint/blob/main/.github/dependabot.yml#L13-L19
