from typing import Sequence
from pulumi import ComponentResource, ResourceOptions
from pulumi_gcp import storage

class StorageBucketArgs:
    def __init__(self,
                 name: str,
                 location: str,
                 storage_class: str,
                 lifecycle_rules: Sequence[storage.BucketLifecycleRuleArgs],
                 versioning: storage.BucketVersioningArgs,
                 uniform_bucket_level_access=False,
                 ) -> None:
        self.name = name
        self.location = location
        self.storage_class = storage_class
        self.lifecycle_rules = lifecycle_rules
        self.versioning = versioning
        self.uniform_bucket_level_access = uniform_bucket_level_access

class StorageBucketAclArgs:
    def __init__(self,
                 bucket: storage.Bucket,
                 role_entity: Sequence[str],
                 ) -> None:
        self.bucket = bucket
        self.role_entity = role_entity

# https://www.pulumi.com/registry/packages/gcp/api-docs/storage/bucket/
class StorageBucket(ComponentResource):
    def __init__(self, 
                 name: str, 
                 label: str,
                 args: StorageBucketArgs, 
                 opts: ResourceOptions = None):
        super().__init__(label, name, {}, opts)

        self.storage = storage.Bucket(
            resource_name=name,
            location=args.location,
            storage_class=args.storage_class,
            lifecycle_rules=args.lifecycle_rules,
            versioning=args.versioning,
            uniform_bucket_level_access=args.uniform_bucket_level_access,
            opts=ResourceOptions(parent=self))
        self.register_outputs({})

# https://www.pulumi.com/registry/packages/gcp/api-docs/storage/bucketacl/
class StorageBucketAcl(ComponentResource):
    def __init__(self, 
                 name: str, 
                 label: str,
                 args: StorageBucketAclArgs, 
                 opts: ResourceOptions = None):
        super().__init__(label, name, {}, opts)

        self.storage_bucket_acl = storage.BucketACL(
            resource_name=name,
            bucket=args.bucket.name,
            role_entities=args.role_entity,
            opts=ResourceOptions(parent=self))
        self.register_outputs({})