# AI-Powered Infrastructure DSL Pipeline

![Terraform](https://img.shields.io/badge/Terraform-Infrastructure-blue)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![GitHub Actions](https://github.com/yourusername/terraform-ai-dsl/workflows/Terraform%20CI/badge.svg)

---

## Project Overview

This project demonstrates a production-grade AI-powered Infrastructure DSL pipeline that converts natural language infrastructure requests into Terraform code using a modular set of AI agents (CrewAI). It features:

- Natural Language Parsing (GPT-4)
- DSL Planning & Validation
- HCL Terraform generation with reusable modules
- Secure secrets injection
- Policy compliance checks
- Automated Terraform lifecycle (init, plan, apply)
- GitHub Actions CI/CD
- Testing and documentation generation

---

## Architecture Diagram

```mermaid
graph TD
    UserInput["User Natural Language Prompt"]
    Parser[\"NLParserAgent (GPT-4)\"]
    Planner[\"DSLPlannerAgent\"]
    Validator[\"DSL Validator (jsonschema/OPA)\"]
    Generator[\"HCLGeneratorAgent (Terraform + Modules)\"]
    SecretAgent[\"SecretAgent (AWS KMS/Vault)\"]
    PolicyValidator[\"PolicyValidatorAgent (OPA)\"]
    Executor[\"ExecutionAgent (Terraform CLI)\"]
    TerraformCode["Terraform Code Output"]
    GitHubActions["GitHub Actions CI/CD"]

    UserInput --> Parser --> Planner --> Validator --> Generator --> SecretAgent --> PolicyValidator --> Executor --> TerraformCode
    TerraformCode --> GitHubActions



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



