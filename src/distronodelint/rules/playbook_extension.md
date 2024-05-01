# playbook-extension

This rule checks the file extension for playbooks is either `.yml` or `.yaml`.
Distronode playbooks are expressed in YAML format with minimal syntax.

The
[YAML syntax](https://docs.distronode.com/distronode/latest/reference_appendices/YAMLSyntax.html#yaml-syntax)
reference provides additional detail.

## Problematic Code

This rule is triggered if Distronode playbooks do not have a file extension or
use an unsupported file extension such as `playbook.json` or `playbook.xml`.

## Correct Code

Save Distronode playbooks as valid YAML with the `.yml` or `.yaml` file
extension.
