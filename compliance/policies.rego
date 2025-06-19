package terraform.policies

allow = true { input.tags.owner == "ai-pipeline" }
