# SAI SRIKANTH — GC MASTER RESUME SOURCE
# ================================================
# PURPOSE: Source of truth for the Writer Agent when job_type = "gc"
# Identity: Sai Srikanth (different from Contract/Fulltime identity)
# Experience: 10 years (Aug 2016 - Present)
# Companies: 5 (Cardinal Health, UBS, MTA, Cognizant, Couth InfoTech)
# ================================================

---

## CONTACT INFO
- Full Name: Sai Srikanth
- Email: saisrikanth4676@gmail.com
- Phone: +1(469) 319-1541
- Location: (not shown on resume)

---

## CLOUD PLATFORM ASSIGNMENT (FIXED FOR GC)
# ================================================
# GC resumes span 10 years and 5 companies across all 3 clouds.
# Each company has a FIXED cloud — do not change these assignments.
#
#   Cardinal Health  → Azure (healthcare, current)
#   UBS              → Azure + Snowflake (finance)
#   MTA              → GCP (public sector)
#   Cognizant        → AWS (telecom)
#   Couth InfoTech   → AWS (early career)
#
# CLOUD ADAPTATION FOR GC:
# Unlike Contract/Fulltime, GC resumes already cover all 3 clouds naturally.
# If the JD emphasizes a specific cloud, PRIORITIZE that cloud's company
# in bullet selection — give it more bullets and place its experience
# more prominently. But do NOT swap clouds between companies.
#
# If the JD heavily emphasizes Azure: expand Cardinal Health and UBS bullets.
# If the JD heavily emphasizes AWS: expand Cognizant bullets and add AWS depth.
# If the JD heavily emphasizes GCP: expand MTA bullets and add GCP depth.
# ================================================

### Azure Services (Cardinal Health, UBS)
Azure OpenAI, Azure AI Search, Azure Data Factory, Azure Data Lake, Azure ML, Azure Event Hubs, Azure DevOps, Azure Synapse, Azure Monitor, Azure Key Vault

### GCP Services (MTA)
BigQuery, Dataproc, Cloud Storage, Pub/Sub, Cloud Composer (Airflow), Data Catalog, Cloud Functions, Cloud Monitoring

### AWS Services (Cognizant, Couth InfoTech)
S3, EC2, EMR, Kinesis, Athena, RDS, Lambda, CloudWatch, IAM, Glue

### Cross-Platform Tools
Databricks, Apache Spark, PySpark, Snowflake, Apache Airflow, Kafka, Delta Lake, Docker, Kubernetes, Terraform, Jenkins, GitHub Actions, MLflow, Power BI, Tableau

---

## WORK EXPERIENCE

### ═══════════════════════════════════════════════════
### COMPANY 1: CARDINAL HEALTH — Dublin, OH
### Role: Senior AI/ML Engineer / Data Engineer
### Dates: November 2024 to Present
### Cloud: Azure
### Domain: Healthcare
### ═══════════════════════════════════════════════════

#### CORE EXPERIENCE

- Architected enterprise Generative AI platforms using Azure OpenAI and RAG to enable clinical decision support and real-time knowledge retrieval across care management systems
- Designed scalable vector-based retrieval systems using Azure AI Search and transformer embeddings to support semantic search across clinical and claims data
- Built PyTorch-based NLP pipelines to extract structured clinical entities from unstructured medical documents enabling downstream analytics and care workflows
- Developed real-time AI inference services delivering summaries, recommendations, and insights to care-management and call-center applications
- Implemented prompt engineering frameworks and retrieval validation techniques to reduce hallucinations and ensure explainable AI outputs
- Established observability pipelines tracking model performance, latency, response quality, and embedding drift using Azure Monitor
- Engineered large-scale ingestion pipelines using Azure Data Factory and Databricks to process healthcare datasets from multiple source systems
- Designed Delta Lake data models supporting claims, pharmacy, provider, and patient data for analytics and ML use cases
- Integrated streaming architectures using Azure Event Hubs enabling near real-time ingestion and AI inference
- Implemented HIPAA-compliant data security controls including masking, tokenization, and role-based access mechanisms
- Built feature engineering pipelines combining clinical and financial data for predictive modeling and decision support systems
- Managed full lifecycle of ML and LLM systems including versioning, deployment, monitoring, and rollback strategies
- Optimized Spark workloads using partitioning and caching strategies for high-throughput data processing
- Collaborated with clinicians and compliance teams to validate AI models and ensure regulatory alignment

