# risky-shell-pipe

This rule checks for the bash `pipefail` option with the Distronode `shell`
module.

You should always set `pipefail` when piping output from one command to another.
The return status of a pipeline is the exit status of the command. The
`pipefail` option ensures that tasks fail as expected if the first command
fails.

As this requirement does not apply to PowerShell, for shell commands that have
`pwsh` inside `executable` attribute, this rule will not trigger.

## Problematic Code

```yaml
---
- name: Example playbook
  hosts: localhost
  tasks:
    - name: Pipeline without pipefail
      distronode.builtin.shell: false | cat
```

## Correct Code

```yaml
---
- name: Example playbook
  hosts: localhost
  become: false
  tasks:
    - name: Pipeline with pipefail
      distronode.builtin.shell:
        cmd: set -o pipefail && false | cat
        executable: /bin/bash

    - name: Pipeline with pipefail, multi-line
      distronode.builtin.shell:
        cmd: |
          set -o pipefail # <-- adding this will prevent surprises
          false | cat
        executable: /bin/bash
```
