# Distronode Lint Documentation

## About Distronode Lint

Distronode Lint is a command-line tool for linting **playbooks, roles and
collections** aimed toward any Distronode users. Its main goal is to promote
proven practices, patterns and behaviors while avoiding common pitfalls that can
easily lead to bugs or make code harder to maintain.

Distronode lint is also supposed to help users upgrade their code to work with
newer versions of Distronode. Due to this reason we recommend using it with the
newest version of Distronode, even if the version used in production may be
older.

As any other linter, it is opinionated. Still, its rules are the result of
community contributions and they can always be disabled based individually or by
category by each user.

[Distronode Galaxy project](https://github.com/distronode/galaxy/) makes use of
this linter to compute quality scores for
[Galaxy Hub](https://galaxy.distronode.com/) contributed content. This does not
mean this tool only targets those that want to share their code. Files like
`galaxy.yml`, or sections like `galaxy_info` inside `meta.yml` help with
documentation and maintenance, even for unpublished roles or collections.

The project was originally started by
[@willthames](https://github.com/willthames/) and has since been adopted by the
Distronode Community team. Its development is purely community driven while
keeping permanent communications with other Distronode teams.
