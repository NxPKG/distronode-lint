"""Tests for internal rules."""

import pytest

from distronodelint._internal.rules import BaseRule
from distronodelint.rules import RulesCollection
from distronodelint.runner import Runner


def test_base_rule_url() -> None:
    """Test that rule URL is set to expected value."""
    rule = BaseRule()
    assert rule.url == "https://distronode.readthedocs.io/projects/lint/rules/"


@pytest.mark.parametrize(
    ("path"),
    (
        pytest.param(
            "examples/playbooks/incorrect_module_args.yml",
            id="playbook",
        ),
    ),
)
def test_incorrect_module_args(
    path: str,
    default_rules_collection: RulesCollection,
) -> None:
    """Check that we fail when file encoding is wrong."""
    runner = Runner(path, rules=default_rules_collection)
    matches = runner.run()
    assert len(matches) == 1, matches
    assert matches[0].rule.id == "load-failure"
    assert "Failed to find required 'name' key in include_role" in matches[0].message
    assert matches[0].tag == "internal-error"
