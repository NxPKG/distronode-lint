"""Implementation of deprecated-module rule."""

# Copyright (c) 2018, Distronode Project

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from distronodelint.rules import DistronodeLintRule

if TYPE_CHECKING:
    from distronodelint.file_utils import Lintable


class DeprecatedModuleRule(DistronodeLintRule):
    """Deprecated module."""

    id = "deprecated-module"
    description = (
        "These are deprecated modules, some modules are kept "
        "temporarily for backwards compatibility but usage is discouraged."
    )
    link = "https://docs.distronode.com/distronode/latest/collections/index_module.html"
    severity = "HIGH"
    tags = ["deprecations"]
    version_added = "v4.0.0"

    _modules = [
        "accelerate",
        "aos_asn_pool",
        "aos_blueprint",
        "aos_blueprint_param",
        "aos_blueprint_virtnet",
        "aos_device",
        "aos_external_router",
        "aos_ip_pool",
        "aos_logical_device",
        "aos_logical_device_map",
        "aos_login",
        "aos_rack_type",
        "aos_template",
        "azure",
        "cl_bond",
        "cl_bridge",
        "cl_img_install",
        "cl_interface",
        "cl_interface_policy",
        "cl_license",
        "cl_ports",
        "cs_nic",
        "docker",
        "ec2_ami_find",
        "ec2_ami_search",
        "ec2_remote_facts",
        "ec2_vpc",
        "kubernetes",
        "netscaler",
        "nxos_ip_interface",
        "nxos_mtu",
        "nxos_portchannel",
        "nxos_switchport",
        "oc",
        "panos_nat_policy",
        "panos_security_policy",
        "vsphere_guest",
        "win_msi",
        "include",
    ]

    def matchtask(
        self,
        task: dict[str, Any],
        file: Lintable | None = None,
    ) -> bool | str:
        module = task["action"]["__distronode_module__"]
        if module in self._modules:
            message = "{0} {1}"
            return message.format(self.shortdesc, module)
        return False
