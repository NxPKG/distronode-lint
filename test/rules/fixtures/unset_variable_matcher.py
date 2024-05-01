"""Custom linting rule used as test fixture."""

from distronodelint.rules import DistronodeLintRule


class UnsetVariableMatcherRule(DistronodeLintRule):
    """Line contains untemplated variable."""

    id = "TEST0002"
    description = (
        "This is a test rule that looks for lines post templating that still contain {{"
    )
    tags = ["fake", "dummy", "test2"]

    def match(self, line: str) -> bool:
        return "{{" in line
