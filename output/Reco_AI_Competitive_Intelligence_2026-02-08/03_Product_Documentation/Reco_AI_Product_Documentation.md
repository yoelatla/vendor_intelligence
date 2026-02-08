# Product Documentation Analysis: Reco AI

**Analysis Date:** 2026-02-08
**Vendor:** Reco AI (reco.ai)
**Category:** Dynamic SaaS Security / SaaS Security Posture Management (SSPM)
**Founded:** 2020, derived from Israeli government counterintelligence technology
**Headquarters:** Israel / United States
**Products Covered:** Unified Reco AI Platform (all pillars)
**Analyst:** Claude Agent 4 - Product Documentation & AI/ML Analyzer

---

## Executive Product Summary

Reco AI delivers a unified, cloud-native SaaS security platform purpose-built for Dynamic SaaS Security and SaaS Security Posture Management (SSPM). Founded in 2020, the company's technology lineage traces directly to Israeli government counterintelligence systems, giving it a distinctive foundation in intelligence-grade graph analytics and behavioral modeling. The platform operates on a fully agentless, API-based, read-only architecture and is available on AWS Marketplace.

Reco AI's core differentiator is its **proprietary patented Knowledge Graph (Identities Interaction Graph)**, a graph-based machine learning engine that models every user, file, record, and application as nodes with weighted interaction edges. This graph engine powers all analytics across the platform, from threat detection and behavioral analytics to identity governance and data exposure management. The company holds four patents (filed by RECOLABS LTD.) covering this interaction graph technology.

The platform has grown to support **225+ native SaaS integrations** with the ability to discover and classify over **50,000 applications**. Average connection time per app is **8 minutes**, and the company claims **80% less implementation and maintenance overhead** compared to legacy SSPM providers. Reco AI has earned recognition as a **GigaOm SSPM Radar Leader and Fast Mover** and a **SINET16 Innovator**.

**Product Philosophy:** AI-first, agentless, graph-driven SaaS security -- intelligence-grade analytics without deployment friction.
**Target Users:** Security operations teams, CISOs, IT governance teams, compliance officers, and identity/access management professionals in mid-market and enterprise organizations with significant SaaS footprints.
**Deployment Model:** Cloud-native SaaS; agentless API-based connections; available on AWS Marketplace.
**AI/ML Integration Level:** Deep -- AI/ML is foundational to the platform, not bolted on. The proprietary Knowledge Graph, NLP engine, behavioral analytics, classification engine, and autonomous AI agents are all core to platform operation.

---

## Product Portfolio

### Platform Architecture

Reco AI is a **single unified platform** with multiple functional pillars, not a collection of separate point products. All pillars share a common data fabric powered by the proprietary Knowledge Graph.

### Product Pillars Overview

| # | Pillar | Category | Purpose | AI/ML Enabled |
|---|--------|----------|---------|---------------|
| 1 | App Discovery & Governance | SaaS Visibility | Discovers and classifies 50,000+ apps; 225+ native integrations | Yes -- Classification Engine |
| 2 | SaaS Posture Management & Compliance | SSPM / Compliance | Continuous configuration monitoring across 20+ compliance frameworks | Yes -- Automated policy analysis |
| 3 | Identity & Access Governance | IAM / IGA | Unified identity consolidation, admin monitoring, MFA enforcement | Yes -- Knowledge Graph identity mapping |
| 4 | Threat Detection & Response | Threat Detection / UEBA | Hundreds of pre-built detections, behavioral analytics | Yes -- UEBA, Knowledge Graph, anomaly detection |
| 5 | Data Exposure Management | Data Security | Automated PII/PHI/IP classification, permission analysis | Yes -- Sensitive Data Classification Engine |
| 6 | Shadow AI & SaaS Discovery | Shadow IT | NLP-based email metadata analysis to detect unauthorized tools | Yes -- NLP Engine |
| 7 | AI Governance & Security | AI Security | AI feature discovery, risk assessment, policy enforcement | Yes -- Classification Engine, Knowledge Graph |
| 8 | Agentic AI Security | AI Security | Detection of autonomous AI agents, non-human identity governance | Yes -- Knowledge Graph, behavioral analysis |
| 9 | AI Agents for SaaS Security | Autonomous Operations | Alert Summary Agent (launched); additional agents planned | Yes -- Autonomous AI Agents |
| 10 | SaaS App Factory | Platform Extensibility | Proprietary no-code engine; 3-5 day new app integration cycle | Yes -- Template-based ML pipeline |

### Product Relationships & Data Flow

All ten pillars operate on a shared data layer powered by the Knowledge Graph. Data flows as follows:

```
SaaS Apps (225+) --> API-Based Connectors (Read-Only, Agentless)
    --> Raw Event & Metadata Ingestion
        --> Knowledge Graph Engine (Nodes: Users, Files, Records, Apps; Edges: Weighted Interactions)
            --> NLP Engine (Email Metadata Analysis)
            --> Classification Engine (50,000+ App Taxonomy)
            --> Behavioral Analytics / UEBA (Baseline Modeling, Anomaly Detection)
            --> Sensitive Data Classification (PII/PHI/IP/Financial)
                --> Unified Analytics Layer
                    --> Dashboards, Alerts, Compliance Reports
                    --> AI Agents (Alert Summary, Future: Consolidation, Shadow Detection, Identity Management)
                    --> SIEM/SOAR/Ticketing Integrations (Downstream)
```

---

## Detailed Pillar Analysis

### Pillar 1: App Discovery & Governance

**Purpose:** Provides complete visibility into the entire SaaS ecosystem, including sanctioned, unsanctioned, and shadow applications.

**Key Capabilities:**
- Discovery and classification of **50,000+ SaaS applications** using the AI-based Classification Engine
- **225+ native integrations** with direct API connectors
- Automated app categorization: productivity, collaboration, development, AI/ML tools, finance, HR, and more
- Risk scoring for each discovered application
- Governance workflows: approval, blocking, and review processes
- Identification of redundant/overlapping applications for consolidation opportunities

**AI/ML Technologies Used:** Classification Engine (supervised ML categorization of application types, risk tiers, and functional categories)

---

### Pillar 2: SaaS Posture Management & Compliance

**Purpose:** Continuously monitors SaaS configuration settings against security best practices and compliance requirements.

**Key Capabilities:**
- Continuous configuration monitoring across all connected SaaS apps
- **20+ compliance frameworks** supported, including SOC 2, ISO 27001, NIST CSF, NIST 800-53, CIS Benchmarks, HIPAA, PCI DSS, GDPR, CCPA, SOX, FedRAMP, and others
- Automated misconfiguration detection and remediation guidance
- Compliance posture dashboards with drill-down capability
- Drift detection: identifies when configurations change from approved baselines
- Evidence collection and audit trail generation for compliance audits

