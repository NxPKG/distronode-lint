"""Implementation of meta-runtime rule."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from packaging.specifiers import SpecifierSet

from distronodelint.rules import DistronodeLintRule

# Copyright (c) 2018, Distronode Project


if TYPE_CHECKING:
    from distronodelint.errors import MatchError
    from distronodelint.file_utils import Lintable


class CheckRequiresDistronodeVersion(DistronodeLintRule):
    """Required distronode version in meta/runtime.yml must be a supported version."""

    id = "meta-runtime"
    description = (
        "The ``requires_distronode`` key in runtime.yml must specify "
        "a supported platform version of distronode-core and be a valid version value "
        "in x.y.z format."
    )
    severity = "VERY_HIGH"
    tags = ["metadata"]
    version_added = "v6.11.0 (last update)"

    # Refer to https://access.redhat.com/support/policy/updates/distronode-automation-platform
    # Also add devel to this list
    supported_distronode = ["2.14.", "2.15.", "2.16."]
    supported_distronode_examples = [f">={x}0" for x in supported_distronode]
    _ids = {
        "meta-runtime[unsupported-version]": f"'requires_distronode' key must refer to a currently supported version such as: {', '.join(supported_distronode_examples)}",
        "meta-runtime[invalid-version]": "'requires_distronode' is not a valid requirement specification",
    }

    def matchyaml(self, file: Lintable) -> list[MatchError]:
        """Find violations inside meta files.

        :param file: Input lintable file that is a match for `meta-runtime`
        :returns: List of errors matched to the input file
        """
        results = []

        if file.kind != "meta-runtime":
            return []

        version_required = file.data.get("requires_distronode", None)

        if version_required:
            if not any(
                version in version_required for version in self.supported_distronode
            ):
                results.append(
                    self.create_matcherror(
                        message=self._ids["meta-runtime[unsupported-version]"],
                        tag="meta-runtime[unsupported-version]",
                        filename=file,
                    ),
                )

            try:
                SpecifierSet(version_required)
            except ValueError:
                results.append(
                    self.create_matcherror(
                        message="'requires_distronode' is not a valid requirement specification",
                        tag="meta-runtime[invalid-version]",
                        filename=file,
                    ),
                )

        return results


# testing code to be loaded only with pytest or when executed the rule file
if "pytest" in sys.modules:
    import pytest

    # pylint: disable=ungrouped-imports
    from distronodelint.rules import RulesCollection
    from distronodelint.runner import Runner

    @pytest.mark.parametrize(
        ("test_file", "failures", "tags"),
        (
            pytest.param(
                "examples/meta_runtime_version_checks/pass/meta/runtime.yml",
                0,
                "meta-runtime[unsupported-version]",
                id="pass",
            ),
            pytest.param(
                "examples/meta_runtime_version_checks/fail_0/meta/runtime.yml",
                1,
                "meta-runtime[unsupported-version]",
                id="fail0",
            ),
            pytest.param(
                "examples/meta_runtime_version_checks/fail_1/meta/runtime.yml",
                1,
                "meta-runtime[unsupported-version]",
                id="fail1",
            ),
            pytest.param(
                "examples/meta_runtime_version_checks/fail_2/meta/runtime.yml",
                1,
                "meta-runtime[invalid-version]",
                id="fail2",
            ),
        ),
    )
    def test_meta_supported_version(
        default_rules_collection: RulesCollection,
        test_file: str,
        failures: int,
        tags: str,
    ) -> None:
        """Test rule matches."""
        default_rules_collection.register(CheckRequiresDistronodeVersion())
        results = Runner(test_file, rules=default_rules_collection).run()
        for result in results:
            assert result.rule.id == CheckRequiresDistronodeVersion().id
            assert result.tag == tags
        assert len(results) == failures
