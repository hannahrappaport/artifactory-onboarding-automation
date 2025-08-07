import json
from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field

# Base repository configuration
class BaseRepoConfig(BaseModel):
    key: str
    project_key: Optional[str] = None
    description: str = ""
    notes: str = ""
    includes_pattern: str = "**/*"
    excludes_pattern: str = ""
    priority_resolution: bool = False
    project_environments: List[str] = Field(default_factory=list)
    blacked_out: bool = False
    property_sets: Optional[List[str]] = Field(default_factory=list)
    archive_browsing_enabled: bool = False
    download_direct: bool = False
    cdn_redirect: bool = False
    x_ray_index: bool = False

# Alpine repository
class AlpineRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "simple-default"
    primary_key_pair_ref: Optional[str] = None

# RPM repository
class RpmRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "simple-default"
    primary_key_pair_ref: Optional[str] = None
    secondary_key_pair_ref: Optional[str] = None
    yum_root_depth: int = 0
    yum_group_file_names: Optional[str] = None
    enable_file_lists_indexing: bool = False
    calculate_yum_metadata: bool = False

# Debian repository
class DebianRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "simple-default"
    primary_key_pair_ref: Optional[str] = None
    secondary_key_pair_ref: Optional[str] = None
    optional_index_compression_formats: List[str] = Field(default_factory=lambda: ["bz2"])
    trivial_layout: bool = False

# Docker repository
class DockerRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "simple-default"
    block_pushing_schema1: bool = False
    max_unique_tags: int = 0
    docker_tag_retention: int = 1

# Generic repository
class GenericRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "simple-default"

# Maven repository
class MavenRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "maven-2-default"
    checksum_policy_type: str = "client-checksums"
    snapshot_version_behavior: str = "unique"
    max_unique_snapshots: int = 0
    handle_releases: bool = True
    handle_snapshots: bool = True
    suppress_pom_consistency_checks: bool = False

# NPM repository
class NpmRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "npm-default"

# NuGet repository
class NugetRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "nuget-default"
    max_unique_snapshots: int = 0
    force_nuget_authentication: bool = False

# PyPI repository
class PypiRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "simple-default"

# Helm repository
class HelmRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "simple-default"
    force_non_duplicate_chart: bool = False
    force_metadata_name_version: bool = False

# CRAN repository
class CranRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "simple-default"

# Composer repository
class ComposerRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "composer-default"

# Gems repository
class GemsRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "simple-default"

# Go repository
class GoRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "go-default"

# Ivy repository
class IvyRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "ivy-default"

# Chef repository
class ChefRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "simple-default"

# Cocoapods repository
class CocoapodsRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "simple-default"

# Terraform Module repository
class TerraformModuleRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "terraform-module-default"

# Terraform Provider repository
class TerraformProviderRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "terraform-provider-default"

# Gradle repository
class GradleRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "gradle-default"
    checksum_policy_type: str = "client-checksums"
    snapshot_version_behavior: str = "unique"
    max_unique_snapshots: int = 0
    handle_releases: bool = True
    handle_snapshots: bool = True
    suppress_pom_consistency_checks: bool = True

# Helm OCI repository
class HelmochiRepoConfig(BaseRepoConfig):
    repo_layout_ref: str = "simple-default"
    docker_tag_retention: int = 1
    max_unique_tags: int = 0

# Virtual repository base
class BaseVirtualRepoConfig(BaseModel):
    key: str
    repositories: List[str] = Field(default_factory=list)
    description: str = ""
    notes: str = ""
    project_key: Optional[str] = None
    project_environments: List[str] = Field(default_factory=list)
    includes_pattern: str = "**/*"
    excludes_pattern: str = ""
    artifactory_requests_can_retrieve_remote_artifacts: bool = False
    default_deployment_repo: Optional[str] = None
    allow_delete: bool = True

