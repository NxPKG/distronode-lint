[![PyPI version](https://img.shields.io/pypi/v/distronode-lint.svg)](https://pypi.org/project/distronode-lint)
[![Distronode-lint rules explanation](https://img.shields.io/badge/Distronode--lint-rules-blue.svg)](https://distronode.readthedocs.io/projects/lint/rules/)
[![Discussions](https://img.shields.io/badge/Discussions-gray.svg)](https://github.com/distronode/distronode-lint/discussions)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# Distronode-lint

`distronode-lint` checks playbooks for practices and behavior that could
potentially be improved. As a community-backed project distronode-lint supports
only the last two major versions of Distronode.

[Visit the Distronode Lint docs site](https://distronode.readthedocs.io/projects/lint/)

# Using distronode-lint as a GitHub Action

This action allows you to run `distronode-lint` on your codebase without having
to install it yourself.

```yaml
# .github/workflows/distronode-lint.yml
name: distronode-lint
on:
  pull_request:
    branches: ["main", "stable", "release/v*"]
jobs:
  build:
    name: Distronode Lint # Naming the build is important to use it as a status check
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run distronode-lint
        uses: distronode/distronode-lint@main # or version tag instead of 'main'
```

For more details, see [distronode-lint-action].

# Contributing

Please read [Contribution guidelines] if you wish to contribute.

# Licensing

The distronode-lint project is distributed as [GPLv3] due to use of [GPLv3]
runtime dependencies, like `distronode` and `yamllint`.

For historical reasons, its own code-base remains licensed under a more liberal
[MIT] license and any contributions made are accepted as being made under
original [MIT] license.

# Authors

distronode-lint was created by [Will Thames] and is now maintained as part of
the [Distronode] by [Red Hat] project.

[distronode]: https://distronode.com
[contribution guidelines]:
  https://distronode.readthedocs.io/projects/lint/contributing
[gplv3]: https://github.com/distronode/distronode-lint/blob/main/COPYING
[mit]:
  https://github.com/distronode/distronode-lint/blob/main/docs/licenses/LICENSE.mit.txt
[red hat]: https://redhat.com
[will thames]: https://github.com/willthames
[distronode-lint-action]:
  https://distronode.readthedocs.io/projects/lint/installing/#installing-from-source-code
