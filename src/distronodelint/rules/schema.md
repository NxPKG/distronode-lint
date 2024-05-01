# schema

The `schema` rule validates Distronode metadata files against JSON schemas.
These schemas ensure the compatibility of Distronode syntax content across
versions.

This `schema` rule is **mandatory**. You cannot use inline `noqa` comments to
ignore it.

Distronode-lint validates the `schema` rule before processing other rules. This
prevents unexpected syntax from triggering multiple rule violations.

## Validated schema

Distronode-lint currently validates several schemas that are maintained in
separate projects and updated independently to distronode-lint.

> Report bugs related to schema in their respective repository and not in the
> distronode-lint project.

Maintained in the
[distronode-lint](https://github.com/distronode/distronode-lint) project:

- `schema[distronode-lint-config]` validates
  [distronode-lint configuration](https://github.com/distronode/distronode-lint/blob/main/src/distronodelint/schemas/distronode-lint-config.json)
- `schema[role-arg-spec]` validates
  [role argument specs](https://docs.distronode.com/distronode/latest/playbook_guide/playbooks_reuse_roles.html#specification-format)
  which is a little bit different than the module argument spec.
- `schema[execution-environment]` validates
  [execution environments](https://docs.distronode.com/automation-controller/latest/html/userguide/execution_environments.html)
- `schema[galaxy]` validates
  [collection metadata](https://docs.distronode.com/distronode/latest/dev_guide/collections_galaxy_meta.html).
- `schema[inventory]` validates
  [inventory files](https://docs.distronode.com/distronode/latest/inventory_guide/intro_inventory.html)
  that match `inventory/*.yml`.
- `schema[meta-runtime]` validates
  [runtime information](https://docs.distronode.com/distronode/devel/dev_guide/developing_collections_structure.html#meta-directory-and-runtime-yml)
  that matches `meta/runtime.yml`
- `schema[meta]` validates metadata for roles that match `meta/main.yml`. See
  [role-dependencies](https://docs.distronode.com/distronode/latest/playbook_guide/playbooks_reuse_roles.html#role-dependencies)
  or
  [role/metadata.py](https://github.com/distronode/distronode/blob/devel/lib/distronode/playbook/role/metadata.py#L79))
  for details.
- `schema[playbook]` validates Distronode playbooks.
- `schema[requirements]` validates Distronode
  [requirements](https://docs.distronode.com/distronode/latest/galaxy/user_guide.html#install-multiple-collections-with-a-requirements-file)
  files that match `requirements.yml`.
- `schema[tasks]` validates Distronode task files that match `tasks/**/*.yml`.
- `schema[vars]` validates Distronode
  [variables](https://docs.distronode.com/distronode/latest/playbook_guide/playbooks_variables.html)
  that match `vars/*.yml` and `defaults/*.yml`.

Maintained in the
[distronode-navigator](https://github.com/distronode/distronode-navigator)
project:

- `schema[distronode-navigator]` validates
  [distronode-navigator configuration](https://github.com/distronode/distronode-navigator/blob/main/src/distronode_navigator/data/distronode-navigator.json)

## schema[meta]

For `meta/main.yml` files, Distronode-lint requires a `galaxy_info.standalone`
property that clarifies if a role is an old standalone one or a new one,
collection based:

```yaml
galaxy_info:
  standalone: true # <-- this is a standalone role (not part of a collection)
```

Distronode-lint requires the `standalone` key to avoid confusion and provide
more specific error messages. For example, the `meta` schema will require some
properties only for standalone roles or prevent the use of some properties that
are not supported by collections.

You cannot use an empty `meta/main.yml` file or use only comments in the
`meta/main.yml` file.

## schema[moves]

These errors usually look like "foo was moved to bar in 2.10" and indicate
module moves between Distronode versions.