# Virtual repository configurations
class ChefVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "simple-default"
    retrieval_cache_period_seconds: int = 7200

class CranVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "simple-default"
    retrieval_cache_period_seconds: int = 7200

class DebianVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "simple-default"
    retrieval_cache_period_seconds: int = 7200
    primary_keypair_ref: Optional[str] = None
    secondary_keypair_ref: Optional[str] = None
    optional_index_compression_formats: List[str] = Field(default_factory=lambda: ["bz2"])
    debian_default_architectures: Optional[str] = None

class DockerVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "simple-default"
    resolve_docker_tags_by_timestamp: bool = False

class GemsVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "simple-default"

class GenericVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "simple-default"

class GoVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "go-default"
    external_dependencies_enabled: bool = False
    external_dependencies_patterns: List[str] = Field(default_factory=list)

class GradleVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "gradle-default"
    pom_repository_references_cleanup_policy: Optional[str] = None
    key_pair: Optional[str] = None

class HelmVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "simple-default"
    retrieval_cache_period_seconds: int = 7200
    use_namespaces: bool = False

class IvyVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "ivy-default"
    pom_repository_references_cleanup_policy: Optional[str] = None
    key_pair: Optional[str] = None

class MavenVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "maven-2-default"
    pom_repository_references_cleanup_policy: Optional[str] = None
    force_maven_authentication: bool = False
    key_pair: Optional[str] = None

class NpmVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "npm-default"
    retrieval_cache_period_seconds: int = 7200
    external_dependencies_enabled: bool = False
    external_dependencies_remote_repo: Optional[str] = None
    external_dependencies_patterns: List[str] = Field(default_factory=lambda: ["**"])

class NugetVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "nuget-default"
    force_nuget_authentication: bool = False

class PypiVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "simple-default"

class RpmVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "simple-default"
    primary_keypair_ref: Optional[str] = None
    secondary_keypair_ref: Optional[str] = None

class TerraformVirtualRepoConfig(BaseVirtualRepoConfig):
    repo_layout_ref: str = "terraform-module-default"

class LocalRepositories(BaseModel):
    alpine: Dict[str, AlpineRepoConfig] = Field(default_factory=dict)
    rpm: Dict[str, RpmRepoConfig] = Field(default_factory=dict)
    debian: Dict[str, DebianRepoConfig] = Field(default_factory=dict)
    docker: Dict[str, DockerRepoConfig] = Field(default_factory=dict)
    generic: Dict[str, GenericRepoConfig] = Field(default_factory=dict)
    maven: Dict[str, MavenRepoConfig] = Field(default_factory=dict)
    npm: Dict[str, NpmRepoConfig] = Field(default_factory=dict)
    nuget: Dict[str, NugetRepoConfig] = Field(default_factory=dict)
    pypi: Dict[str, PypiRepoConfig] = Field(default_factory=dict)
    helm: Dict[str, HelmRepoConfig] = Field(default_factory=dict)
    cran: Dict[str, CranRepoConfig] = Field(default_factory=dict)
    composer: Dict[str, ComposerRepoConfig] = Field(default_factory=dict)
    gems: Dict[str, GemsRepoConfig] = Field(default_factory=dict)
    go: Dict[str, GoRepoConfig] = Field(default_factory=dict)
    ivy: Dict[str, IvyRepoConfig] = Field(default_factory=dict)
    chef: Dict[str, ChefRepoConfig] = Field(default_factory=dict)
    cocoapods: Dict[str, CocoapodsRepoConfig] = Field(default_factory=dict)
    terraform_module: Dict[str, TerraformModuleRepoConfig] = Field(default_factory=dict)
    terraform_provider: Dict[str, TerraformProviderRepoConfig] = Field(default_factory=dict)
    gradle: Dict[str, GradleRepoConfig] = Field(default_factory=dict)
    helmoci: Dict[str, HelmochiRepoConfig] = Field(default_factory=dict)

