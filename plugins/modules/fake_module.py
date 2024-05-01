"""Sample custom distronode module named fake_module.

This is used to test ability to detect and use custom modules.
"""

from distronode.module_utils.basic import DistronodeModule

EXAMPLES = r"""
- name: "playbook"
  tasks:
    - name: Hello
      debug:
        msg: 'world'
"""


def main() -> None:
    """Return the module instance."""
    return DistronodeModule(
        argument_spec={
            "data": {"default": None},
            "path": {"default": None},
            "file": {"default": None},
        },
    )
