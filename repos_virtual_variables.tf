variable "artifactory_access_token" {
  type      = string
  sensitive = true
}

variable "artifactory_url" {
  type      = string
  sensitive = true
}

variable "keypair_default" {
  type = object({
    pair_name   = string
    pair_type   = string
    alias       = string
    public_key  = string
    private_key = string
  })
  sensitive = true
}

variable "remote_repo_credentials" {
  description = "Remote repository credentials for Artifactory repositories."
  type = object({
    alpine    = optional(map(object({ password = string })))
    bower     = optional(map(object({ password = string })))
    chef      = optional(map(object({ password = string })))
    cocoapods = optional(map(object({ password = string })))
    composer  = optional(map(object({ password = string })))
    conda     = optional(map(object({ password = string })))
    cran      = optional(map(object({ password = string })))
    debian    = optional(map(object({ password = string })))
    docker    = optional(map(object({ password = string })))
    gems      = optional(map(object({ password = string })))
    generic   = optional(map(object({ password = string })))
    go        = optional(map(object({ password = string })))
    gradle    = optional(map(object({ password = string })))
    helm      = optional(map(object({ password = string })))
    maven     = optional(map(object({ password = string })))
    npm       = optional(map(object({ password = string })))
    nuget     = optional(map(object({ password = string })))
    pypi      = optional(map(object({ password = string })))
    rpm       = optional(map(object({ password = string })))
    terraform = optional(map(object({ password = string })))
    vcs       = optional(map(object({ password = string })))
  })
  sensitive = true
}