class VirtualRepositories(BaseModel):
    chef: Dict[str, ChefVirtualRepoConfig] = Field(default_factory=dict)
    cran: Dict[str, CranVirtualRepoConfig] = Field(default_factory=dict)
    debian: Dict[str, DebianVirtualRepoConfig] = Field(default_factory=dict)
    docker: Dict[str, DockerVirtualRepoConfig] = Field(default_factory=dict)
    gems: Dict[str, GemsVirtualRepoConfig] = Field(default_factory=dict)
    generic: Dict[str, GenericVirtualRepoConfig] = Field(default_factory=dict)
    go: Dict[str, GoVirtualRepoConfig] = Field(default_factory=dict)
    gradle: Dict[str, GradleVirtualRepoConfig] = Field(default_factory=dict)
    helm: Dict[str, HelmVirtualRepoConfig] = Field(default_factory=dict)
    ivy: Dict[str, IvyVirtualRepoConfig] = Field(default_factory=dict)
    maven: Dict[str, MavenVirtualRepoConfig] = Field(default_factory=dict)
    npm: Dict[str, NpmVirtualRepoConfig] = Field(default_factory=dict)
    nuget: Dict[str, NugetVirtualRepoConfig] = Field(default_factory=dict)
    pypi: Dict[str, PypiVirtualRepoConfig] = Field(default_factory=dict)
    rpm: Dict[str, RpmVirtualRepoConfig] = Field(default_factory=dict)
    terraform: Dict[str, TerraformVirtualRepoConfig] = Field(default_factory=dict)

class RepositoryStructure(BaseModel):
    local_repositories: LocalRepositories = Field(default_factory=LocalRepositories)
    virtual_repositories: VirtualRepositories = Field(default_factory=VirtualRepositories)

def create_docker_repo_json(
    repo_name: str,
    key: str,
    project_key: Optional[str] = None,
    description: str = "",
    notes: str = "",
    includes_pattern: str = "**/*",
    excludes_pattern: str = "",
    repo_layout_ref: str = "simple-default",
    block_pushing_schema1: bool = False,
    priority_resolution: bool = False,
    project_environments: Optional[List[str]] = None,
    max_unique_tags: int = 0,
    blacked_out: bool = False,
    property_sets: Optional[List[str]] = None,
    archive_browsing_enabled: bool = False,
    docker_tag_retention: int = 1,
    download_direct: bool = False,
    cdn_redirect: bool = False,
    x_ray_index: bool = False,
) -> RepositoryStructure:
    if project_environments is None:
        project_environments = []
    if property_sets is None:
        property_sets = []

    repo = DockerRepoConfig(
        key=key,
        project_key=project_key,
        description=description,
        notes=notes,
        includes_pattern=includes_pattern,
        excludes_pattern=excludes_pattern,
        repo_layout_ref=repo_layout_ref,
        block_pushing_schema1=block_pushing_schema1,
        priority_resolution=priority_resolution,
        project_environments=project_environments,
        max_unique_tags=max_unique_tags,
        blacked_out=blacked_out,
        property_sets=property_sets,
        archive_browsing_enabled=archive_browsing_enabled,
        docker_tag_retention=docker_tag_retention,
        download_direct=download_direct,
        cdn_redirect=cdn_redirect,
        x_ray_index=x_ray_index,
    )
    
    local_repos = LocalRepositories()
    local_repos.docker[repo_name] = repo
    
    return RepositoryStructure(local_repositories=local_repos)

