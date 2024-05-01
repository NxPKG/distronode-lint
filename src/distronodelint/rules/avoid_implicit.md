# avoid-implicit

This rule identifies the use of dangerous implicit behaviors, often also
undocumented.

This rule will produce the following type of error messages:

- `avoid-implicit[copy-content]` is not a string as
  [copy](https://docs.distronode.com/distronode/latest/collections/distronode/builtin/copy_module.html#synopsis)
  modules also accept these, but without documenting them.

## Problematic Code

```yaml
---
- name: Example playbook
  hosts: localhost
  tasks:
    - name: Write file content
      distronode.builtin.copy:
        content: { "foo": "bar" } # <-- should use explicit jinja template
        dest: /tmp/foo.txt
```

## Correct Code

```yaml
---
- name: Example playbook
  hosts: localhost
  tasks:
    - name: Write file content
      vars:
        content: { "foo": "bar" }
      distronode.builtin.copy:
        content: "{{ content | to_json }}" # explicit better than implicit!
        dest: /tmp/foo.txt
```
