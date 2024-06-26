from typing import Sequence
from pulumi import ComponentResource, ResourceOptions
from pulumi_gcp import compute

class FirewallArgs:
    def __init__(self,
                 name: str,
                 network: compute.Network,
                 source_ranges: Sequence[str],
                 allows: Sequence[compute.FirewallAllowArgs],
                 target_tags: Sequence[str]=None,
                 depends_on=None
                 ):
        self.name = name
        self.network = network
        self.source_ranges = source_ranges
        self.allows = allows
        self.target_tags = target_tags
        self.depends_on = depends_on

# https://www.pulumi.com/registry/packages/gcp/api-docs/compute/firewall/
class Firewall(ComponentResource):
    def __init__(self, 
                 name: str, 
                 label: str,
                 args: FirewallArgs, 
                 opts: ResourceOptions = None):
        super().__init__(label, name, {}, opts)

        self.firewall = compute.Firewall(
            resource_name=name,
            network=args.network.id,
            source_ranges=args.source_ranges,
            allows=args.allows,
            target_tags=args.target_tags,
            opts=ResourceOptions(parent=self, depends_on=args.depends_on))
        self.register_outputs({})