def create_maven_repo_json(
    repo_name: str,
    key: str,
    project_key: Optional[str] = None,
    description: str = "",
    notes: str = "",
    includes_pattern: str = "**/*",
    excludes_pattern: str = "",
    repo_layout_ref: str = "maven-2-default",
    priority_resolution: bool = False,
    project_environments: Optional[List[str]] = None,
    blacked_out: bool = False,
    property_sets: Optional[List[str]] = None,
    archive_browsing_enabled: bool = False,
    download_direct: bool = False,
    cdn_redirect: bool = False,
    x_ray_index: bool = False,
    checksum_policy_type: str = "client-checksums",
    snapshot_version_behavior: str = "unique",
    max_unique_snapshots: int = 0,
    handle_releases: bool = True,
    handle_snapshots: bool = True,
    suppress_pom_consistency_checks: bool = False,
) -> RepositoryStructure:
    if project_environments is None:
        project_environments = []
    if property_sets is None:
        property_sets = []

    repo = MavenRepoConfig(
        key=key,
        project_key=project_key,
        description=description,
        notes=notes,
        includes_pattern=includes_pattern,
        excludes_pattern=excludes_pattern,
        repo_layout_ref=repo_layout_ref,
        priority_resolution=priority_resolution,
        project_environments=project_environments,
        blacked_out=blacked_out,
        property_sets=property_sets,
        archive_browsing_enabled=archive_browsing_enabled,
        download_direct=download_direct,
        cdn_redirect=cdn_redirect,
        x_ray_index=x_ray_index,
        checksum_policy_type=checksum_policy_type,
        snapshot_version_behavior=snapshot_version_behavior,
        max_unique_snapshots=max_unique_snapshots,
        handle_releases=handle_releases,
        handle_snapshots=handle_snapshots,
        suppress_pom_consistency_checks=suppress_pom_consistency_checks,
    )
    
    local_repos = LocalRepositories()
    local_repos.maven[repo_name] = repo
    
    return RepositoryStructure(local_repositories=local_repos)

def create_npm_repo_json(
    repo_name: str,
    key: str,
    project_key: Optional[str] = None,
    description: str = "",
    notes: str = "",
    includes_pattern: str = "**/*",
    excludes_pattern: str = "",
    repo_layout_ref: str = "npm-default",
    priority_resolution: bool = False,
    project_environments: Optional[List[str]] = None,
    blacked_out: bool = False,
    property_sets: Optional[List[str]] = None,
    archive_browsing_enabled: bool = False,
    download_direct: bool = False,
    cdn_redirect: bool = False,
    x_ray_index: bool = False,
) -> RepositoryStructure:
    if project_environments is None:
        project_environments = []
    if property_sets is None:
        property_sets = []

    repo = NpmRepoConfig(
        key=key,
        project_key=project_key,
        description=description,
        notes=notes,
        includes_pattern=includes_pattern,
        excludes_pattern=excludes_pattern,
        repo_layout_ref=repo_layout_ref,
        priority_resolution=priority_resolution,
        project_environments=project_environments,
        blacked_out=blacked_out,
        property_sets=property_sets,
        archive_browsing_enabled=archive_browsing_enabled,
        download_direct=download_direct,
        cdn_redirect=cdn_redirect,
        x_ray_index=x_ray_index,
    )
    
    local_repos = LocalRepositories()
    local_repos.npm[repo_name] = repo
    
    return RepositoryStructure(local_repositories=local_repos)

def create_generic_repo_json(
    repo_name: str,
    key: str,
    project_key: Optional[str] = None,
    description: str = "",
    notes: str = "",
    includes_pattern: str = "**/*",
    excludes_pattern: str = "",
    repo_layout_ref: str = "simple-default",
    priority_resolution: bool = False,
    project_environments: Optional[List[str]] = None,
    blacked_out: bool = False,
    property_sets: Optional[List[str]] = None,
    archive_browsing_enabled: bool = False,
    download_direct: bool = False,
    cdn_redirect: bool = False,
    x_ray_index: bool = False,
) -> RepositoryStructure:
    if project_environments is None:
        project_environments = []
    if property_sets is None:
        property_sets = []

    repo = GenericRepoConfig(
        key=key,
        project_key=project_key,
        description=description,
        notes=notes,
        includes_pattern=includes_pattern,
        excludes_pattern=excludes_pattern,
        repo_layout_ref=repo_layout_ref,
        priority_resolution=priority_resolution,
        project_environments=project_environments,
        blacked_out=blacked_out,
        property_sets=property_sets,
        archive_browsing_enabled=archive_browsing_enabled,
        download_direct=download_direct,
        cdn_redirect=cdn_redirect,
        x_ray_index=x_ray_index,
    )
    
    local_repos = LocalRepositories()
    local_repos.generic[repo_name] = repo
    
    return RepositoryStructure(local_repositories=local_repos)

