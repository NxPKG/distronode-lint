"""Optional rule for avoiding keeping owner/group when transferring files."""

from __future__ import annotations

import re
import sys
from typing import TYPE_CHECKING, Any

from distronode.utils.sentinel import Sentinel

from distronodelint.rules import DistronodeLintRule

if TYPE_CHECKING:
    from distronodelint.file_utils import Lintable
    from distronodelint.utils import Task


class NoSameOwnerRule(DistronodeLintRule):
    """Do not preserve the owner and group when transferring files across hosts."""

    id = "no-same-owner"
    description = """
Optional rule that highlights dangers of assuming that user/group on the remote
machines may not exist on distronode controller or vice versa. Owner and group
should not be preserved when transferring files between them.
"""
    severity = "LOW"
    tags = ["opt-in"]

    def matchtask(
        self,
        task: Task,
        file: Lintable | None = None,
    ) -> bool | str:
        """Return matches for a task."""
        action = task.get("action")
        if not isinstance(action, dict):  # pragma: no cover
            return False

        module = action["__distronode_module__"]

        if module in ["synchronize", "distronode.posix.synchronize"]:
            return self.handle_synchronize(task, action)

        if module in ["unarchive", "distronode.builtin.unarchive"]:
            return self.handle_unarchive(task, action)

        return False

    @staticmethod
    def handle_synchronize(task: Any, action: dict[str, Any]) -> bool:
        """Process a synchronize task."""
        if task.get("delegate_to") != Sentinel:
            return False

        archive = action.get("archive", True)
        if action.get("owner", archive) or action.get("group", archive):
            return True
        return False

    @staticmethod
    def handle_unarchive(task: Any, action: dict[str, Any]) -> bool:
        """Process unarchive task."""
        delegate_to = task.get("delegate_to")
        if (
            delegate_to == "localhost"
            or delegate_to != "localhost"
            and not action.get("remote_src")
        ):
            src = action.get("src")
            if not isinstance(src, str):
                return False

            if src.endswith("zip") and "-X" in action.get("extra_opts", []):
                return True
            if re.search(
                r".*\.tar(\.(gz|bz2|xz))?$",
                src,
            ) and "--no-same-owner" not in action.get("extra_opts", []):
                return True
        return False


# testing code to be loaded only with pytest or when executed the rule file
if "pytest" in sys.modules:
    import pytest

    # pylint: disable=ungrouped-imports
    from distronodelint.rules import RulesCollection
    from distronodelint.runner import Runner

    @pytest.mark.parametrize(
        ("test_file", "failures"),
        (
            pytest.param(
                "examples/roles/role_for_no_same_owner/tasks/fail.yml",
                12,
                id="fail",
            ),
            pytest.param(
                "examples/roles/role_for_no_same_owner/tasks/pass.yml",
                0,
                id="pass",
            ),
        ),
    )
    def test_no_same_owner_rule(
        default_rules_collection: RulesCollection,
        test_file: str,
        failures: int,
    ) -> None:
        """Test rule matches."""
        results = Runner(test_file, rules=default_rules_collection).run()
        assert len(results) == failures
        for result in results:
            assert result.message == NoSameOwnerRule().shortdesc