#### PROJECT: CLINICAL AI DECISION SUPPORT PLATFORM
- RAG-based clinical Q&A system using Azure OpenAI for answer generation and Azure AI Search for vector retrieval
- Processes clinical documents (discharge summaries, care plans, formulary data) through chunking and embedding pipeline
- PyTorch NLP models extract ICD codes, drug names, and clinical entities from unstructured text
- Real-time inference APIs serve care managers with summarized patient insights and treatment recommendations
- Delta Lake on Databricks serves as the unified data layer combining claims, pharmacy, and clinical data
- HIPAA-compliant architecture with data masking, tokenization, audit logging, and RBAC

---

### ═══════════════════════════════════════════════════
### COMPANY 2: UBS — Weehawken, NJ
### Role: Big Data Engineer / ML Engineer
### Dates: February 2023 to October 2024
### Cloud: Azure + Snowflake
### Domain: Financial Services
### ═══════════════════════════════════════════════════

#### CORE EXPERIENCE

- Designed and implemented financial data platforms using Azure Data Lake, Databricks, and Snowflake supporting fraud detection and compliance analytics
- Built real-time ingestion pipelines using Azure Event Hubs and batch pipelines using Data Factory for transaction data processing
- Developed PySpark pipelines to cleanse, standardize, and enrich financial datasets for analytics and ML consumption
- Designed Snowflake schemas and data marts supporting fraud monitoring, risk analytics, and regulatory reporting
- Engineered feature pipelines generating behavioral and transactional features for fraud detection models
- Integrated Azure Machine Learning pipelines for model training, scoring, and deployment into production systems
- Built transaction scoring systems generating risk scores and decision flags for fraud detection workflows
- Implemented monitoring solutions for model performance and data drift detection ensuring reliability
- Optimized Spark and Snowflake performance using clustering, partitioning, and caching strategies
- Enforced data security using RBAC, encryption, and masking policies aligned with PCI compliance
- Developed dashboards using Power BI and Tableau for fraud analysis and executive reporting
- Orchestrated pipelines using Apache Airflow ensuring reliable execution across workflows
- Implemented CI/CD pipelines using Git and Azure DevOps for automated deployment of data and ML systems
- Collaborated with risk and compliance teams to align analytics with business and regulatory requirements

#### PROJECT: FRAUD DETECTION AND RISK ANALYTICS PLATFORM
- Real-time transaction scoring system processing financial events through Azure Event Hubs
- Feature engineering pipeline generates 50+ behavioral features from transaction history
- ML models trained on Azure ML for fraud classification with automated retraining on data drift
- Snowflake data marts provide historical fraud patterns for compliance reporting
- Databricks handles large-scale batch processing for daily risk aggregation
- PCI-compliant architecture with encryption, masking, and role-based access

---

### ═══════════════════════════════════════════════════
### COMPANY 3: MTA (Metropolitan Transportation Authority) — New York, NY
### Role: Senior Data Engineer
### Dates: September 2019 to January 2023
### Cloud: GCP
### Domain: Public Sector / Transportation
### ═══════════════════════════════════════════════════

#### CORE EXPERIENCE

- Built GCP-based data platforms using Cloud Storage and BigQuery to consolidate multi-agency datasets
- Designed ingestion pipelines extracting and loading data from legacy systems into cloud-based storage
- Developed PySpark pipelines on Dataproc for data transformation and integration across agencies
- Implemented metadata management and lineage tracking using Data Catalog for governance
- Built analytics-ready datasets in BigQuery supporting compliance and policy reporting
- Enabled real-time ingestion using Pub/Sub and Kafka for event-driven data processing
- Optimized BigQuery performance using partitioning and clustering techniques
- Implemented data validation and reconciliation frameworks ensuring data accuracy
- Enforced IAM-based access control for secure data sharing across departments
- Automated workflows using Cloud Composer (Airflow) for orchestration
- Developed dashboards using Power BI and Tableau for operational insights
- Collaborated with stakeholders to standardize data definitions and KPIs
- Maintained documentation supporting audits and compliance processes
- Implemented CI/CD pipelines for ETL deployment and workflow automation

#### PROJECT: MULTI-AGENCY DATA CONSOLIDATION PLATFORM
- Unified data platform consolidating ridership, operations, and financial data from multiple transit agencies
- GCP-native architecture with Cloud Storage for landing zone, Dataproc for processing, BigQuery for analytics
- Real-time event processing through Pub/Sub and Kafka for operational monitoring
- Data Catalog provides metadata management and lineage tracking for governance compliance
- Cloud Composer orchestrates daily ETL workflows across agency data sources
- IAM-based security model with department-level access controls

---

### ═══════════════════════════════════════════════════
### COMPANY 4: COGNIZANT TECHNOLOGY SOLUTIONS — Bangalore, India
### Role: Data Engineer
### Dates: April 2018 to June 2019
### Cloud: AWS
### Domain: Telecom
### ═══════════════════════════════════════════════════