def create_helm_repo_json(
    repo_name: str,
    key: str,
    project_key: Optional[str] = None,
    description: str = "",
    notes: str = "", 
    includes_pattern: str = "**/*",
    excludes_pattern: str = "",
    repo_layout_ref: str = "simple-default",
    priority_resolution: bool = False,
    project_environments: Optional[List[str]] = None,
    blacked_out: bool = False,
    property_sets: Optional[List[str]] = None,
    archive_browsing_enabled: bool = False,
    download_direct: bool = False,
    cdn_redirect: bool = False,
    x_ray_index: bool = False,
    force_non_duplicate_chart: bool = False,
    force_metadata_name_version: bool = False,
) -> RepositoryStructure:
    if project_environments is None:
        project_environments = []
    if property_sets is None:
        property_sets = []

    repo = HelmRepoConfig(
        key=key,
        project_key=project_key,
        description=description,
        notes=notes,
        includes_pattern=includes_pattern,
        excludes_pattern=excludes_pattern,
        repo_layout_ref=repo_layout_ref,
        priority_resolution=priority_resolution,
        project_environments=project_environments,
        blacked_out=blacked_out,
        property_sets=property_sets,
        archive_browsing_enabled=archive_browsing_enabled,
        download_direct=download_direct,
        cdn_redirect=cdn_redirect,
        x_ray_index=x_ray_index,
        force_non_duplicate_chart=force_non_duplicate_chart,
        force_metadata_name_version=force_metadata_name_version,
    )
    
    local_repos = LocalRepositories()
    local_repos.helm[repo_name] = repo
    
    return RepositoryStructure(local_repositories=local_repos)

def create_pypi_repo_json(
    repo_name: str,
    key: str,
    project_key: Optional[str] = None,
    description: str = "",
    notes: str = "",
    includes_pattern: str = "**/*",
    excludes_pattern: str = "",
    repo_layout_ref: str = "simple-default",
    priority_resolution: bool = False,
    project_environments: Optional[List[str]] = None,
    blacked_out: bool = False,
    property_sets: Optional[List[str]] = None,
    archive_browsing_enabled: bool = False,
    download_direct: bool = False,
    cdn_redirect: bool = False,
    x_ray_index: bool = False,
) -> RepositoryStructure:
    if project_environments is None:
        project_environments = []
    if property_sets is None:
        property_sets = []

    repo = PypiRepoConfig(
        key=key,
        project_key=project_key,
        description=description,
        notes=notes,
        includes_pattern=includes_pattern,
        excludes_pattern=excludes_pattern,
        repo_layout_ref=repo_layout_ref,
        priority_resolution=priority_resolution,
        project_environments=project_environments,
        blacked_out=blacked_out,
        property_sets=property_sets,
        archive_browsing_enabled=archive_browsing_enabled,
        download_direct=download_direct,
        cdn_redirect=cdn_redirect,
        x_ray_index=x_ray_index,
    )
    
    local_repos = LocalRepositories()
    local_repos.pypi[repo_name] = repo
    
    return RepositoryStructure(local_repositories=local_repos)