**AI/ML Technologies Used:** Knowledge Graph (maps configuration relationships and blast radius); automated policy analysis

---

### Pillar 3: Identity & Access Governance

**Purpose:** Consolidates identities across all connected SaaS applications into a unified view and enforces governance policies.

**Key Capabilities:**
- **Unified identity consolidation:** maps the same user across all SaaS apps regardless of login method (SSO, local, OAuth, service accounts)
- Admin account monitoring: identifies over-privileged administrators, dormant admin accounts, and admin sprawl
- MFA enforcement visibility: detects users and apps without MFA enabled
- External user and guest access monitoring
- Service account and non-human identity tracking
- Access reviews and certification campaigns
- Least-privilege analysis and recommendations

**AI/ML Technologies Used:** Knowledge Graph (identity node resolution and cross-app correlation); behavioral analytics (identifies anomalous access patterns)

---

### Pillar 4: Threat Detection & Response

**Purpose:** Detects threats, compromised accounts, insider risks, and policy violations across the SaaS estate using behavioral analytics and pre-built detection rules.

**Key Capabilities:**
- **Hundreds of pre-built detection rules** covering account compromise, insider threats, data exfiltration, privilege escalation, and policy violations
- Behavioral analytics (UEBA): baselines normal behavior and detects deviations
- Cross-app correlation: connects suspicious activities across multiple SaaS applications via the Knowledge Graph
- Real-time alerting with context-rich alert details
- Integration with SIEM (Splunk, etc.) and SOAR (Palo Alto XSOAR, Torq, Tines) for automated response
- Investigation workflows with timeline visualization

**AI/ML Technologies Used:** Behavioral Analytics / UEBA (supervised + unsupervised ML, clustering, probabilistic anomaly detection); Knowledge Graph (cross-entity correlation); AI Alert Summary Agent (context enrichment)

---

### Pillar 5: Data Exposure Management

**Purpose:** Identifies sensitive data across SaaS applications and analyzes sharing permissions to detect and remediate data exposure risks.

**Key Capabilities:**
- **Automated sensitive data classification:** PII (personally identifiable information), PHI (protected health information), financial records, and intellectual property (IP)
- AI-based scanning and pattern recognition for data identification
- Permission analysis: maps who has access to what data, through which sharing mechanisms
- External sharing detection: identifies files and records shared outside the organization
- Public link detection and remediation
- Data exposure risk scoring based on sensitivity level and sharing scope
- Remediation workflows: revoke access, notify owners, enforce policies

**AI/ML Technologies Used:** Automated Sensitive Data Classification Engine (AI-based scanning, pattern recognition, real-time classification); Knowledge Graph (maps data-to-user-to-app relationships)

---

### Pillar 6: Shadow AI & SaaS Discovery

**Purpose:** Discovers unauthorized SaaS and AI tools being used by employees through NLP-based analysis of email metadata.

**Key Capabilities:**
- **NLP-based email metadata analysis** from Gmail and Microsoft Outlook
- Detects communications with unauthorized SaaS and AI tool vendors (signup confirmations, onboarding emails, billing notifications)
- Intelligent filtering of internal applications and marketing/promotional emails to reduce false positives
- Shadow AI detection: specifically identifies unauthorized AI tools (ChatGPT, Bard, Midjourney, Cursor, Copilot, etc.)
- Risk assessment of discovered shadow tools
- Governance workflows for newly discovered applications

**AI/ML Technologies Used:** Fine-tuned NLP model (email metadata classification, vendor identification, marketing email filtering); Classification Engine (categorization of discovered tools)

---

### Pillar 7: AI Governance & Security

**Purpose:** Discovers AI features embedded within sanctioned SaaS applications, assesses their risk, and enforces governance policies.

**Key Capabilities:**
- AI feature discovery: identifies when SaaS vendors activate AI/ML features (e.g., Salesforce Einstein, Microsoft Copilot, Slack AI)
- Risk assessment of AI features: evaluates data access, training data usage, and third-party AI model risks
- Policy enforcement: enables security teams to approve, restrict, or block AI features
- AI usage monitoring: tracks which users are interacting with AI features and what data is being processed
- Compliance mapping for AI-specific regulations and frameworks

**AI/ML Technologies Used:** Classification Engine (AI feature identification); Knowledge Graph (maps AI feature data flows)

---

### Pillar 8: Agentic AI Security

**Purpose:** Detects and governs autonomous AI agents (agentic AI) operating within the SaaS ecosystem, including non-human identities created by AI systems.

**Key Capabilities:**
- Detection of autonomous AI agents interacting with SaaS applications
- Non-human identity governance: tracks service accounts, API tokens, and bot identities created by or for AI agents
- Behavioral monitoring of AI agent actions: identifies anomalous autonomous behaviors
- Permission analysis for AI agents: ensures least-privilege access
- Policy enforcement for AI agent interactions

**AI/ML Technologies Used:** Knowledge Graph (models AI agent interactions as nodes/edges); behavioral analytics (baselines AI agent behavior patterns)

---

### Pillar 9: AI Agents for SaaS Security

**Purpose:** Deploys autonomous AI agents that assist security teams by automating analysis, investigation, and response workflows.

**Key Capabilities:**
- **Alert Summary Agent (launched -- first agent):** Provides context-rich insights for each security alert, including:
  - AI-driven alert prioritization based on asset criticality, user privilege level, and historical behavior context
  - Leverages the Knowledge Graph to evaluate the full context of an alert (who, what, where, when, why)
  - Automated narrative summaries that explain the alert in plain language
  - Recommended response actions
- **Planned future agents:**
  - App Consolidation Agent: recommends redundant app elimination
  - Shadow Detection Agent: proactively hunts for shadow SaaS/AI
  - Identity Management Agent: automates access reviews and deprovisioning

**AI/ML Technologies Used:** Autonomous AI Agents built on Knowledge Graph context; AI-driven prioritization models

---

### Pillar 10: SaaS App Factory

**Purpose:** A proprietary no-code engine that enables rapid development of new SaaS app integrations.

**Key Capabilities:**
- **3-5 day integration cycle** for new SaaS applications (vs. weeks/months for competitors)
- No-code integration builder: security analysts and engineers can define data mappings, detection rules, and governance policies without writing code
- Template-based approach: leverages patterns from 225+ existing integrations
- Customer-requested integrations delivered rapidly
- Milestone: **Cursor was the 200th integration**, now at 225+

**AI/ML Technologies Used:** ML-assisted mapping and template generation based on patterns from existing integrations

---

## Core Architecture

### Deployment Model

