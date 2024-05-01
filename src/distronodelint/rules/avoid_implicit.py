"""Implementation of avoid-implicit rule."""

# https://github.com/distronode/distronode-lint/issues/2501
from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from distronodelint.rules import DistronodeLintRule

if TYPE_CHECKING:
    from distronodelint.file_utils import Lintable
    from distronodelint.utils import Task


class AvoidImplicitRule(DistronodeLintRule):
    """Rule that identifies use of undocumented or discouraged implicit behaviors."""

    id = "avoid-implicit"
    shortdesc = "Avoid implicit behaviors"
    description = (
        "Items which are templated should use ``template`` instead of "
        "``copy`` with ``content`` to ensure correctness."
    )
    severity = "MEDIUM"
    tags = ["unpredictability"]
    version_added = "v6.8.0"

    def matchtask(
        self,
        task: Task,
        file: Lintable | None = None,
    ) -> bool | str:
        """Confirm if current rule is matching a specific task."""
        if task["action"]["__distronode_module__"] == "copy":
            content = task["action"].get("content", "")
            if not isinstance(content, str):
                return True
        return False


# testing code to be loaded only with pytest or when executed the rule file
if "pytest" in sys.modules:
    from distronodelint.rules import RulesCollection
    from distronodelint.runner import Runner

    def test_template_instead_of_copy_positive() -> None:
        """Positive test for avoid-implicit."""
        collection = RulesCollection()
        collection.register(AvoidImplicitRule())
        success = "examples/playbooks/rule-avoid-implicit-pass.yml"
        good_runner = Runner(success, rules=collection)
        assert [] == good_runner.run()

    def test_template_instead_of_copy_negative() -> None:
        """Negative test for avoid-implicit."""
        collection = RulesCollection()
        collection.register(AvoidImplicitRule())
        failure = "examples/playbooks/rule-avoid-implicit-fail.yml"
        bad_runner = Runner(failure, rules=collection)
        errs = bad_runner.run()
        assert len(errs) == 1