def create_nuget_repo_json(
    repo_name: str,
    key: str,
    project_key: Optional[str] = None,
    description: str = "",
    notes: str = "",
    includes_pattern: str = "**/*",
    excludes_pattern: str = "",
    repo_layout_ref: str = "nuget-default",
    priority_resolution: bool = False,
    project_environments: Optional[List[str]] = None,
    blacked_out: bool = False,
    property_sets: Optional[List[str]] = None,
    archive_browsing_enabled: bool = False,
    download_direct: bool = False,
    cdn_redirect: bool = False,
    x_ray_index: bool = False,
    max_unique_snapshots: int = 0,
    force_nuget_authentication: bool = False,
) -> RepositoryStructure:
    if project_environments is None:
        project_environments = []
    if property_sets is None:
        property_sets = []

    repo = NugetRepoConfig(
        key=key,
        project_key=project_key,
        description=description,
        notes=notes,
        includes_pattern=includes_pattern,
        excludes_pattern=excludes_pattern,
        repo_layout_ref=repo_layout_ref,
        priority_resolution=priority_resolution,
        project_environments=project_environments,
        blacked_out=blacked_out,
        property_sets=property_sets,
        archive_browsing_enabled=archive_browsing_enabled,
        download_direct=download_direct,
        cdn_redirect=cdn_redirect,
        x_ray_index=x_ray_index,
        max_unique_snapshots=max_unique_snapshots,
        force_nuget_authentication=force_nuget_authentication,
    )
    
    local_repos = LocalRepositories()
    local_repos.nuget[repo_name] = repo
    
    return RepositoryStructure(local_repositories=local_repos)

def create_alpine_repo_json(
    repo_name: str,
    key: str,
    project_key: Optional[str] = None,
    description: str = "",
    notes: str = "",
    includes_pattern: str = "**/*",
    excludes_pattern: str = "",
    repo_layout_ref: str = "simple-default",
    priority_resolution: bool = False,
    project_environments: Optional[List[str]] = None,
    blacked_out: bool = False,
    property_sets: Optional[List[str]] = None,
    archive_browsing_enabled: bool = False,
    download_direct: bool = False,
    cdn_redirect: bool = False,
    x_ray_index: bool = False,
    primary_key_pair_ref: Optional[str] = None,
) -> RepositoryStructure:
    if project_environments is None:
        project_environments = []
    if property_sets is None:
        property_sets = []

    repo = AlpineRepoConfig(
        key=key,
        project_key=project_key,
        description=description,
        notes=notes,
        includes_pattern=includes_pattern,
        excludes_pattern=excludes_pattern,
        repo_layout_ref=repo_layout_ref,
        priority_resolution=priority_resolution,
        project_environments=project_environments,
        blacked_out=blacked_out,
        property_sets=property_sets,
        archive_browsing_enabled=archive_browsing_enabled,
        download_direct=download_direct,
        cdn_redirect=cdn_redirect,
        x_ray_index=x_ray_index,
        primary_key_pair_ref=primary_key_pair_ref,
    )
    
    local_repos = LocalRepositories()
    local_repos.alpine[repo_name] = repo
    
    return RepositoryStructure(local_repositories=local_repos)

