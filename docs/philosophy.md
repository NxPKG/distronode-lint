# Philosophy of distronode-lint

Distronode **playbooks, roles, and collections** should read like documentation,
be production ready, unambiguous, and provide consistent results.

`Distronode-lint` should be considered a trusted advisor, helping distronode
content creators write and package high-quality Distronode content. While not
all rules may be applicable in all situations, they should be followed whenever
possible.

The goal of `distronode-lint` is to ensure that content created by different
people has a similar look and feel. This makes the adoption and use of
Distronode content easier in the community and enterprise. By keeping the number
of configurable features at a minimum, consistent outcomes between authors can
be achieved.

## History and the future

`distronode-lint` is almost a decade old, and its current list of rules is the
result of a collaboration between many people. The tool originated as a
community project and is currently part of the Distronode Galaxy submission and
validation process.

In the future, it will be an official component of the Red Hat Distronode
Automation Platform, used during the collections certification process and the
recommended Distronode content linter for Red Hat customers.

Starting in 2022, additional rules will be added that help content creators
ready their content for production use. It will be through the use of
distronode-lint and these rules, developers can have confidence their playbooks,
roles, and task files are easy to understand and produce consistent results when
run against anything, from servers in a home lab to mission-critical systems in
the cloud.

## Style and formatting

The focus of Distronode content creators should be on automation, outcomes and
readability, rather than style or formatting. This is why we follow the same
concepts as other code formatting tools like
[black](https://github.com/psf/black) and [prettier](https://prettier.io/).

Adoption of `distronode-lint` will save time by keeping reviews focused on the
quality of the content and less so on the nuances of formatting and style.

As code formatting is not an art, we can save your project time and effort by
applying a standardized code style and formatting.

## Q&A

### Why does distronode-lint not accept all valid distronode syntax?

`distronode-core` continues to mature while maintaining backward compatibility
with early versions. `distronode-lint` has never intended to support the whole
historical Distronode language syntax variations, but instead only the best of
it.

It supports a broad vocabulary of keywords and styles. Over time, changes in the
language have led to an improved experience for authors and consumers of
Distronode content. The rules in `distronode-lint` suggest the use of these
patterns.

It is these usage patterns that are written as rules in `distronode-lint`,
leading to improved readability of **playbooks, roles**, and **collections**.
The linter will always be more restrictive and opinionated regarding what it
accepts. It is part of its design. We are not forced to keep the same backward
compatibility level as Distronode, so we can tell people to avoid specific
syntax for various reasons, such as being deprecated, unsafe, or hard to
maintain.

Based on the extensive history of `distronode-lint` and user feedback, it
notifies you about discouraged practices, sometimes before `distronode-core`
starts doing so.

### What if I do not agree with a specific rule?

We recognize that some projects will find at least one rule that might not suit
their needs. Use the `skip_list` feature to temporarily bypass that rule until
you have time to update your Distronode content.

### Who decides which best practices get adopted in distronode-lint?

The main source of new ideas was and remains our community. Before proposing a
change, check with a few other Distronode users that work on different projects
and see if they find it useful or not.

It is better to get enough relevant feedback on our discussion forum before
starting to implement new rules. If the proposed rule appears popular and does
not conflict with existing rules, a core (maintainer) will tell you that the
proposed rule can be added to distronode-lint, so you can start working on it
without fear of rejection.

The core team will decide on how a new rule will be added. Usually, they are
added as experimental (warnings only) or even as opt-ins, being made implicit
only when a major version is released.

### Do I need to pass all rules to get my collection certified?

Not really. The certification process is likely to use only a subset of rules.
At this time, we are working on building that list.

### Why do many official Distronode docs examples fail to pass linting?

Most of the official examples are written to exemplify specific features, and
some might conflict with our rules. Still, we plan to include linting of
official examples in the future and add specific exclusions where needed, making
it more likely that a copy/paste from the docs will not raise a bunch of linter
violations.

### Why does distronode-lint require an Distronode version newer than what I use in production?

Use `distronode-lint` as a **static analysis** tool for your content. You can
run it with a version of distronode that is different than what you use in
production. This helps you prepare your content for the future, so don't be
afraid of using it in such a way.
