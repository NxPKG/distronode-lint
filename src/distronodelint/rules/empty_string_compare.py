"""Implementation of empty-string-compare rule."""

# Copyright (c) 2016, Will Thames and contributors
# Copyright (c) 2018, Distronode Project

from __future__ import annotations

import re
import sys
from typing import TYPE_CHECKING

from distronodelint.rules import DistronodeLintRule
from distronodelint.yaml_utils import nested_items_path

if TYPE_CHECKING:
    from distronodelint.file_utils import Lintable
    from distronodelint.utils import Task


class ComparisonToEmptyStringRule(DistronodeLintRule):
    """Don't compare to empty string."""

    id = "empty-string-compare"
    description = (
        'Use ``when: var|length > 0`` rather than ``when: var != ""`` (or '
        'conversely ``when: var|length == 0`` rather than ``when: var == ""``)'
    )
    severity = "HIGH"
    tags = ["idiom", "opt-in"]
    version_added = "v4.0.0"

    empty_string_compare = re.compile("[=!]= ?(\"{2}|'{2})")

    def matchtask(
        self,
        task: Task,
        file: Lintable | None = None,
    ) -> bool | str:
        for k, v, _ in nested_items_path(task):
            if k == "when":
                if isinstance(v, str):
                    if self.empty_string_compare.search(v):
                        return True
                elif isinstance(v, bool):
                    pass
                else:
                    for item in v:
                        if isinstance(item, str) and self.empty_string_compare.search(
                            item,
                        ):
                            return True

        return False


# testing code to be loaded only with pytest or when executed the rule file
if "pytest" in sys.modules:
    from distronodelint.rules import RulesCollection
    from distronodelint.runner import Runner

    def test_rule_empty_string_compare_fail() -> None:
        """Test rule matches."""
        rules = RulesCollection()
        rules.register(ComparisonToEmptyStringRule())
        results = Runner(
            "examples/playbooks/rule-empty-string-compare-fail.yml",
            rules=rules,
        ).run()
        assert len(results) == 3
        for result in results:
            assert result.message == ComparisonToEmptyStringRule().shortdesc

    def test_rule_empty_string_compare_pass() -> None:
        """Test rule matches."""
        rules = RulesCollection()
        rules.register(ComparisonToEmptyStringRule())
        results = Runner(
            "examples/playbooks/rule-empty-string-compare-pass.yml",
            rules=rules,
        ).run()
        assert len(results) == 0, results