def create_rpm_repo_json(
    repo_name: str,
    key: str,
    project_key: Optional[str] = None,
    description: str = "",
    notes: str = "",
    includes_pattern: str = "**/*",
    excludes_pattern: str = "",
    repo_layout_ref: str = "simple-default",
    priority_resolution: bool = False,
    project_environments: Optional[List[str]] = None,
    blacked_out: bool = False,
    property_sets: Optional[List[str]] = None,
    archive_browsing_enabled: bool = False,
    download_direct: bool = False,
    cdn_redirect: bool = False,
    x_ray_index: bool = False,
    primary_key_pair_ref: Optional[str] = None,
    secondary_key_pair_ref: Optional[str] = None,
    yum_root_depth: int = 0,
    yum_group_file_names: Optional[str] = None,
    enable_file_lists_indexing: bool = False,
    calculate_yum_metadata: bool = False,
) -> RepositoryStructure:
    if project_environments is None:
        project_environments = []
    if property_sets is None:
        property_sets = []

    repo = RpmRepoConfig(
        key=key,
        project_key=project_key,
        description=description,
        notes=notes,
        includes_pattern=includes_pattern,
        excludes_pattern=excludes_pattern,
        repo_layout_ref=repo_layout_ref,
        priority_resolution=priority_resolution,
        project_environments=project_environments,
        blacked_out=blacked_out,
        property_sets=property_sets,
        archive_browsing_enabled=archive_browsing_enabled,
        download_direct=download_direct,
        cdn_redirect=cdn_redirect,
        x_ray_index=x_ray_index,
        primary_key_pair_ref=primary_key_pair_ref,
        secondary_key_pair_ref=secondary_key_pair_ref,
        yum_root_depth=yum_root_depth,
        yum_group_file_names=yum_group_file_names,
        enable_file_lists_indexing=enable_file_lists_indexing,
        calculate_yum_metadata=calculate_yum_metadata,
    )
    
    local_repos = LocalRepositories()
    local_repos.rpm[repo_name] = repo
    
    return RepositoryStructure(local_repositories=local_repos)

def create_debian_repo_json(
    repo_name: str,
    key: str,
    project_key: Optional[str] = None,
    description: str = "",
    notes: str = "",
    includes_pattern: str = "**/*",
    excludes_pattern: str = "",
    repo_layout_ref: str = "simple-default",
    priority_resolution: bool = False,
    project_environments: Optional[List[str]] = None,
    blacked_out: bool = False,
    property_sets: Optional[List[str]] = None,
    archive_browsing_enabled: bool = False,
    download_direct: bool = False,
    cdn_redirect: bool = False,
    x_ray_index: bool = False,
    primary_key_pair_ref: Optional[str] = None,
    secondary_key_pair_ref: Optional[str] = None,
    optional_index_compression_formats: Optional[List[str]] = None,
    trivial_layout: bool = False,
) -> RepositoryStructure:
    if project_environments is None:
        project_environments = []
    if property_sets is None:
        property_sets = []
    if optional_index_compression_formats is None:
        optional_index_compression_formats = ["bz2"]

    repo = DebianRepoConfig(
        key=key,
        project_key=project_key,
        description=description,
        notes=notes,
        includes_pattern=includes_pattern,
        excludes_pattern=excludes_pattern,
        repo_layout_ref=repo_layout_ref,
        priority_resolution=priority_resolution,
        project_environments=project_environments,
        blacked_out=blacked_out,
        property_sets=property_sets,
        archive_browsing_enabled=archive_browsing_enabled,
        download_direct=download_direct,
        cdn_redirect=cdn_redirect,
        x_ray_index=x_ray_index,
        primary_key_pair_ref=primary_key_pair_ref,
        secondary_key_pair_ref=secondary_key_pair_ref,
        optional_index_compression_formats=optional_index_compression_formats,
        trivial_layout=trivial_layout,
    )
    
    local_repos = LocalRepositories()
    local_repos.debian[repo_name] = repo
    
    return RepositoryStructure(local_repositories=local_repos)

# Add virtual repository creation functions
def create_chef_virtual_repo_json(
    repo_name: str,
    key: str,
    repositories: Optional[List[str]] = None,
    description: str = "",
    notes: str = "",
    project_key: Optional[str] = None,
    project_environments: Optional[List[str]] = None,
    includes_pattern: str = "**/*",
    excludes_pattern: str = "",
    repo_layout_ref: str = "simple-default",
    artifactory_requests_can_retrieve_remote_artifacts: bool = False,
    default_deployment_repo: Optional[str] = None,
    retrieval_cache_period_seconds: int = 7200,
    allow_delete: bool = True,
) -> RepositoryStructure:
    if repositories is None:
        repositories = []
    if project_environments is None:
        project_environments = []

    repo = ChefVirtualRepoConfig(
        key=key,
        repositories=repositories,
        description=description,
        notes=notes,
        project_key=project_key,
        project_environments=project_environments,
        includes_pattern=includes_pattern,
        excludes_pattern=excludes_pattern,
        repo_layout_ref=repo_layout_ref,
        artifactory_requests_can_retrieve_remote_artifacts=artifactory_requests_can_retrieve_remote_artifacts,
        default_deployment_repo=default_deployment_repo,
        allow_delete=allow_delete,
        retrieval_cache_period_seconds=retrieval_cache_period_seconds,
    )
    
    virtual_repos = VirtualRepositories()
    virtual_repos.chef[repo_name] = repo
    
    return RepositoryStructure(virtual_repositories=virtual_repos)

