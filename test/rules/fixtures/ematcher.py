"""Custom rule used as fixture."""

from distronodelint.rules import DistronodeLintRule


class EMatcherRule(DistronodeLintRule):
    """BANNED string found."""

    id = "TEST0001"
    description = (
        "This is a test custom rule that looks for lines containing BANNED string"
    )
    tags = ["fake", "dummy", "test1"]

    def match(self, line: str) -> bool:
        return "BANNED" in line
