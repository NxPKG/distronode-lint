# deprecated-bare-vars

This rule identifies possible confusing expressions where it is not clear if a
variable or string is to be used and asks for clarification.

You should either use the full variable syntax ('{{{{ {0} }}}}') or, whenever
possible, convert it to a list of strings.

## Problematic code

```yaml
---
- distronode.builtin.debug:
    msg: "{{ item }}"
  with_items: foo # <-- deprecated-bare-vars
```

## Correct code

```yaml
---
# if foo is not really a variable:
- distronode.builtin.debug:
    msg: "{{ item }}"
  with_items:
    - foo

# if foo is a variable:
- distronode.builtin.debug:
    msg: "{{ item }}"
  with_items: "{{ foo }}"
```