def create_docker_virtual_repo_json(
    repo_name: str,
    key: str,
    repositories: Optional[List[str]] = None,
    description: str = "",
    notes: str = "",
    project_key: Optional[str] = None,
    project_environments: Optional[List[str]] = None,
    includes_pattern: str = "**/*",
    excludes_pattern: str = "",
    repo_layout_ref: str = "simple-default",
    artifactory_requests_can_retrieve_remote_artifacts: bool = False,
    default_deployment_repo: Optional[str] = None,
    resolve_docker_tags_by_timestamp: bool = False,
    allow_delete: bool = True,
) -> RepositoryStructure:
    if repositories is None:
        repositories = []
    if project_environments is None:
        project_environments = []

    repo = DockerVirtualRepoConfig(
        key=key,
        repositories=repositories,
        description=description,
        notes=notes,
        project_key=project_key,
        project_environments=project_environments,
        includes_pattern=includes_pattern,
        excludes_pattern=excludes_pattern,
        repo_layout_ref=repo_layout_ref,
        artifactory_requests_can_retrieve_remote_artifacts=artifactory_requests_can_retrieve_remote_artifacts,
        default_deployment_repo=default_deployment_repo,
        allow_delete=allow_delete,
        resolve_docker_tags_by_timestamp=resolve_docker_tags_by_timestamp,
    )
    
    virtual_repos = VirtualRepositories()
    virtual_repos.docker[repo_name] = repo
    
    return RepositoryStructure(virtual_repositories=virtual_repos)

# Example usage:
if __name__ == "__main__":
    # Create a Docker repository
    docker_repo = create_docker_repo_json(
        repo_name="my-docker-repo",
        key="my-docker-repo",
        description="A local Docker repository for internal use",
        notes="Used for staging Docker images",
        includes_pattern="**/*",
        excludes_pattern="*.tmp",
        block_pushing_schema1=True,
        priority_resolution=True,
        property_sets=["artifactory"],
    )
    
    # Create a Maven repository
    maven_repo = create_maven_repo_json(
        repo_name="my-maven-repo",
        key="my-maven-repo",
        description="A local Maven repository",
        priority_resolution=True,
        property_sets=["artifactory"],
    )
    
    # Create an NPM repository
    npm_repo = create_npm_repo_json(
        repo_name="my-npm-repo",
        key="my-npm-repo",
        description="A local NPM repository",
        priority_resolution=True,
        property_sets=["artifactory"],
    )
    
    # Create a Chef virtual repository
    chef_virtual_repo = create_chef_virtual_repo_json(
        repo_name="my-chef-virtual",
        key="my-chef-virtual",
        description="A virtual Chef repository",
        repositories=["chef1", "chef2"],
    )
    
    # Print as JSON
    print("Docker Repository:")
    print(json.dumps(docker_repo.dict(), indent=2))
    print("\nMaven Repository:")
    print(json.dumps(maven_repo.dict(), indent=2))
    print("\nNPM Repository:")
    print(json.dumps(npm_repo.dict(), indent=2))
    print("\nChef Virtual Repository:")
    print(json.dumps(chef_virtual_repo.dict(), indent=2))
