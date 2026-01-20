# Serverless Evolution: From Functions to Constructs

Source: https://www.infoq.com/articles/cloud-computing-post-serverless-trends/
Date: 2024-01-24

## Core Thesis

Cloud computing is evolving beyond traditional serverless (FaaS) toward "construct-rich" services that eliminate the need for custom function code by providing configurable, composable cloud primitives.

## Three Major Trends

### 1. From Primitives to Constructs as a Service

**Evolution of Software Units:**
- Monolithic apps → Microservices (on VMs/containers)
- Microservices → Functions (FaaS like Lambda)
- Functions → **Cloud Constructs** (configurable capabilities)

**Constructs Replacing Function Code:**

Programming constructs (if-else, loops, try-catch) are becoming **cloud service configurations**:

| Task | Old Way (Lambda code) | New Way (Cloud construct) |
|------|----------------------|---------------------------|
| Request routing | Parse & route in function | API Gateway routes |
| Request validation | if-else validation | OpenAPI schema validation |
| Data transformation | Custom mapping code | Apache Velocity templates |
| Event filtering | Filter logic in function | Event Source Mapping filters |
| Event batching | Loop to aggregate | Event Source Mapping batching |
| Retry/DLQ | try-catch logic | Built-in retry + DLQ config |
| Calling other services | boto3/SDK code | StepFunction tasks |

**Key AWS Examples:**
- **API Gateway**: Direct service integration, no Lambda needed for routing/transformation
- **DynamoDB Streams**: Mandatory change data capture, no dual-write code
- **EventBridge Pipes**: Filtering, transformation, enrichment via JSON path
- **StepFunctions**: Call HTTP endpoints, read/write DB without Lambda
- **Lambda Destinations**: Result-based routing without invocation code

**Result:** Moving from **FaaS** to **NoFaaS** (no fuss) - many use cases don't need custom functions at all.

### 2. From Hyperscale to Hyperspecialization

**The Shift:**
- Hyperscalers (AWS, Azure, GCP): Broad services, horizontal expansion
- **Vertical Multi-Cloud Services**: Deep specialization in one area with rich constructs

**Why Hyperspecializers Win:**
- Better developer experience
- More granular, domain-specific constructs
- Simplified complexity (deep in one area vs. shallow in many)

**Examples of Hyperspecialized Services:**

| Service | Hyperscaler Alternative | Why Better |
|---------|------------------------|------------|
| **Confluent Cloud** | AWS MSK, Azure Event Hubs | Kafka + connectors + Flink + schema registry + governance |
| **Vercel** | AWS Amplify | Frontend DX, edge deployment, preview environments |
| **Supabase** | AWS Amplify/Firebase | Open-source, Postgres-based, self-hostable |
| **MongoDB Atlas** | DocumentDB | Native MongoDB, better tooling, multi-cloud |
| **Neon** | Aurora Serverless | Database branching, instant scaling, PostgreSQL |
| **PlanetScale** | Aurora MySQL | Schema changes without downtime, branching |
| **Temporal** | StepFunctions | Durable execution across any infrastructure |
| **Diagrid Catalyst** | (none) | Serverless Dapr APIs - messaging + workflows |
| **Upstash** | AWS MSK Serverless | Low-latency serverless Kafka + Redis |

**Future:** Bare-bones serverless primitives without rich constructs will feel like "on-premise software."

### 3. From Infrastructure as Code (IaC) to Composition as Code (CaC)

**Evolution of Cloud Automation:**

**Gen 1: IaC with DSLs**
- Tools: Terraform, Ansible, Chef, Puppet
- Languages: HCL, YAML (declarative)
- Users: Operations teams
- Focus: Infrastructure primitives (VMs, networks, storage)

**Gen 2: CaC with General-Purpose Languages**
- Tools: Pulumi, AWS CDK
- Languages: TypeScript, Python, Go, C#, Java
- Users: **Developers** (shift-left)
- Focus: Application composition + infrastructure

**Why General-Purpose Languages:**
- More expressive for logic-driven constructs
- Same language for business logic + cloud composition
- Developer self-service (not waiting on platform teams)

**Developer Responsibilities Expand:**
- Business logic (Lambda functions)
- **+ Routing config** (API Gateway)
- **+ Event filtering** (EventBridge rules)
- **+ Data streaming** (DynamoDB Streams)
- **+ Orchestration** (StepFunctions)

**Platform teams** still use declarative IaC (Terraform) for governance, security, monitoring - but **developer-focused constructs shift left** to developers.

## Redefinition of Microservices

Microservices evolve from **architectural boundary** to **organizational boundary**:

**Old:** Microservice = single deployment unit (one container/function)

**New:** Microservice = composition of:
- Functions
- Containers
- Cloud constructs (routing, filtering, streaming, orchestration)
- All implemented in a **single language** by the dev team

## Implications

1. **Less Custom Code:** Cloud constructs handle plumbing (routing, filtering, retries, DLQs)
2. **More Configuration:** Developers configure constructs instead of writing logic
3. **Vertical Specialization:** Best-in-class services win in specific domains
4. **Developer-First:** Composition shifts from ops to developers
5. **Language Convergence:** Same language for app logic + cloud composition

## Technologies to Watch

**Construct-Rich Platforms:**
- AWS (API Gateway, EventBridge, StepFunctions)
- Confluent Cloud (Kafka ecosystem)
- Temporal (durable execution)
- Diagrid Catalyst (serverless Dapr)

**CaC Tools:**
- Pulumi (multi-language IaC)
- AWS CDK (TypeScript/Python/Java/Go)
- Terraform CDK (programmatic Terraform)

**Vertical Multi-Cloud:**
- Database: Neon, PlanetScale, Fauna, MongoDB Atlas
- Frontend: Vercel, Railway
- Backend: Supabase, Temporal
- Messaging: Upstash, Confluent Cloud

## Key Quote

> "The future is shaping to be hyperspecialized and focused on the developer-first cloud."

## Related Concepts

- Dapr (Distributed Application Runtime)
- Event-driven architecture patterns (Content Enricher, Message Filter, Router)
- Infrastructure from Code (IfC) / Framework-Defined Infrastructure
- Developer self-service platforms
