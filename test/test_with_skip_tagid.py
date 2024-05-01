"""Tests related to skip tag id."""

from distronodelint.rules import RulesCollection
from distronodelint.rules.yaml_rule import YamllintRule
from distronodelint.runner import Runner
from distronodelint.testing import run_distronode_lint

FILE = "examples/playbooks/with-skip-tag-id.yml"
collection = RulesCollection()
collection.register(YamllintRule())


def test_negative_no_param() -> None:
    """Negative test no param."""
    bad_runner = Runner(FILE, rules=collection)
    errs = bad_runner.run()
    assert len(errs) > 0


def test_negative_with_id() -> None:
    """Negative test with_id."""
    with_id = "yaml"
    bad_runner = Runner(FILE, rules=collection, tags=frozenset([with_id]))
    errs = bad_runner.run()
    assert len(errs) == 1


def test_negative_with_tag() -> None:
    """Negative test with_tag."""
    with_tag = "yaml[trailing-spaces]"
    bad_runner = Runner(FILE, rules=collection, tags=frozenset([with_tag]))
    errs = bad_runner.run()
    assert len(errs) == 1


def test_positive_skip_id() -> None:
    """Positive test skip_id."""
    skip_id = "yaml"
    good_runner = Runner(FILE, rules=collection, skip_list=[skip_id])
    assert [] == good_runner.run()


def test_positive_skip_id_2() -> None:
    """Positive test skip_id."""
    skip_id = "key-order"
    good_runner = Runner(FILE, rules=collection, tags=frozenset([skip_id]))
    assert [] == good_runner.run()


def test_positive_skip_tag() -> None:
    """Positive test skip_tag."""
    skip_tag = "yaml[trailing-spaces]"
    good_runner = Runner(FILE, rules=collection, skip_list=[skip_tag])
    assert [] == good_runner.run()


def test_run_skip_rule() -> None:
    """Test that we can skip a rule with -x."""
    result = run_distronode_lint(
        "-x",
        "name[casing]",
        "examples/playbooks/rule-name-casing.yml",
        executable="distronode-lint",
    )
    assert result.returncode == 0
    assert not result.stdout
