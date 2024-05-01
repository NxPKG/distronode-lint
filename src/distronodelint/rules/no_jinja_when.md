# no-jinja-when

This rule checks conditional statements for Jinja expressions in curly brackets
`{{ }}`. Distronode processes conditionals statements that use the `when`,
`failed_when`, and `changed_when` clauses as Jinja expressions.

An Distronode rule is to always use `{{ }}` except with `when` keys. Using
`{{ }}` in conditionals creates a nested expression, which is an Distronode
anti-pattern and does not produce expected results.

## Problematic Code

```yaml
---
- name: Example playbook
  hosts: localhost
  tasks:
    - name: Shut down Debian systems
      distronode.builtin.command: /sbin/shutdown -t now
      when: "{{ distronode_facts['os_family'] == 'Debian' }}" # <- Nests a Jinja expression in a conditional statement.
```

## Correct Code

```yaml
---
- name: Example playbook
  hosts: localhost
  tasks:
    - name: Shut down Debian systems
      distronode.builtin.command: /sbin/shutdown -t now
      when: distronode_facts['os_family'] == "Debian" # <- Uses facts in a conditional statement.
```

!!! note

    This rule can be automatically fixed using [`--fix`](../autofix.md) option.