#### CORE EXPERIENCE

- Designed AWS-based data lake solutions using S3 to process telecom data including call detail records and network events
- Built ingestion pipelines using Kinesis and Airflow for batch and streaming data processing
- Developed Spark-based processing pipelines on EMR for large-scale telecom datasets
- Structured datasets using Parquet and partitioning for performance optimization
- Built aggregation pipelines generating telecom KPIs for analytics and reporting
- Enabled SQL querying using Athena and Hive external tables
- Implemented data validation frameworks ensuring data consistency
- Optimized Spark workloads using partition pruning and join strategies
- Secured data using IAM policies and encryption mechanisms
- Delivered datasets supporting fraud detection and churn analytics
- Automated deployment workflows using Jenkins and Git
- Collaborated with engineering teams to validate metrics and reporting outputs
- Maintained documentation and runbooks for production systems
- Supported regulatory and operational reporting requirements

---

### ═══════════════════════════════════════════════════
### COMPANY 5: COUTH INFOTECH PVT. LTD — Hyderabad, India
### Role: Associate Data Engineer
### Dates: August 2016 to March 2018
### Cloud: AWS
### Domain: IT Services
### ═══════════════════════════════════════════════════

#### CORE EXPERIENCE

- Built foundational AWS data pipelines using S3, EC2, and RDS to centralize telemetry and operational datasets
- Developed Python-based ETL pipelines for processing structured and semi-structured data
- Implemented batch workflows for aggregating operational and usage data
- Designed relational data models supporting reporting and analytics
- Optimized SQL queries and indexing strategies for performance improvements
- Implemented data-quality validation checks ensuring data accuracy
- Managed secure access using IAM roles and policies
- Supported reporting and analytics using SQL-based queries
- Collaborated with infrastructure teams for data validation and monitoring
- Maintained documentation for ETL processes and workflows
- Automated batch workflows for daily data processing tasks
- Developed scripts for data cleansing and transformation
- Supported hybrid-cloud data integration initiatives
- Ensured operational stability of data pipelines

---

## TECHNICAL SKILLS INVENTORY

### Programming
Python, SQL, PySpark

### AI/ML
PyTorch, Transformers, NLP, Feature Engineering, Model Training and Inference

### Generative AI
LLMs, RAG, Prompt Engineering, Vector Embeddings, Semantic Search

### MLOps/LLMOps
MLflow, CI/CD, Model Monitoring, Drift Detection, Versioning

### Data Engineering
Spark, Databricks, ETL/ELT, Data Lakes, Lakehouse Architecture, Delta Lake

### Cloud Platforms
Azure (Data Factory, Data Lake, OpenAI, AI Search, ML, Event Hubs, DevOps, Synapse), AWS (S3, EC2, EMR, Kinesis, Athena, RDS, Lambda), GCP (BigQuery, Dataproc, Cloud Storage, Pub/Sub, Cloud Composer, Data Catalog)

### Databases
Snowflake, BigQuery, Synapse, RDS, Firestore

### Streaming
Kafka, Kinesis, Event Hubs, Pub/Sub

### Orchestration
Apache Airflow, Cloud Composer

### DevOps
Docker, Kubernetes, Terraform, Jenkins, GitHub Actions

### BI Tools
Power BI, Tableau

### Governance and Security
Data Catalog, Lineage, RBAC, Encryption, Compliance (HIPAA, PCI)

---

## WRITER AGENT INSTRUCTIONS (GC MODE)
# ================================================
# 1. READ THE JD FIRST — identify required skills, tools, and cloud platform
# 2. SELECT RELEVANT BULLETS — pick bullets that match JD keywords
# 3. CLOUD IS FIXED — do NOT swap clouds between companies. Cardinal Health = Azure, UBS = Azure, MTA = GCP, Cognizant = AWS, Couth InfoTech = AWS
# 4. EMPHASIZE BY JD — if JD emphasizes a specific cloud, give MORE bullets to that cloud's company
# 5. ADAPT TOOLS — if JD mentions Airflow, Databricks, Snowflake etc, use them where they fit
# 6. PRIORITIZE RECENT — Cardinal Health and UBS are primary, MTA is secondary, Cognizant and Couth are supporting
# 7. DO NOT INVENT — only use experience listed in this file
# 8. MATCH JD LANGUAGE — mirror the JD's terminology
# 9. CHRONOLOGY — GenAI/LLM/RAG only in Cardinal Health (2024+). UBS can have ML but not GenAI. MTA, Cognizant, Couth are pure data engineering.
# 10. PROJECT ASSIGNMENT — each company has ONE project context, do not mix
# 11. SKILLS FORMAT — use the categories shown in Technical Skills Inventory above
# ================================================