| Attribute | Detail |
|-----------|--------|
| **Deployment Type** | Cloud-native SaaS |
| **Architecture** | Agentless, API-based, read-only connections |
| **Cloud Availability** | AWS Marketplace |
| **Average Connection Time** | 8 minutes per app |
| **Implementation Overhead** | 80% less than legacy SSPM providers |
| **Agent Required** | No -- fully agentless |
| **Data Residency** | Cloud-hosted; specific regions available via AWS |
| **Multi-Tenancy** | Yes |

### Architecture Principles

1. **Agentless by design:** No software agents deployed on endpoints or within SaaS applications. All data collection occurs through API-based, read-only connections. This eliminates deployment friction, reduces attack surface, and ensures zero performance impact on monitored applications.

2. **Read-only access:** Reco AI connects to SaaS APIs using read-only permissions. The platform observes and analyzes but does not modify configurations, data, or permissions directly (remediation actions are recommended and can be executed through integrated workflows).

3. **Knowledge Graph-centric:** All analytics, detections, identity resolution, and context enrichment flow through the proprietary Knowledge Graph. This is not a bolt-on feature -- it is the foundational data structure of the entire platform.

4. **Rapid time-to-value:** 8-minute average connection time per app. The SaaS App Factory enables 3-5 day integration development for new apps.

---

## AI/ML/LLM TECHNOLOGY DEEP DIVE

### AI/ML Technology Overview

