# AI-Powered-Infrastructure-DSL-Pipeline

> Build Infrastructure from Natural Language — Powered by LLMs, CrewAI, and Terraform.  
> Designed to mirror real-world AI Infra platforms like those inside Airbnb, AWS, and NVIDIA.

---

## Overview

This project showcases an **AI-first Infrastructure-as-Code (IaC) pipeline**, where a user describes their infrastructure requirements in **natural language**, and the system generates **modular, production-grade Terraform code**, injects secrets, validates policies, and applies it after human approval.

💡 Example:  
You write → `"Provision a 3-tier VPC with public and private subnets, an EC2 in the private subnet, and an RDS DB"`  
This system → Generates production-level HCL code with best practices.

---

## 🧱 Architecture

```bash
terraform-ai-dsl/
├── agents/                 # CrewAI agents (parser, planner, generator, validator, executor)
├── crew/                   # CrewAI task orchestration logic
├── pipelines/              # NLP-to-DSL and DSL-to-Terraform pipeline
├── terraform/              # Final generated Terraform project (main.tf, variables.tf, etc.)
├── modules/                # Reusable Terraform modules (vpc, ec2, rds, alb, etc.)
├── docs/                   # Terraform Docs auto-generated here
├── secrets/                # Encrypted secrets (KMS or Vault ready)
├── compliance/             # Regional tagging, policy rules, allow/deny lists
├── tests/                  # Unit tests for DSL interpretation and HCL correctness
└── README.md               # You're here!


## FlowChart
```bash
  A[Natural Language Input] --> B[Parse to DSL via NLParserAgent]
  B --> C[Add Compliance + Policies via DSLPlannerAgent]
  C --> D[Generate Modular Terraform via HCLGeneratorAgent]
  D --> E[Inject Secrets via SecretAgent]
  E --> F[Validate with PolicyValidatorAgent]
  F --> G[Generate Terraform Docs via DocAgent]
  G --> H{Human Approval}
  H -->|Yes| I[terraform apply]
  H -->|No| J[Halt]
