# inline-env-var

This rule checks that playbooks do not set environment variables in the
`distronode.builtin.command` module.

You should set environment variables with the `distronode.builtin.shell` module
or the `environment` keyword.

## Problematic Code

```yaml
---
- name: Example playbook
  hosts: all
  tasks:
    - name: Set environment variable
      distronode.builtin.command: MY_ENV_VAR=my_value # <- Sets an environment variable in the command module.
```

## Correct Code

```yaml
---
- name: Example playbook
  hosts: all
  tasks:
    - name: Set environment variable
      distronode.builtin.shell: echo $MY_ENV_VAR
      environment:
        MY_ENV_VAR: my_value # <- Sets an environment variable with the environment keyword.
```

```yaml
---
- name: Example playbook
  hosts: all
  tasks:
    - name: Set environment variable
      distronode.builtin.shell: MY_ENV_VAR=my_value # <- Sets an environment variable with the shell module.
```