**AI/ML Maturity Level:** Leading
**Primary AI Technologies:** Proprietary Knowledge Graph (Graph-based ML), NLP, Behavioral Analytics (UEBA), Classification Engine, Autonomous AI Agents, Automated Data Classification
**AI-Powered Features Count:** 6 core AI/ML technologies powering all 10 platform pillars
**AI Implementation Approach:** Proprietary (built in-house, patented, informed by CTO's academic research)

**Overall Assessment:**
Reco AI is an AI-first platform where machine learning is not a feature layer but the foundational architecture. The patented Knowledge Graph is the central nervous system of the product, and every functional pillar depends on AI/ML for its core operation. The company's technology heritage from Israeli government counterintelligence, combined with the CTO's extensive academic publication record in AI/ML for cybersecurity, provides a credible and differentiated AI foundation. With four patents, 14 research publications, and a CTO who has published on self-attention mechanisms for network security, encrypted traffic classification, and zero-shot IoT labeling with LLMs, Reco AI's AI capabilities are grounded in genuine research rather than marketing claims.

---

### Technology 1: Proprietary Knowledge Graph / Identities Interaction Graph

**Overview:**
- **Type:** Graph-based Machine Learning
- **Specific Model/Framework:** Proprietary graph database and ML engine (patented)
- **Implementation:** Fully proprietary; 4 patents held by RECOLABS LTD.
- **Patent Inventors:** Include Tal Shapira (CTO) and co-inventors
- **Status:** Core production technology; foundational to all platform capabilities

**Use Case & Application:**

- **Problem Solved:** SaaS security requires understanding complex, dynamic relationships between users, applications, files, records, and permissions across hundreds of applications. Traditional tabular or log-based approaches fail to capture the interconnected nature of these relationships. The Knowledge Graph solves this by modeling the entire SaaS ecosystem as an interconnected graph.

- **Features Utilizing This Technology:**
  - **Identity & Access Governance:** Resolves and consolidates user identities across 225+ SaaS apps by modeling each identity as a graph node and linking aliases, SSO mappings, and OAuth connections as edges
  - **Threat Detection & Response:** Correlates suspicious activities across multiple applications by traversing the graph to find connected events and entities
  - **Data Exposure Management:** Maps file/record ownership, sharing permissions, and access chains through graph traversal
  - **AI Agent Context:** The Alert Summary Agent queries the Knowledge Graph to evaluate asset criticality, user privilege level, and historical behavior patterns
  - **Agentic AI Security:** Models AI agent interactions, service accounts, and API token relationships as graph entities

- **Concrete Example:** When a user account exhibits suspicious file-sharing behavior in Google Drive, the Knowledge Graph enables Reco AI to instantly traverse the graph to determine: (a) all other SaaS apps this user accesses, (b) their privilege level in each app, (c) all files they have accessed recently across all apps, (d) whether the shared files contain sensitive data, (e) who received the shared files and their risk profile, and (f) whether this behavior deviates from the user's historical baseline and their peer group's baseline -- all in a single correlated view.

**Technical Implementation:**

- **Graph Structure:**
  - **Nodes:** Users (human and non-human identities), files, records, applications, groups, roles, permissions, AI agents
  - **Edges:** Interactions between nodes, each carrying **"interaction weights"** that quantify the strength, frequency, recency, and type of interaction
  - **Temporal dimension:** The graph is continuously updated to reflect real-time changes, with historical snapshots retained for trend analysis and baseline comparison

- **Architecture:**
  ```
  SaaS API Connectors (225+ apps)
      --> Raw Event Stream (logins, file access, sharing, config changes, API calls)
          --> Entity Extraction & Resolution (maps events to graph nodes)
              --> Edge Creation & Weight Calculation (interaction weights computed)
                  --> Knowledge Graph Database (continuously updated)
                      --> Graph ML Algorithms (traversal, community detection, anomaly scoring)
                          --> Analytics Layer (dashboards, alerts, reports, AI agents)
  ```

- **Interaction Weights:** Each edge in the graph carries a computed weight that reflects:
  - Frequency of interaction (how often the user accesses the resource)
  - Recency (when the last interaction occurred)
  - Type of interaction (read, write, share, delete, admin action)
  - Sensitivity of the target resource
  - Direction of the interaction (who initiated, who received)

- **Graph ML Algorithms Employed:**
  - Community detection: identifies clusters of related users, apps, and data
  - Centrality analysis: identifies high-risk nodes (e.g., users with access to many sensitive resources)
  - Path analysis: determines shortest paths between entities for blast radius assessment
  - Anomaly detection on graph structure: identifies unusual new edges or missing expected edges
  - Temporal pattern analysis: detects changes in interaction patterns over time

- **Training & Updates:**
  - **Data Sources:** Real-time API data from all connected SaaS applications
  - **Training Method:** Combination of supervised (labeled threat patterns) and unsupervised (graph structure analysis) approaches
  - **Model Updates:** Continuous -- the graph is updated in real-time as new events are ingested
  - **Customer-Specific:** Each customer's Knowledge Graph is unique to their environment; models are trained on their specific data

- **Inference & Deployment:**
  - **Processing Location:** Cloud (Reco AI's cloud infrastructure / AWS)
  - **Processing Mode:** Real-time (continuous graph updates) and batch (periodic full-graph analytics)
  - **Scalability:** Graph scales with customer's SaaS footprint; designed for enterprises with hundreds of apps and tens of thousands of users

**Patents (RECOLABS LTD.):**

| Patent / Application | Title | Key Innovation |
|----------------------|-------|----------------|
| Patent 1 | "Data Security Method Using Interaction Graphs" | Defines the interaction graph with weighted edges for security analytics; methods for computing interaction scores between entities |
| Patent 2 | "Computer Implemented Method for Securing Files" | Describes process for computing interaction scores between users and files; uses these scores for file security risk assessment |
| Patent 3 | Related interaction graph methods | Extensions of the core graph technology |
| Patent 4 | Related interaction graph methods | Extensions of the core graph technology |

**Competitive Differentiation:**

| Aspect | Reco AI | Typical SSPM Competitors | Industry Standard |
|--------|---------|--------------------------|-------------------|
| Core Data Model | Patented Knowledge Graph with interaction weights | Log-based analytics, tabular databases | Rule-based detection on event logs |
| Cross-App Correlation | Native via graph traversal | Limited; requires manual correlation or SIEM | SIEM-dependent |
| Identity Resolution | Graph-based multi-app identity consolidation | Per-app identity views | IdP-dependent |
| Context Depth | Full graph context (user + data + app + permissions + behavior) | Partial context per alert | Alert-level context only |

- **Advantages:** The patented Knowledge Graph provides a fundamentally different analytical foundation than competitors' log-based or rule-based approaches. Graph-based correlation enables cross-app threat detection and identity resolution that is architecturally impossible for competitors who process each SaaS app in isolation. The interaction weights enable nuanced risk scoring that goes beyond binary rule matching.
- **Gaps:** Graph-based approaches can be computationally expensive at extreme scale; the proprietary nature means no open-source community contributions to the graph engine.
- **Innovation Level:** Cutting-edge. The patented graph-based approach with interaction weights is unique in the SSPM market.

---

### Technology 2: Natural Language Processing (NLP) Engine

**Overview:**
- **Type:** Fine-tuned NLP model
- **Specific Model/Framework:** Proprietary fine-tuned NLP model (specific base model not publicly disclosed)
- **Implementation:** Proprietary
- **Primary Application:** Shadow AI & SaaS Discovery (Pillar 6)

**Use Case & Application:**

- **Problem Solved:** Organizations cannot discover shadow SaaS and shadow AI tools through traditional network monitoring alone because these tools are accessed via standard HTTPS connections. Reco AI solves this by analyzing email metadata (not email content) to detect communications with SaaS/AI vendors -- signup confirmations, onboarding emails, billing notifications, feature announcements -- that reveal unauthorized tool usage.

- **Features Utilizing This Technology:**
  - **Shadow SaaS Discovery:** Analyzes email metadata from Gmail and Microsoft Outlook to identify vendor communications indicating SaaS tool adoption
  - **Shadow AI Detection:** Specifically trained to recognize communications from AI tool vendors (ChatGPT, Midjourney, Cursor, GitHub Copilot, etc.)
  - **Marketing Email Filtering:** Filters out marketing/promotional emails and internal communications to reduce false positives and focus on genuine tool adoption signals

- **Concrete Example:** An employee signs up for an unauthorized AI coding assistant. The NLP engine detects the welcome email, account verification email, and subsequent onboarding emails in the employee's inbox metadata. It classifies these as genuine tool adoption (not marketing) and flags the shadow AI tool for security review. Internal emails and promotional newsletters from the same vendor are filtered out.

**Technical Implementation:**

- **Architecture:**
  ```
  Gmail / Outlook APIs (email metadata only, not content)
      --> Metadata Extraction (sender, subject, timestamps, headers)
          --> NLP Classification Pipeline:
              Step 1: Vendor identification (is this from a SaaS/AI vendor?)
              Step 2: Communication type classification (signup, onboarding, billing, marketing, internal)
              Step 3: Filtering (remove marketing, internal, false positives)
              Step 4: Tool categorization (classify the discovered tool)
          --> Shadow App/AI Inventory
              --> Risk Assessment & Governance Workflows
  ```

- **Training Details:**
  - **Data Sources:** Labeled email metadata datasets covering SaaS vendor communications, marketing emails, and internal communications
  - **Training Method:** Supervised learning with fine-tuning on domain-specific email metadata corpus
  - **Model Updates:** Periodic retraining as new SaaS/AI vendors emerge
  - **Privacy:** Analyzes metadata (sender, subject line, headers) -- not email body content

- **Inference & Deployment:**
  - **Processing Location:** Cloud
  - **Processing Mode:** Batch (periodic analysis of new email metadata)
  - **Key Challenge Addressed:** Distinguishing genuine tool adoption signals from marketing noise with high precision

**Competitive Differentiation:**

- **Advantages:** Email metadata analysis for shadow SaaS discovery is a relatively uncommon approach in SSPM. Most competitors rely on CASB-style network monitoring or OAuth token analysis, which miss tools accessed via browser without SSO. The NLP approach catches shadow tools that leave no network trace other than email communications.
- **Gaps:** Dependent on email connector access (Gmail/Outlook); will not detect tools that do not send email communications.
- **Innovation Level:** Competitive to cutting-edge. Email-based shadow discovery is a distinctive approach in the SSPM market.

---

### Technology 3: Behavioral Analytics / User and Entity Behavior Analytics (UEBA)

**Overview:**
- **Type:** Behavioral analytics engine using supervised and unsupervised machine learning
- **Specific Techniques:** Clustering algorithms, probabilistic models, peer-group analysis, cross-entity baselining
- **Implementation:** Proprietary, built on top of the Knowledge Graph
- **Primary Application:** Threat Detection & Response (Pillar 4)

**Use Case & Application:**

- **Problem Solved:** Static rule-based threat detection generates excessive false positives and misses novel attacks that do not match predefined patterns. Behavioral analytics solves this by learning what "normal" looks like for each user and entity, then detecting deviations that indicate compromise, insider threats, or policy violations.

- **Features Utilizing This Technology:**
  - **Anomaly Detection:** Identifies unusual login patterns, file access patterns, sharing behaviors, and administrative actions that deviate from established baselines
  - **Peer-Group Analysis:** Compares a user's behavior to their peer group (same department, role, location) to identify outliers
  - **Cross-Entity Baselining:** Establishes behavioral baselines not just for users but for applications, files, and groups
  - **Threat Scoring:** Assigns dynamic risk scores based on the degree and type of behavioral deviation
  - **Insider Threat Detection:** Identifies patterns consistent with data exfiltration, privilege abuse, or pre-departure data hoarding

- **Concrete Example:** A sales executive who normally accesses 20-30 Salesforce records per day suddenly downloads 5,000 records in a single session. The UEBA engine detects this as a significant deviation from the user's personal baseline and their peer group's baseline (other sales executives). Cross-referencing with the Knowledge Graph reveals the user recently updated their LinkedIn profile and has a resignation email in HR systems. The system correlates these signals to generate a high-confidence insider threat alert with full context.

**Technical Implementation:**

- **Architecture:**
  ```
  Knowledge Graph (user/entity interaction data with temporal dimension)
      --> Feature Extraction (behavioral features per entity per time window)
          --> Baseline Modeling:
              - Individual baselines (per-user, per-entity historical behavior)
              - Peer-group baselines (clustering algorithms group similar entities)
              - Organizational baselines (global norms)
          --> Anomaly Detection:
              - Probabilistic models (deviation scoring against baselines)
              - Unsupervised clustering (identifies novel attack patterns)
              - Supervised models (known threat pattern matching)
          --> Risk Scoring & Alert Generation
              --> Alert Summary Agent (AI-driven context enrichment)
  ```

- **ML Model Details:**

  | Model Component | Technique | Purpose |
  |----------------|-----------|---------|
  | Baseline Modeling | Clustering algorithms (unsupervised) | Groups similar users/entities to establish peer-group norms |
  | Anomaly Scoring | Probabilistic models | Computes deviation probability from baseline; generates anomaly scores |
  | Pattern Matching | Supervised ML | Detects known threat patterns (e.g., credential stuffing sequences, exfiltration patterns) |
  | Peer-Group Analysis | Clustering + statistical comparison | Identifies outliers within peer groups |
  | Cross-Entity Baselining | Multi-dimensional baseline modeling | Baselines behavior at user, app, file, and group levels simultaneously |

- **Training Details:**
  - **Data Sources:** Customer-specific behavioral data from connected SaaS apps (via Knowledge Graph)
  - **Training Method:** Combination of supervised (labeled threat data) and unsupervised (baseline learning from unlabeled behavioral data)
  - **Model Updates:** Baselines are continuously updated as new behavioral data is ingested; supervised models are periodically retrained
  - **Warm-Up Period:** Baselines require an initial learning period to establish norms (typically days to weeks depending on data volume)

- **Inference & Deployment:**
  - **Processing Location:** Cloud
  - **Processing Mode:** Near real-time (behavioral features computed on streaming data; baselines updated in batch)
  - **Scalability:** Designed to handle behavioral modeling across tens of thousands of users and hundreds of applications

**Competitive Differentiation:**

| Aspect | Reco AI | Typical SSPM Competitors | Dedicated UEBA Vendors |
|--------|---------|--------------------------|------------------------|
| Behavioral Data Source | Knowledge Graph (cross-app, graph-structured) | Per-app log analysis | Network/endpoint logs |
| Cross-App Correlation | Native (same graph) | Requires SIEM integration | Requires data aggregation |
| Entity Types Baselined | Users, apps, files, groups, AI agents | Primarily users | Users, devices, network entities |
| Peer-Group Formation | Graph-based clustering | Role/department-based | Rule-based or ML-based |
| Context Enrichment | Knowledge Graph + AI Agent | Manual investigation | Varies |

- **Advantages:** The combination of UEBA with the Knowledge Graph provides richer behavioral context than standalone UEBA products. Cross-app correlation via the graph enables detection of multi-app attack sequences that per-app UEBA would miss. Peer-group formation benefits from graph-based clustering rather than simple role/department grouping.
- **Gaps:** UEBA effectiveness depends on data volume and quality; newer customers in the warm-up period may experience lower detection accuracy.
- **Innovation Level:** Advanced. The Knowledge Graph integration differentiates Reco AI's UEBA from standalone UEBA products, though behavioral analytics itself is a well-established technology.

---

### Technology 4: Classification Engine

**Overview:**
- **Type:** AI-based classification and categorization engine
- **Specific Techniques:** Supervised ML classification, multi-label categorization
- **Implementation:** Proprietary
- **Primary Application:** App Discovery & Governance (Pillar 1), AI Governance (Pillar 7), Shadow AI Discovery (Pillar 6)

**Use Case & Application:**

- **Problem Solved:** Organizations need to understand not just what applications exist in their environment but what type of applications they are, what risk they pose, and how they should be governed. With 50,000+ applications in the classification taxonomy, manual categorization is impossible. The Classification Engine automates this at scale.

- **Features Utilizing This Technology:**
  - **Application Classification:** Categorizes discovered applications into functional categories (productivity, collaboration, development, AI/ML, finance, HR, security, etc.)
  - **Risk Tier Assignment:** Assigns risk tiers based on application characteristics, vendor security posture, data access patterns, and compliance status
  - **AI Tool Identification:** Specifically identifies and classifies AI tools, AI features within SaaS apps, and AI agents
  - **Shadow App Categorization:** Classifies newly discovered shadow applications from the NLP engine
  - **SaaS App Factory Support:** Assists in categorizing new applications during the integration development process

- **Concrete Example:** An employee's OAuth connection reveals a new application the organization has not seen before. The Classification Engine automatically identifies it as an AI-powered code generation tool, categorizes it under "Development Tools > AI Coding Assistants," assigns it a high risk tier due to code data access, and flags it for security review.

**Technical Implementation:**

- **Architecture:**
  ```
  Application Metadata (name, domain, OAuth scopes, API patterns, vendor info)
      --> Feature Extraction (application characteristics, behavioral signals)
          --> Multi-Label ML Classifier:
              - Functional category (productivity, security, AI, etc.)
              - Risk tier (high, medium, low)
              - AI classification (is this an AI tool? What type?)
              - Compliance relevance (HIPAA, SOX, GDPR implications)
          --> Classification Output
              --> App Inventory & Governance Workflows
  ```

- **Taxonomy Scale:** 50,000+ known applications in the classification database, continuously expanding
- **Training Method:** Supervised ML trained on labeled application datasets; continuously updated as new applications emerge
- **Update Frequency:** Classification database updated regularly to keep pace with the rapidly evolving SaaS and AI tool landscape

**Competitive Differentiation:**

- **Advantages:** The 50,000+ application taxonomy is among the largest in the SSPM market. The specific focus on AI tool classification (including AI features within SaaS apps and autonomous AI agents) is forward-looking and addresses a rapidly growing market need.
- **Innovation Level:** Competitive. Application classification is a standard SSPM capability, but the scale (50,000+) and AI-specific classification are differentiators.

---

### Technology 5: AI Agents (Autonomous)

**Overview:**
- **Type:** Autonomous AI agents for security operations
- **Implementation:** Proprietary, built on the Knowledge Graph
- **Status:** Alert Summary Agent launched (GA); additional agents in development
- **Primary Application:** AI Agents for SaaS Security (Pillar 9)

**Use Case & Application:**

- **Problem Solved:** Security teams are overwhelmed by alert volume and lack the time to investigate each alert thoroughly. AI Agents automate the investigation and context-enrichment process, providing security analysts with ready-to-act intelligence rather than raw alerts.

- **Launched Agent: Alert Summary Agent**
  - Automatically generates context-rich summaries for each security alert
  - AI-driven prioritization based on:
    - **Asset criticality:** How sensitive/important is the affected resource? (queried from Knowledge Graph)
    - **User privilege level:** What is the user's role, access level, and admin status? (queried from Knowledge Graph)
    - **Historical behavior:** Does this alert represent a genuine deviation from the user's baseline? (queried from UEBA + Knowledge Graph)
  - Provides recommended response actions
  - Presents a narrative explanation in plain language

- **Planned Future Agents:**
  - **App Consolidation Agent:** Analyzes the application portfolio to identify redundant tools and recommend consolidation opportunities
  - **Shadow Detection Agent:** Proactively hunts for shadow SaaS and AI tools using multi-signal analysis
  - **Identity Management Agent:** Automates access reviews, deprovisioning recommendations, and least-privilege enforcement

- **Concrete Example:** An alert fires for "unusual file sharing from executive account." The Alert Summary Agent immediately queries the Knowledge Graph to determine: the executive is a VP of Engineering (high privilege), the shared files contain source code (high sensitivity), the recipient is an external email address not previously seen, and the executive's file-sharing volume is 15x their 90-day average. The agent generates a summary: "High-priority alert: VP Engineering shared 47 source code files with unknown external recipient -- volume 15x above baseline. Recommend immediate investigation and temporary sharing suspension." The security analyst receives an actionable brief instead of a raw alert.

**Technical Implementation:**

- **Architecture:**
  ```
  Security Alert Generated
      --> Alert Summary Agent Activated
          --> Knowledge Graph Query:
              - User node: privilege level, role, department, admin status
              - Asset nodes: sensitivity classification, ownership, sharing history
              - Historical edges: interaction patterns over time
              - Peer-group context: how does this compare to similar users?
          --> UEBA Context Query:
              - Baseline deviation magnitude
              - Anomaly score
              - Related anomalies in time window
          --> AI Summarization & Prioritization:
              - Generate plain-language narrative
              - Compute priority score
              - Generate recommended actions
          --> Output: Context-rich alert summary delivered to analyst
  ```

- **Agent Design Principles:**
  - **Knowledge Graph-native:** Agents are built to traverse and query the Knowledge Graph as their primary data source
  - **Context-first:** Every agent output includes full graph context, not just the triggering event
  - **Action-oriented:** Agents provide specific recommended actions, not just descriptions

**Competitive Differentiation:**

- **Advantages:** Reco AI is among the first SSPM vendors to deploy autonomous AI agents for security operations. The Knowledge Graph provides a richer context layer for AI agents than competitors who would need to query multiple disconnected data stores. The agent roadmap (consolidation, shadow detection, identity management) addresses high-value security operations use cases.
- **Gaps:** Only one agent (Alert Summary) is currently in production; the agent platform is early-stage. Competitors like Microsoft (Security Copilot) and CrowdStrike (Charlotte AI) are investing heavily in AI agents for security, though in different security domains.
- **Innovation Level:** Cutting-edge for the SSPM market. AI agents represent the next evolution of security automation beyond SOAR playbooks.

---

### Technology 6: Automated Sensitive Data Classification

**Overview:**
- **Type:** AI-based data scanning and pattern recognition
- **Implementation:** Proprietary
- **Primary Application:** Data Exposure Management (Pillar 5)

**Use Case & Application:**

- **Problem Solved:** Organizations need to know where sensitive data resides across their SaaS applications to manage exposure risk. Manual data classification is impractical at SaaS scale. The Automated Sensitive Data Classification engine scans content across connected SaaS apps and classifies it in real time.

- **Features Utilizing This Technology:**
  - **PII Detection:** Social security numbers, email addresses, phone numbers, addresses, names, dates of birth
  - **PHI Detection:** Medical record numbers, diagnosis codes, treatment information, insurance identifiers
  - **Financial Records Detection:** Credit card numbers, bank account numbers, financial statements, transaction records
  - **Intellectual Property Detection:** Source code, trade secrets, proprietary documents, patent-related materials
  - **Real-Time Classification:** New files and records are classified as they are created or modified
  - **Permission-Sensitivity Correlation:** Cross-references data sensitivity with sharing permissions to identify high-risk exposures

- **Concrete Example:** A Salesforce record containing customer credit card numbers and home addresses is identified by the classification engine as containing PII and financial data. The Knowledge Graph reveals this record is accessible by 45 users, including 3 external contractors. The system generates a data exposure alert with full context and remediation recommendations.

**Technical Implementation:**

- **Architecture:**
  ```
  SaaS Content APIs (files, records, messages across connected apps)
      --> Content Extraction & Preprocessing
          --> AI Classification Pipeline:
              - Pattern recognition (regex + ML for structured data types)
              - Contextual analysis (ML-based classification for unstructured content)
              - Multi-label classification (same content can be PII + Financial + IP)
          --> Sensitivity Labels Applied
              --> Knowledge Graph Integration (link sensitivity labels to file/record nodes)
                  --> Permission Analysis (who has access to sensitive data?)
                      --> Risk Scoring & Exposure Alerts
  ```

- **Classification Approach:** Combines traditional pattern matching (regex for structured data like SSNs, credit card numbers) with ML-based contextual analysis for unstructured content that requires understanding context to classify correctly.
- **Processing Mode:** Real-time classification of new/modified content; batch scanning for initial deployment and periodic full-scan audits.

**Competitive Differentiation:**

- **Advantages:** Integration with the Knowledge Graph means that data classification is immediately correlated with identity, access, and behavioral context. This provides a richer risk picture than standalone DLP or data classification tools that operate in isolation.
- **Innovation Level:** Competitive. Data classification is a well-established capability, but the Knowledge Graph integration and real-time SaaS-native approach are differentiators.

---

### AI/ML Technology Stack Summary

| Technology | Type | Primary Use Case | Maturity | Competitive Edge | Key Differentiator |
|------------|------|------------------|----------|------------------|--------------------|
| Knowledge Graph / Identities Interaction Graph | Graph-based ML | Cross-app correlation, identity resolution, context enrichment | Mature (patented, 4 patents) | Cutting-edge | Patented interaction weights; foundational to all analytics |
| NLP Engine | Fine-tuned NLP | Shadow AI & SaaS discovery via email metadata | Mature (production) | Cutting-edge | Email metadata approach is uncommon in SSPM |
| Behavioral Analytics / UEBA | Supervised + Unsupervised ML | Threat detection, anomaly detection, insider threat | Mature (production) | Advanced | Knowledge Graph integration provides richer context than standalone UEBA |
| Classification Engine | Supervised ML | App discovery, AI tool identification | Mature (50,000+ apps) | Competitive | Scale (50,000+) and AI-specific classification |
| AI Agents | Autonomous AI | Alert investigation, prioritization, response | Early (1 agent GA) | Cutting-edge | First-mover in SSPM AI agents; Knowledge Graph-native |
| Sensitive Data Classification | AI-based pattern recognition | PII/PHI/IP/financial data identification | Mature (production) | Competitive | Real-time SaaS-native; Knowledge Graph integration |

---

### Overall AI/ML Assessment

**AI/ML Strengths:**

1. **Patented foundational AI architecture:** The Knowledge Graph with interaction weights is not a feature -- it is the platform's core data structure. This provides a sustainable, defensible competitive moat that competitors cannot replicate without similar architectural investment.
2. **Research-backed innovation:** CTO Tal Shapira's 14 publications and 356 citations provide genuine academic credibility. Research on self-attention mechanisms (SASA), encrypted traffic classification (ECHO), and zero-shot IoT labeling with LLMs (ZEAL) demonstrates a deep, research-informed approach to AI/ML in security.
3. **Intelligence community heritage:** The technology's origins in Israeli government counterintelligence provide a unique foundation in graph-based intelligence analysis that commercial competitors typically lack.
4. **AI-first architecture:** AI/ML is not bolted onto a legacy product -- it is the foundational architecture. This enables deeper, more coherent AI integration than competitors who add AI features to existing products.
5. **Forward-looking AI agent strategy:** The launch of AI Agents for SaaS Security and the Agentic AI Security pillar position Reco AI at the forefront of the AI-agent wave in cybersecurity.
6. **Cross-app graph correlation:** The ability to correlate signals across 225+ apps through a single Knowledge Graph is architecturally superior to per-app analysis.

**AI/ML Weaknesses:**

1. **Proprietary opacity:** The patented, proprietary nature of the Knowledge Graph and ML models means customers must trust the vendor's claims without the ability to audit or customize the underlying algorithms.
2. **AI agent maturity:** Only one AI agent (Alert Summary) is currently in production. The agent platform is promising but early-stage compared to the vision.
3. **NLP scope limitation:** The NLP-based shadow discovery is limited to Gmail and Outlook email metadata, which will not detect shadow tools that do not generate email communications.
4. **Warm-up dependency:** Behavioral analytics requires a learning period to establish baselines, meaning new deployments may have reduced detection accuracy initially.
5. **Limited public benchmarks:** Reco AI does not publish detailed accuracy/false-positive-rate benchmarks for its ML models, making independent evaluation difficult.

**Strategic AI Assessment:**

- **AI Implementation Philosophy:** AI-First -- the platform is built on AI from the ground up, not enhanced with AI as an afterthought
- **Market Position (AI Capabilities):** Leader in the SSPM category for AI depth and sophistication
- **Innovation Level:** Cutting-edge -- the patented Knowledge Graph, NLP-based shadow discovery, and AI agents represent genuine innovation
- **AI Differentiation:** The patented Knowledge Graph with interaction weights is the primary AI differentiator. No other SSPM vendor has a comparable patented graph-based analytics engine with this depth of integration.

---

## CTO Research Background & Academic Foundation

### Tal Shapira, Ph.D. -- Co-Founder & CTO

Tal Shapira's academic and professional background is central to understanding Reco AI's AI/ML capabilities. His research directly informs the platform's technology.

**Research Profile:**
- **Publications:** 14 papers
- **Citations:** 356 (ResearchGate)
- **Research Focus:** AI/ML for cybersecurity, graph analytics, network security, encrypted traffic analysis

**Key Publications:**

| Paper | Topic | Relevance to Reco AI |
|-------|-------|---------------------|
| **SASA** | IP Hijack Detection using self-attention neural network architectures | Demonstrates expertise in self-attention mechanisms for network security pattern detection; applicable to Reco AI's behavioral analytics |
| **ECHO** | Encrypted traffic classification achieving 90% latency reduction | Shows deep expertise in ML-based traffic analysis; informs Reco AI's approach to analyzing SaaS API traffic patterns |
| **ZEAL** | Zero-shot IoT device labeling using Large Language Models (LLMs) | Demonstrates cutting-edge LLM expertise; applicable to Reco AI's classification engine and potential future LLM-powered features |

**Professional Background:**
- **Former Head of Cybersecurity R&D, Israeli Prime Minister's Office:** This is the direct lineage for Reco AI's technology. The Knowledge Graph and behavioral analytics capabilities trace back to counterintelligence technology developed under Shapira's leadership.
- **AI Controls Security Working Group, Cloud Security Alliance (CSA):** Active participation in industry standards for AI security governance

**Research-to-Product Pipeline:**
Shapira's academic work demonstrates a clear pipeline from research to product:
- Self-attention mechanisms (SASA) --> Behavioral analytics pattern detection
- Traffic classification (ECHO) --> SaaS API interaction analysis
- Zero-shot labeling with LLMs (ZEAL) --> Classification Engine, potential LLM-powered features
- Graph-based intelligence analysis (government R&D) --> Patented Knowledge Graph

---

## Patents

### RECOLABS LTD. Patent Portfolio

| # | Title | Key Innovation | Relevance |
|---|-------|---------------|-----------|
| 1 | "Data Security Method Using Interaction Graphs" | Defines a method for building an interaction graph with weighted edges between entities (users, files, apps) for security analytics. The interaction weights encode the strength, frequency, and type of interaction. | Core patent for the Knowledge Graph architecture |
| 2 | "Computer Implemented Method for Securing Files" | Describes a computational method for generating interaction scores between processes/users and files. These scores are used to assess file security risk and detect anomalous file access patterns. | Core patent for data exposure management and file security analytics |
| 3 | Related interaction graph methods | Extensions and refinements of the core interaction graph technology | Broadens IP protection for the Knowledge Graph |
| 4 | Related interaction graph methods | Extensions and refinements of the core interaction graph technology | Broadens IP protection for the Knowledge Graph |

**Patent Assessment:** Four patents provide meaningful IP protection for Reco AI's core differentiator (the Knowledge Graph). The patents cover both the graph construction methodology (interaction weights, edge types) and the application of the graph for security analytics (file security, anomaly detection). This creates a defensible moat against competitors who might attempt to replicate the graph-based approach.

---

## Integration Ecosystem

### Native SaaS Integrations (225+)

**Core Productivity & Collaboration:**
- Microsoft 365 (Exchange, SharePoint, OneDrive, Teams)
- Google Workspace (Gmail, Drive, Calendar, Chat)
- Slack
- Zoom

**CRM & Business Applications:**
- Salesforce
- ServiceNow
- Jira / Atlassian Suite
- Workday
- Veeva (life sciences-specific)

**Identity & Access Management:**
- Okta
- Azure Active Directory (Entra ID)
- Google Workspace Directory

**Development Tools:**
- GitHub
- GitLab
- Cursor (200th integration milestone)
- Jira

**Security Integrations:**

| Integration Type | Products |
|-----------------|----------|
| SIEM | Splunk, and others |
| SOAR | Palo Alto XSOAR, Torq, Tines |
| Cloud Security | Wiz |
| Third-Party Risk | Black Kite |
| Asset Management | JupiterOne |

**Integration Architecture:**
- All integrations are API-based and read-only
- Average connection time: **8 minutes per app**
- No agents, proxies, or inline components required
- SaaS App Factory enables **3-5 day development** of new integrations

---

## Security & Compliance Certifications

### Reco AI Platform Certifications

| Certification | Status | Description |
|--------------|--------|-------------|
| **SOC 2 Type II** | Certified | Independent audit of security controls over an extended period |
| **ISO 27001** | Certified | International standard for information security management |
| **GDPR** | Compliant | European data protection regulation compliance |

**Trust Center:** [trust.reco.ai](https://trust.reco.ai) -- public trust center with current compliance documentation, security practices, and certifications.

### Compliance Frameworks Supported (for Customer Environments)

Reco AI's SaaS Posture Management pillar supports continuous monitoring and compliance reporting for **20+ frameworks**, including:

- SOC 2
- ISO 27001
- NIST Cybersecurity Framework (CSF)
- NIST 800-53
- CIS Benchmarks
- HIPAA
- PCI DSS
- GDPR
- CCPA/CPRA
- SOX
- FedRAMP
- And additional industry-specific frameworks

---

## Recent Updates & Milestones (2024-2025)

| Date/Period | Update | Significance |
|-------------|--------|--------------|
| 2024-2025 | Launch of AI Agents for SaaS Security | First SSPM vendor to deploy autonomous AI agents; Alert Summary Agent is the first production agent |
| 2024-2025 | Launch of Agentic AI Security / AI Agent Governance | New pillar addressing the emerging agentic AI threat surface |
| 2024-2025 | 200+ integrations milestone | Cursor was the 200th integration, demonstrating commitment to AI developer tools |
| 2025 | 225+ native integrations | Continued rapid expansion of the integration ecosystem |
| 2024-2025 | GigaOm SSPM Radar: Leader & Fast Mover | Analyst recognition as both a leader and the fastest-moving vendor in SSPM |
| 2024-2025 | SINET16 Innovator | Recognition as one of the 16 most innovative security companies |

---

## Industry Recognition

| Recognition | Source | Significance |
|-------------|--------|--------------|
| **SSPM Radar Leader** | GigaOm | Positioned as a leader in the SSPM market |
| **SSPM Radar Fast Mover** | GigaOm | Recognized for the fastest rate of innovation and improvement in the SSPM category |
| **SINET16 Innovator** | SINET | Selected as one of the 16 most innovative security companies globally |

---

## Competitive Positioning Summary

### Key Differentiators vs. SSPM Market

1. **Patented Knowledge Graph:** No other SSPM vendor has a comparable patented graph-based analytics engine. This is a structural advantage that cannot be replicated through feature additions.

2. **AI-first architecture:** Born as an AI-native platform from intelligence-community technology, not a legacy product with AI features added.

3. **Agentless simplicity:** 8-minute connection time, 80% less implementation overhead, read-only API access.

4. **Breadth:** 225+ integrations with the SaaS App Factory enabling 3-5 day new integration development.

5. **AI governance leadership:** Early mover in AI Governance, Agentic AI Security, and AI Agents for SaaS Security -- addressing the next wave of SaaS security challenges before they become critical.

6. **Research-backed:** CTO with 14 publications, 356 citations, and government counterintelligence R&D leadership. The AI is grounded in genuine research, not marketing.

---

## Sources

### Official Resources
- Reco AI Official Website: [reco.ai](https://reco.ai)
- Reco AI Trust Center: [trust.reco.ai](https://trust.reco.ai)
- AWS Marketplace Listing: Reco AI on AWS Marketplace

### Patent Records
- RECOLABS LTD. patent filings (USPTO / patent databases)
- "Data Security Method Using Interaction Graphs"
- "Computer Implemented Method for Securing Files"

### Academic Publications
- Tal Shapira, ResearchGate profile (14 publications, 356 citations)
- SASA: IP Hijack Detection with self-attention mechanisms
- ECHO: Encrypted traffic classification
- ZEAL: Zero-shot IoT labeling with LLMs

### Industry Analyst Reports
- GigaOm SSPM Radar Report (Leader & Fast Mover positioning)
- SINET16 Innovator recognition

### Industry Affiliations
- Cloud Security Alliance (CSA) -- AI Controls Security Working Group

---

## Verified Sources & References

1. [Reco AI Official Website](https://www.reco.ai)
2. [Reco AI - AI Agents for SaaS Security](https://www.reco.ai/ai-agents-for-saas-security)
3. [Reco AI - AI Usage Control](https://www.reco.ai/use-cases/ai-usage-control)
4. [Reco AI Blog - Generative AI in SaaS Security](https://www.reco.ai/blog/reimagining-contextualized-saas-security-with-generative-ai-1)
5. [Reco AI - Competitor Comparisons](https://www.reco.ai/compare)
6. [Reco AI - Top SSPM Tools Guide](https://www.reco.ai/compare/top-sspm-tools)
7. [Reco AI Newsroom](https://www.reco.ai/newsroom)
8. [GlobeNewsWire - Reco Identity-First Approach](https://www.globenewswire.com/news-release/2023/12/12/2794806/0/en/Reco-ai-Is-Changing-the-Game-of-SaaS-Security-with-Its-Identity-First-Approach-to-SaaS-Security-Posture-Management.html)
9. [Reco AI - LinkedIn](https://www.linkedin.com/company/recolabs)
10. [Tal Shapira (CTO) - LinkedIn](https://www.linkedin.com/in/tal-shapira/)
11. [Crunchbase - Reco Company Profile](https://www.crunchbase.com/organization/reco-67bb)
12. [Cyber Defense Magazine - Reco Innovator Spotlight](https://www.cyberdefensemagazine.com/innovator-spotlight-reco-ai/)
13. [CRN 2025 Stellar Startup - Reco](https://www.reco.ai/blog/reco-recognized-as-a-crn-2025-stellar-startup)
14. [Startup Nation Finder - RecoLabs](https://finder.startupnationcentral.org/company_page/recolabs)
15. [USPTO Patent Public Search](https://ppubs.uspto.gov/) — Search for assignee "RECOLABS" to find patent filings
16. [Google Patents](https://patents.google.com/) — Search for assignee "RECOLABS LTD" for patent details

*Patent numbers for RECOLABS LTD. can be verified through USPTO Patent Public Search (ppubs.uspto.gov) or Google Patents. The 4 patents referenced in this report cover the Identities Interaction Graph technology.*

*All URLs verified as of February 2026.*