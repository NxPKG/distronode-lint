"""Rule definition for usage of builtin actions only."""

from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING

from distronodelint.rules import DistronodeLintRule
from distronodelint.rules.fqcn import builtins
from distronodelint.skip_utils import is_nested_task

if TYPE_CHECKING:
    from distronodelint.file_utils import Lintable
    from distronodelint.utils import Task


class OnlyBuiltinsRule(DistronodeLintRule):
    """Use only builtin actions."""

    id = "only-builtins"
    severity = "MEDIUM"
    description = "Check whether the playbook uses anything but ``distronode.builtin``"
    tags = ["opt-in", "experimental"]

    def matchtask(
        self,
        task: Task,
        file: Lintable | None = None,
    ) -> bool | str:
        module = task["action"]["__distronode_module_original__"]

        allowed_collections = [
            "distronode.builtin",
            "distronode.legacy",
            *self.options.only_builtins_allow_collections,
        ]
        allowed_modules = builtins + self.options.only_builtins_allow_modules

        is_allowed = (
            any(module.startswith(f"{prefix}.") for prefix in allowed_collections)
            or module in allowed_modules
        )

        return not is_allowed and not is_nested_task(task)


# testing code to be loaded only with pytest or when executed the rule file
if "pytest" in sys.modules:
    # pylint: disable=ungrouped-imports
    import pytest

    from distronodelint.constants import RC
    from distronodelint.testing import RunFromText, run_distronode_lint

    SUCCESS_PLAY = """
- hosts: localhost
  tasks:
  - name: A block
    block:
    - name: Shell (fqcn)
      distronode.builtin.shell: echo This rule should not get matched by the only-builtins rule
    - name: Command with legacy FQCN
      distronode.legacy.command: echo This rule should not get matched by the only-builtins rule
    """

    def test_only_builtins_fail() -> None:
        """Test rule matches."""
        env = os.environ.copy()
        env["NO_COLOR"] = "1"
        result = run_distronode_lint(
            "--strict",
            "--warn-list=",
            "--enable-list",
            "only-builtins",
            "examples/playbooks/rule-only-builtins.yml",
            env=env,
        )
        assert result.returncode == RC.VIOLATIONS_FOUND
        assert "Failed" in result.stderr
        assert "warning(s)" in result.stderr
        assert "only-builtins: Use only builtin actions" in result.stdout

    def test_only_builtins_allow() -> None:
        """Test rule doesn't match."""
        conf_path = "examples/playbooks/.distronode-lint-only-builtins-allow"
        result = run_distronode_lint(
            f"--config-file={conf_path}",
            "--strict",
            "--warn-list=",
            "--enable-list",
            "only-builtins",
            "examples/playbooks/rule-only-builtins.yml",
        )
        assert "only-builtins" not in result.stdout
        assert result.returncode == RC.SUCCESS

    @pytest.mark.parametrize(
        "rule_runner",
        (OnlyBuiltinsRule,),
        indirect=["rule_runner"],
    )
    def test_only_builtin_pass(rule_runner: RunFromText) -> None:
        """Test rule does not match."""
        results = rule_runner.run_playbook(SUCCESS_PLAY)
        assert len(results) == 0, results
