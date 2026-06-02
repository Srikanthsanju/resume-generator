# SRIKANTH MANCHIMCHETTY — RESUME MASTER SOURCE WITH ROLE LANES

Purpose: This file is the single source of truth for the resume writer agent. The writer must read the Job Description first, classify the target role, select the correct role lane, apply cloud and tool substitutions, then generate a believable ATS optimized resume.

This file is intentionally large. The goal is high ATS coverage without role drift. The writer must not pull every impressive AI skill into every resume. The writer must use only the role lane that matches the JD.

---

## CONTACT INFO

Full Name: Srikanth Manchimchetty  
Email: mvss.1998@gmail.com  
Phone: +1(940)703-0146  
LinkedIn: www.linkedin.com/in/srikanthmanchimchetty  
Location: Dallas, TX, USA  
GitHub: https://github.com/Srikanthsanju

---

# 1. JD CLASSIFICATION OUTPUT REQUIRED BEFORE WRITING

The backend must classify the JD before the writer generates the resume. This classification is not a decoration. It is the routing plan for the entire resume.

Required editable classification card:

Primary Role:
Secondary Role:
Role Family:
AI Intensity:
Cloud Environment:
Data Platform:
Backend Environment:
Domain Context:
Required Skills:
Preferred Skills:
Top 10 ATS Keywords:
Must-Prove Skills:
Resume Strategy:
Skills to Emphasize:
Skills to Suppress:
Forbidden Drift Terms:
Evidence Plan:
Interview Risk Notes:

Allowed Primary Role values:
AI Engineer
ML Engineer
Data Scientist
Data Engineer
Python Developer
Software Engineer
Backend Engineer
Platform Engineer
Analytics Engineer
Business Intelligence Engineer

Allowed Role Family values:
AI Platform
ML Platform
Data Platform
Backend Platform
Analytics
BI and Reporting
Healthcare Technology
FinTech or Banking
General Software Engineering

Allowed AI Intensity values:
Level 0: No AI
Level 1: Light ML or analytics only
Level 2: ML focused
Level 3: GenAI or RAG focused
Level 4: Agentic AI focused

AI intensity selection rule:
Do not decide AI intensity from the candidate's projects. Decide it from the JD.
If the JD title or responsibilities explicitly mention AI agents, LLMs, GenAI, LangChain, LlamaIndex, RAG, vector databases, embeddings or prompt workflows, set AI Intensity to Level 3 or Level 4 even when the title is Python Engineer or Software Engineer.
If the JD is Data Engineer, Analytics Engineer, BI Engineer or pure Backend Engineer and only mentions Python, SQL, cloud, APIs, Spark, ETL or dashboards, set AI Intensity to Level 0 or Level 1.

Evidence Plan format:
For every required skill, the classifier must decide where it will appear:
Skill:
Summary mention: Yes or No
Skills section mention: Yes or No
Experience proof bullet: Bee Data, Allied, BYJU'S, Cognizant or Not Supported
Project lane:
Risk level: Low, Medium or High

Writer rule:
The writer must not generate the resume until Primary Role, AI Intensity, Cloud Environment and Evidence Plan are selected.
The writer must treat the selected role lane as the main source. Secondary Role may contribute only 1 or 2 supporting bullets per recent role.
The writer must never pull a skill only because it is impressive. The skill must be required by the JD, preferred by the JD or needed to make the selected role believable.

JD reading rule:
The writer must identify the actual job being hired for, not just the title.
Example: A "Python Engineer" JD that asks for AI agent logic, LangChain, state persistence and long-running tasks is a Backend AI Platform role, not a generic Python API role.
Example: A "Data Engineer" JD that asks for Spark, Airflow, BigQuery and ETL is a Data Platform role, not an AI Engineer role.
Example: A "Data Scientist" JD that asks for forecasting, experimentation, regression and business insights is an analytical modeling role, not an MLOps engineer role.

---

# 2. ROLE WEIGHT RULES

The writer must use these weights when selecting bullets. These are responsibility weights, not keyword stuffing weights. A resume should sound like the role being hired for.

AI Engineer:
55% GenAI, LLM, RAG, agents, prompt engineering, embeddings, safety, evaluation or model serving
20% backend, APIs and platform services
15% MLOps, deployment and monitoring
10% data pipelines and storage

ML Engineer:
45% model training, evaluation, deployment, monitoring, drift and MLOps
25% feature engineering and data preparation
20% backend APIs and serving
10% cloud infrastructure

Data Scientist:
45% modeling, experimentation, statistical analysis, scoring logic and metrics
30% feature engineering, data preparation and business analysis
15% Python, SQL and reporting
10% deployment or automation only if JD asks

Data Engineer:
55% ingestion, ETL, ELT, orchestration, Spark, warehouse, data quality and monitoring
25% cloud data platforms and storage
15% Python automation and backend integration
5% AI or ML only if JD explicitly asks

Python Developer or Software Engineer:
50% Python backend, APIs, services, databases, async processing, authentication and testing
25% cloud deployment, containers, observability and reliability
15% data processing, integrations or automation
10% AI framework integration only if JD explicitly asks

Python Engineer with AI Agent JD:
40% Python backend APIs, FastAPI, Django, auth, databases and async processing
25% AI agent backend infrastructure, LangChain or LlamaIndex integration, state persistence and workflow routing
20% cloud, containers, API Gateway, task queues and observability
15% SQL, NoSQL, vector databases and service reliability

Backend Engineer:
60% APIs, microservices, databases, auth, async workflows, reliability and observability
20% cloud and containers
15% data processing
5% ML or AI only if JD explicitly asks

Platform Engineer:
45% Kubernetes, CI/CD, observability, scalable services and cloud operations
25% backend platform APIs
20% data or ML platform workflows
10% governance, security and reliability

Analytics Engineer or BI Engineer:
45% SQL, warehouse modeling, dashboards and stakeholder reporting
30% ETL, data quality and transformation workflows
15% Python automation
10% statistics or ML only if JD asks

Hybrid role rule:
If a JD combines two role families, select one Primary Role and one Secondary Role. The Primary Role must drive the summary, skills order and first 5 bullets of the latest role.
Examples:
Python Engineer + AI agents = Primary Role Python Developer, Secondary Role AI Engineer, AI Intensity Level 4
Data Engineer + ML pipelines = Primary Role Data Engineer, Secondary Role ML Engineer, AI Intensity Level 2
Data Scientist + MLOps deployment = Primary Role Data Scientist, Secondary Role ML Engineer, AI Intensity Level 2

---

# 3. ROLE DRIFT CONTROL RULES

Role drift means the resume sounds like a different job than the JD. High ATS score is useless if the recruiter feels the resume is not believable for the role.

If Primary Role is Data Engineer:
Avoid RAG, prompt engineering, LangGraph, GPT-4, Claude, LoRA, fine-tuning, agentic workflows and vector databases unless the JD explicitly mentions GenAI, LLM, RAG, embeddings or agents.
Use pipeline, ingestion, transformation, orchestration, Spark, Airflow, Databricks, Snowflake, BigQuery, data quality, warehouse, monitoring, batch processing and cloud storage.
Allowed AI wording for Data Engineer: "ML features", "scoring outputs", "embedding generation" or "model input datasets" only when the JD mentions ML or AI data pipelines.

If Primary Role is Python Developer or Software Engineer:
Do not lead with ML models, RAG, fine-tuning or prompt engineering.
Use FastAPI, Django, REST APIs, async services, Pydantic, Celery, authentication, PostgreSQL, Redis, Docker, Kubernetes, CI/CD, logging, monitoring and service reliability.
If the JD explicitly asks for AI agents, LangChain, LlamaIndex, vector databases or AI frameworks, describe AI as backend infrastructure. Use words like "agent workflow orchestration", "state persistence", "long-running tasks", "tool integration" and "routing logic". Do not sound like an AI researcher.

If Primary Role is Data Scientist:
Avoid sounding like only a pipeline engineer.
Use feature engineering, model evaluation, classification, regression, scoring, experimentation, thresholds, accuracy, precision, recall, business outcomes and trend analysis.
Use cloud and API content only as supporting context.

If Primary Role is ML Engineer:
Avoid only dashboard or BI language.
Use model training, deployment, feature pipelines, inference APIs, MLflow, drift monitoring, experiment tracking, model registry, retraining and scalable serving.
If GenAI is not in the JD, keep LLM wording minimal.

If Primary Role is AI Engineer:
Use GenAI terms only when AI is central to the title or responsibilities.
Use RAG, LangChain, LangGraph, LlamaIndex, GPT, Claude, embeddings, vector databases, prompt evaluation, safety, guardrails and human-in-the-loop review.
Still keep backend, monitoring and production reliability visible so the resume does not sound like only prompt writing.

Final validation:
The scorer must calculate Role Drift Score before final output.
If target role is Data Engineer and the resume has more than 2 GenAI terms in the latest experience, flag it for rewrite unless the JD explicitly asks for GenAI.
If target role is Python Developer and the JD does not mention AI frameworks, the resume must not have more AI than backend/API language.
If target role is Python Engineer and the JD explicitly asks for AI agent logic, LangChain or LlamaIndex, AI backend bullets are allowed but must be written as software engineering responsibilities.
If target role is Data Scientist and the resume does not mention analysis, modeling, metrics or feature engineering, flag it for rewrite.

# 3A. JD RESPONSIBILITY TRANSLATION RULES

The writer must translate each project into the responsibilities of the JD instead of copying project descriptions.

Do not write:
"Built RAG chatbot using LangChain and Claude"
when the JD is Data Engineer.

Write:
"Built document ingestion and indexing pipelines that transformed policy PDFs into searchable structured datasets with metadata, validation and scheduled refresh jobs."

Do not write:
"Built AI agent workflow with LangGraph"
when the JD is Python Engineer unless the JD asks for AI agents.

Write:
"Built backend workflow orchestration for long-running AI tasks with state persistence, async workers, Redis and PostgreSQL."

Do not write:
"Used AWS services"
when the JD asks for GCP.

Write:
"Built cloud data workflows using Cloud Storage, Cloud SQL, Pub/Sub and Cloud Monitoring" only if GCP was selected and mapped.

Required skill proof rule:
Every required skill in the JD must be handled in one of four ways:
1. Proven in a bullet with specific responsibility
2. Listed in skills and supported indirectly by related experience
3. Marked as exposure only
4. Suppressed because it is unsupported or risky

Never list a required skill only in Skills if it is central to the JD. Central skills must appear in experience bullets.

Interview safety rule:
If a skill is included in a bullet, the bullet must be specific enough to answer follow-up questions.
Bad: "Worked on authentication"
Good: "Implemented OAuth2 and OpenID Connect flows with JWT validation, token expiration handling and role-based access controls."

---

# 4. CLOUD AND TOOL ADAPTABILITY RULES

One cloud per company rule:
Each company in the generated resume must use one cloud ecosystem only. Do not mix AWS, Azure and GCP inside the same role.

Default cloud assignment:
Bee Data Technologies: AWS
Allied Health Agency: AWS
BYJU'S: GCP
Cognizant: On premise and SQL Server

Cloud selection logic:
If the JD lists AWS, Azure and GCP equally, keep AWS for Bee Data and Allied Health.
If the JD strongly emphasizes GCP, switch Bee Data to GCP and keep BYJU'S as GCP.
If the JD strongly emphasizes Azure or Microsoft environment, switch Bee Data to Azure. Allied Health may remain AWS unless the JD is heavily Microsoft focused.
If the JD asks for Microsoft environment, prefer Azure, Azure ML, AKS, Azure Data Factory, Synapse, Azure SQL or Azure Database for PostgreSQL, Azure OpenAI Service, Azure Monitor, Entra ID and Power BI when relevant.

AWS to Azure map:
SageMaker: Azure Machine Learning
EKS: AKS
EC2: Azure Virtual Machines
S3: Azure Blob Storage
RDS PostgreSQL: Azure Database for PostgreSQL
Lambda: Azure Functions
AWS Transcribe: Azure Speech Services
AWS Textract: Azure AI Document Intelligence
AWS Bedrock: Azure OpenAI Service
CloudWatch: Azure Monitor
Cognito: Entra ID or Azure AD B2C
DynamoDB: Cosmos DB
KMS: Azure Key Vault
EMR Spark: Azure Synapse Spark or HDInsight
Kinesis: Azure Event Hubs
Step Functions: Azure Durable Functions
API Gateway: Azure API Management

AWS to GCP map:
SageMaker: Vertex AI only if JD explicitly requires Vertex AI or GCP ML platform
EKS: GKE
EC2: Compute Engine
S3: Cloud Storage
RDS PostgreSQL: Cloud SQL for PostgreSQL
Lambda: Cloud Functions
AWS Transcribe: Google Speech-to-Text
AWS Textract: Google Document AI
AWS Bedrock: Vertex AI Model Garden only if JD explicitly requires it
CloudWatch: Cloud Monitoring and Cloud Logging
Cognito: Identity Platform or Firebase Auth
DynamoDB: Firestore
KMS: Cloud KMS
EMR Spark: Dataproc
Kinesis: Pub/Sub
Step Functions: Cloud Workflows
API Gateway: API Gateway or Cloud Endpoints

Cloud rewrite discipline:
Do not blindly convert every cloud service when the JD mentions a cloud once.
Switch cloud only when the selected Cloud Environment says so.
When switching cloud, keep the responsibility the same and replace only the infrastructure nouns.
If the replacement sounds unrealistic or unsupported, use cloud-neutral wording such as object storage, managed PostgreSQL, API gateway, container orchestration, cloud monitoring or serverless functions.

Cloud consistency check:
Each company must use one cloud family in Work Experience and the Skills section.
If Bee Data is rewritten as GCP, do not mention AWS services in Bee Data bullets or Bee Data environment.
If Allied Health remains AWS, do not add GCP services to Allied Health just because GCP appears in the JD.
BYJU'S may remain GCP because the truth base already supports GCP.

Data tool substitutions:
If JD asks Airflow, replace Kubeflow orchestration references with Airflow for data pipelines.
If JD asks Databricks, replace Spark or EMR references with Databricks and Delta Lake.
If JD asks Snowflake, use Snowflake for warehouse workloads instead of BigQuery or Redshift.
If JD asks BigQuery, use BigQuery and Dataproc for GCP roles.
If JD asks Microsoft data stack, use Azure Data Factory, Synapse, Azure SQL and Power BI.
If JD asks Kafka, replace Redis Streams or Kinesis with Kafka only in event streaming contexts.
If JD asks dbt, mention dbt only for transformation and semantic modeling work.
If JD asks MLflow, use MLflow. If JD asks Weights & Biases, mention it only if explicitly required.

---

# 5. COMPANY 1: BEE DATA TECHNOLOGIES — ATLANTA, GA

Default role title: AI Engineer
Default cloud: AWS
Primary projects: P1 AI Application Intelligence Platform, P2 Multi-Platform AI Writing Assistant

## COMPANY TRUTH BASE

Bee Data Technologies work centered on AI enabled career technology products. The work included backend services, document processing, scoring systems, AI rewriting workflows, job matching, voice mock interview support, cross platform writing assistance, cloud deployment, monitoring and production API integration.

Use Bee Data as the strongest recent role for AI Engineer, ML Engineer, Python Developer and Platform Engineer roles.
For Data Engineer roles, describe Bee Data as data platform and pipeline engineering around document ingestion, parsing, metadata processing, batch scoring and cloud data workflows.

## BEE DATA CORE BULLET BANK BY ROLE

### Bee Data Lane: AI Engineer

Built production GenAI services for a career intelligence platform using FastAPI, GPT based APIs, LangChain, vector retrieval and cloud hosted model workflows.
Designed RAG style retrieval flows that injected relevant resume, job description and skill context into controlled prompts to reduce hallucinated resume suggestions.
Created prompt templates with structured JSON outputs, few shot examples and validation rules to support section level resume rewriting.
Built agentic workflows that coordinated resume parsing, job matching, scoring and interview preparation through multi step reasoning patterns.
Integrated embeddings and vector search for semantic job matching across resumes and job descriptions serving 5,000+ users.
Fine tuned LLM adapters using Hugging Face PEFT and LoRA to improve resume enhancement quality by 30% while reducing inference costs.
Created evaluation workflows that compared generated resume sections against JD requirements, keyword coverage, semantic relevance and hallucination risk.
Implemented AI service guardrails including schema validation, fallback responses, confidence thresholds and human review paths for low confidence recommendations.
Partnered with product and research stakeholders to turn model experiments into production ready AI features across sprint releases.

### Bee Data Lane: ML Engineer

Built ML pipeline architecture for resume scoring, job matching and interview feedback workflows using Python, SageMaker, MLflow and cloud deployment services.
Designed batch and real time inference paths separating high volume overnight scoring from low latency FastAPI endpoints.
Created feature engineering pipelines that extracted skills, job titles, experience signals, keywords, document sections and semantic similarity features from resumes and JDs.
Managed experiment tracking with MLflow by logging training runs, parameters, metrics, artifacts and model versions across scoring model iterations.
Implemented model promotion workflows across development, staging and production using evaluation thresholds and rollback ready model registry practices.
Trained custom scoring models using SageMaker with hyperparameter tuning and spot instances to reduce training cost.
Monitored prediction drift, score distribution shifts and quality signals to trigger retraining workflows when model performance degraded.
Built dataset versioning and reproducibility controls so each model run could be traced back to the source training data snapshot.
Exposed model endpoints through FastAPI with request validation, authentication, structured logging and error handling.

### Bee Data Lane: Data Engineer

Built document ingestion pipelines using pdfplumber for text-based resumes with AWS Textract as OCR fallback for scanned uploads processing mixed-format documents into normalized metadata tables in PostgreSQL.
Designed ETL workflows that extracted resume sections, skills, job titles, education and experience dates from raw document uploads transforming unstructured content into structured relational records for downstream scoring and matching systems.
Created batch processing jobs using Python and PySpark on EMR to process high-volume resume and job listing datasets performing deduplication, skill normalization and embedding generation for analytics and search workflows.
Implemented data quality validation checks for malformed PDF uploads, empty text extractions, duplicate resume profiles, missing required fields and failed OCR processing jobs ensuring reliability of downstream scoring pipelines.
Designed data storage architecture using S3 for raw resume and job description documents with RDS PostgreSQL for parsed metadata, user profiles, processing status, scoring outputs and activity history.
Built automated job data ingestion pipelines from RapidAPI with SerpAPI as fallback provider implementing retry logic, rate limiting and normalized schemas to maintain fresh job matching datasets.
Created monitoring dashboards for document parsing failure rates, batch processing latency, job ingestion freshness, data quality exception counts and pipeline throughput supporting operational visibility.
Optimized PostgreSQL queries and indexing strategies for resume lookup, scoring history retrieval, skill-based search and job match result pagination reducing query response times for user-facing features.
Built reusable data models for resume profiles, extracted skills, work history records, job posting metadata, ATS scoring results and user interaction events supporting analytics and reporting requirements.
Designed event-driven data workflows using S3 event triggers and Lambda functions for real-time document processing on new uploads with scheduled batch jobs for full dataset reconciliation and consistency checks.

### Bee Data Lane: Data Scientist

Developed hybrid ATS scoring logic combining TF-IDF keyword matching with semantic embedding similarity and structured resume feature signals to rank job-resume alignment across 5,000+ user profiles.
Engineered features from parsed resume sections including skill coverage ratios, job title similarity scores, keyword density, years of experience overlap, section completeness and JD requirement match percentages.
Analyzed false positive and false negative scoring cases using confusion matrix analysis and threshold tuning to improve ranking precision for borderline resume-job matches.
Created model evaluation workflows comparing keyword-only, semantic-only and hybrid scoring strategies across relevance metrics using cross-validation and held-out test sets with Python and Scikit-learn.
Built explainability outputs that highlighted matched skills, missing JD requirements, weak resume sections and high-value rewrite opportunities providing actionable insights for user-facing recommendations.
Profiled parsed resume datasets using Pandas and NumPy to validate feature distributions, detect data quality anomalies and test scoring model behavior across different role categories and experience levels.
Designed evaluation datasets for ATS score calibration using manually reviewed resume-to-JD alignment examples ensuring scoring consistency across job types and industries.
Performed statistical analysis on scoring outcomes to measure correlation between resume structure, skill phrasing, section completeness and recruiter callback rates informing product improvements.

### Bee Data Lane: Python Developer or Software Engineer

Developed async FastAPI services handling resume upload, document parsing, ATS scoring, resume rewriting, job matching and user profile management workflows with sub-100ms P95 latency for 10,000+ daily API requests.
Built Django admin dashboards and ORM-backed modules for internal operations, user management and metadata review screens connected to PostgreSQL reducing internal tooling development time.
Built backend API contracts connecting React TypeScript frontend components with document processing services, scoring endpoints, PostgreSQL storage and S3 document retrieval through versioned REST interfaces.
Implemented Pydantic schemas for request validation, structured response models and consistent error handling across 15+ service endpoints reducing integration bugs with frontend development team.
Designed modular Python service layers separating parsing, scoring, rewriting, job ingestion, interview feedback and user profile operations into independently testable modules with clear dependency boundaries.
Implemented OAuth2 and OpenID Connect authentication flows with JWT token validation, token expiration handling and role-based access controls protecting backend APIs and user data across internal and external consumers.
Built Celery task queues with Redis broker for long-running document parsing, batch scoring and analytics aggregation jobs implementing task chains, dead letter queues, progress tracking and timeout handling for reliable async processing.
Built WebSocket connections for real-time typing suggestions in the writing assistant with sub-50ms latency and SSE streaming endpoints for long-running response delivery with automatic reconnection fallback.
Created retry logic, timeout handling and graceful fallback paths for external API dependencies including job data providers, LLM services and document OCR processing ensuring service resilience under provider outages.
Containerized backend services using Docker multi-stage builds and deployed on AWS EKS with Kubernetes pod autoscaling, health checks and rolling deployments achieving 99.5% uptime.
Optimized PostgreSQL connection pooling, query execution plans and indexing strategies for user profile retrieval, scoring history lookup and job match pagination reducing database load by 40%.
Stored session and cache data in Redis with TTL-based expiration and used MongoDB for flexible document-oriented storage of parsed resume structures and job posting metadata where schema variability required NoSQL flexibility.
Designed API Gateway routing and internal service communication patterns enabling independent scaling of document processing, scoring and user management services without tight cross-service coupling.

NOTE FOR WRITER: For pure Python/SE roles, limit AI-related bullets to maximum 2 across the entire resume. If the JD explicitly asks for AI agent logic, LangChain, LlamaIndex, vector databases or workflow orchestration, allow 3 to 5 AI-backend bullets across recent roles, but write them as backend responsibilities around APIs, state persistence, task queues, routing and reliability. Do not lead with model training, prompt engineering or fine-tuning unless the JD asks.

### Bee Data Lane: Platform Engineer

Configured Kubernetes based deployment workflows for backend services, model endpoints and asynchronous processing workers.
Built CI/CD pipelines using GitHub Actions to validate, package and deploy FastAPI services and ML workflow components.
Implemented cloud monitoring dashboards for API latency, error rates, job processing failures, model endpoint health and infrastructure utilization.
Designed autoscaling strategies for API services and worker queues to handle spikes in resume uploads and job matching requests.
Created environment promotion workflows for development, staging and production with rollback procedures and configuration management.
Implemented secrets management, access controls and audit logging for cloud storage, databases and external API credentials.
Supported production incident response by improving logs, traces, metrics and failure isolation across platform services.

---

# PROJECT P1: AI APPLICATION INTELLIGENCE PLATFORM

Company: Bee Data Technologies
Project type: Resume intelligence, ATS scoring, resume tailoring, job matching and voice mock interview support
Architecture: User to React frontend to FastAPI backend to document processing to scoring services to model or LLM APIs to vector database and storage
Business outcome: Improved resume tailoring quality, enabled ATS scoring, supported semantic job matching and served 5,000+ users

## P1 Truth Base

The platform parsed resumes and job descriptions, extracted structured information, scored ATS alignment, generated resume improvement recommendations, supported resume rewriting and provided voice mock interview workflows.
Core components included React TypeScript frontend, FastAPI backend, pdfplumber, AWS Textract fallback, keyword filtering, GPT based semantic scoring, SageMaker training workflows, LoRA fine tuning, Pinecone or pgvector, S3, RDS PostgreSQL, Cognito, CloudWatch and Sentry.
Document processing used pdfplumber as the primary parser and OCR fallback for scanned or image based PDFs.
ATS scoring used a hybrid approach: keyword or TF-IDF prefilter followed by semantic scoring for top matches.
The vector search layer supported resume embeddings, job embeddings and semantic similarity matching.
Voice mock interview support used speech to text and text to speech components.

## P1 AI Engineer Bullet Bank

Built an AI resume intelligence platform using FastAPI, GPT based APIs, LangChain style retrieval flows, vector search and structured prompt outputs for resume scoring and rewriting.
Designed hybrid ATS scoring that combined keyword filtering, semantic ranking and LLM based reasoning to evaluate resume and job description alignment.
Engineered prompt templates with section level instructions, few shot examples and structured JSON output to improve rewrite consistency and reduce hallucinations.
Implemented RAG style context injection using resume chunks, job description requirements and retrieved skill mappings to produce grounded recommendations.
Built evaluation checks comparing generated resume bullets against JD requirements, source resume facts, keyword coverage and hallucination risk.
Integrated vector search with metadata filters to retrieve relevant resume sections, job requirements and skill evidence during scoring and rewriting.
Fine tuned Llama based adapters with LoRA to improve resume enhancement quality and reduce cost at scale.
Created guardrails that blocked unsupported claims, enforced schema validation and flagged low confidence rewrite suggestions for review.
Designed AI workflows for mock interview feedback by combining transcription analysis with LLM based answer evaluation.

## P1 ML Engineer Bullet Bank

Trained custom ATS scoring models using SageMaker workflows with feature engineering, hyperparameter tuning and reproducible evaluation steps.
Built ML feature pipelines extracting skill coverage, keyword density, semantic similarity scores, section completeness and job title alignment from resumes and JDs.
Designed batch scoring jobs for high volume resume and job description comparisons while keeping real time scoring endpoints available for user facing interactions.
Managed model experiments with MLflow by tracking metrics, parameters, artifacts and model versions across scoring model iterations.
Implemented data and prediction drift monitoring on scoring outputs to detect quality degradation and trigger retraining workflows.
Created model validation pipelines comparing keyword based, semantic and hybrid scoring approaches across relevance and ranking metrics.
Built inference APIs using FastAPI to serve scoring models with low latency, request validation and structured logging.
Implemented dataset versioning for training snapshots, extracted features and evaluation datasets to support reproducible model development.
Used spot based managed training jobs to reduce model training cost while preserving automated model lifecycle workflows.

## P1 Data Engineer Bullet Bank

Built scalable document ingestion pipelines for resume and job description uploads using Python parsers, OCR fallback services, cloud storage and relational metadata tables.
Created ETL workflows that extracted resume sections, skills, job titles, education, experience dates and JD requirements into normalized downstream datasets.
Designed batch processing jobs using Python and Spark to transform unstructured resume and job posting content into structured records for scoring and analytics.
Implemented data validation checks for unsupported file types, empty extractions, duplicate uploads, missing sections, invalid dates and failed OCR jobs.
Built job posting ingestion pipelines using external job APIs with fallback providers, retry handling and normalized schemas for job matching datasets.
Stored raw documents in object storage while maintaining parsed metadata, processing status, user records and scoring results in PostgreSQL.
Created monitoring for parsing failures, job ingestion freshness, batch processing latency and data quality exceptions to improve pipeline reliability.
Optimized database indexes and queries for resume lookup, scoring history, skill search and job match retrieval.
Produced structured datasets that enabled dashboard reporting on user activity, resume quality trends, match scores and document processing volume.

## P1 Data Scientist Bullet Bank

Developed ATS scoring logic using TF-IDF, keyword overlap, semantic similarity and structured resume feature signals to rank job fit.
Engineered features from resume sections, skills, titles, years of experience, education signals, JD requirements and keyword density.
Analyzed scoring outcomes to identify false positives, false negatives, weak matching patterns and threshold tuning opportunities.
Compared keyword only, semantic only and hybrid scoring strategies using relevance metrics and user feedback signals.
Built explainability outputs showing matched skills, missing requirements, weak sections and high value rewrite opportunities.
Used Python based analysis to profile resumes, job descriptions and scoring distributions across user segments and role categories.
Designed evaluation datasets for ATS score calibration using manually reviewed resume to JD alignment examples.
Translated scoring insights into product recommendations that helped users improve resume targeting and job match quality.

## P1 Python Developer or Software Engineer Bullet Bank

Built async FastAPI endpoints for resume upload, document parsing, ATS scoring, resume rewrite requests, job matching and interview feedback workflows.
Created modular Python services for parsing, scoring, rewriting, job ingestion, user profile management and notification workflows.
Implemented Pydantic validation, OAuth based authentication, rate limiting, structured errors and API response contracts across backend services.
Designed background processing patterns for long running parsing, scoring and interview analysis jobs with status tracking and retry support.
Integrated React TypeScript frontend workflows with backend APIs for file upload, scoring results, generated suggestions and user profile updates.
Built WebSocket and SSE endpoints to stream long running AI or scoring responses back to the client with fallback handling.
Created PostgreSQL schemas and optimized queries for users, resumes, parsed sections, job descriptions, scores and activity history.
Implemented API logging, error monitoring and service health checks through cloud monitoring and Sentry.
Containerized services with Docker and deployed backend workloads on Kubernetes based infrastructure.

## P1 Platform Engineer Bullet Bank

Designed cloud deployment architecture for document processing workers, scoring APIs and user facing backend services.
Implemented CI/CD pipelines for Python services and ML workflows with automated validation, testing, packaging and deployment.
Configured Kubernetes autoscaling for API services and asynchronous processing workers handling variable resume upload volume.
Built monitoring dashboards for API latency, queue depth, parsing failures, model endpoint errors and infrastructure utilization.
Implemented environment configuration management for development, staging and production deployments.
Created secure access controls for object storage, relational databases, model endpoints and external API keys.
Improved production reliability by separating document processing, scoring and user APIs into independently deployable services.

---

# PROJECT P2: MULTI-PLATFORM AI WRITING ASSISTANT

Company: Bee Data Technologies
Project type: Cross platform AI writing assistant for real time rewriting suggestions
Architecture: User types in mobile, browser or desktop app to text capture layer to FastAPI backend to rewriting service to streaming response back to client
Business outcome: Delivered real time writing suggestions across messaging contexts with privacy first session design

## P2 Truth Base

The assistant captured text from Android, iOS, browser based apps and desktop contexts, sent text to backend rewriting services and streamed suggestions back to the user.
Core components included React Native, browser extension, Electron overlay, FastAPI, WebSocket, SSE, GPT-3.5 Turbo or Claude Haiku, Redis active sessions, DynamoDB opt in history, Cognito, Lambda, ECS, CloudWatch and Sentry.
Privacy design used no storage by default and encrypted opt in history.
Context management used sliding window context from recent messages.

## P2 AI Engineer Bullet Bank

Built real time AI rewriting workflows that used conversation context, persona prompts and fast LLM inference to generate tone aware message suggestions.
Designed prompt templates for predefined personas and user customized writing styles while controlling output format and response length.
Implemented sliding window context retrieval to provide recent conversation awareness without sending entire threads to the model.
Created model routing logic between fast and cost efficient LLMs based on latency, complexity and cost constraints.
Built safety and privacy controls that avoided storing conversation content by default while supporting encrypted opt in history.
Evaluated rewrite quality across tone, clarity, intent preservation and response usefulness for messaging use cases.

## P2 ML Engineer Bullet Bank

Designed inference workflows for low latency rewriting suggestions with model routing, response streaming and fallback behavior.
Created evaluation datasets for rewrite quality covering tone adjustment, grammar correction, concise phrasing and intent preservation.
Implemented latency tracking and quality monitoring for LLM rewrite responses across mobile, browser and desktop clients.
Built prompt versioning and experiment tracking to compare rewrite templates, persona behavior and cost performance.
Designed scalable serving patterns for handling concurrent rewrite requests with session context and streaming output.
Optimized request payloads and context windows to balance model quality, token cost and response latency.

## P2 Data Engineer Bullet Bank

Built event pipelines for capturing anonymized product usage signals, rewrite request metadata, latency metrics and error events without storing private message content by default.
Designed session data handling using Redis TTL for active context and optional durable storage for user enabled encrypted history.
Created structured schemas for user sessions, rewrite events, persona selections, platform type, response latency and error categories.
Implemented data retention rules that separated temporary session context from long term anonymized analytics.
Built monitoring datasets for request volume, platform usage, model latency, failure rate and feature adoption.
Supported analytics workflows that helped identify high traffic platforms, expensive prompt patterns and common rewrite use cases.

## P2 Data Scientist Bullet Bank

Analyzed rewrite quality feedback, usage patterns, persona adoption and latency tradeoffs to improve model selection and prompt templates.
Created metrics for rewrite usefulness, acceptance rate, response latency and user retention across platform channels.
Compared prompt variants and persona templates to identify which writing styles produced higher acceptance and engagement.
Segmented usage by platform, message type and persona selection to inform product improvements.
Built lightweight evaluation workflows for grammar correction, tone shift accuracy, conciseness and intent preservation.

## P2 Python Developer or Software Engineer Bullet Bank

Built FastAPI backend services for rewrite requests, session context retrieval, persona management and streaming suggestion delivery.
Implemented WebSocket connections for real time typing suggestions and SSE endpoints for one way LLM response streaming fallback.
Developed browser extension and Electron integration APIs that connected text capture clients to backend rewriting services.
Created Redis based active session management with TTL rules and optional DynamoDB backed history for user enabled storage.
Implemented authentication, rate limiting, request validation, retry logic and structured logging across writing assistant APIs.
Designed service fallbacks for LLM provider latency, timeout errors and disconnected streaming clients.
Built monitoring and error tracking for mobile, browser and desktop platform requests using cloud logs and Sentry.

## P2 Platform Engineer Bullet Bank

Deployed API and streaming workloads across serverless and container based infrastructure to support low latency rewrite requests.
Configured autoscaling for WebSocket servers and API endpoints based on concurrent connections and request volume.
Implemented monitoring for streaming disconnects, model timeout errors, token usage, latency and service health.
Managed secure configuration for authentication, encryption keys, API secrets and environment specific deployments.
Built CI/CD workflows for backend services, browser extension builds and desktop app release artifacts.

---

# 6. COMPANY 2: ALLIED HEALTH AGENCY — DALLAS, TX

Default role title: AI/ML Engineer
Default cloud: AWS
Primary projects: P3 Multi-Agent Call Intelligence, P4 Insurance RAG Chatbot

## COMPANY TRUTH BASE

Allied Health Agency work centered on healthcare and insurance operations. The work included call transcription pipelines, sentiment classification, compliance checks, routing support, reporting, policy document Q&A, document ingestion, retrieval, API services, analytics and cloud storage.

Use Allied Health as strong evidence for healthcare AI, ML engineering, data engineering, Python backend, analytics and production workflow automation.
For non AI roles, describe this work as call data pipelines, transcription ingestion, classification services, reporting data models, policy document processing and operational automation.

## ALLIED HEALTH CORE BULLET BANK BY ROLE

### Allied Lane: AI Engineer

Built AI powered call intelligence and policy Q&A workflows using transcription, sentiment analysis, LLM validation, retrieval and human handoff patterns.
Designed healthcare focused AI workflows that processed call transcripts, detected sentiment, checked compliance signals and generated coaching insights.
Implemented RAG based policy Q&A with citation tracking and low confidence escalation to support teams.
Created prompt templates for healthcare and insurance terminology with controlled outputs, source citations and escalation logic.
Built agent style workflows for transcription, compliance, routing and coaching when AI intensity level requires agentic language.

### Allied Lane: ML Engineer

Built ML workflows for call sentiment classification, routing support and anomaly detection using Python, Scikit-learn and domain specific transcript features.
Trained sentiment classification models on call transcript data achieving 88% accuracy with cross validation and hyperparameter tuning.
Created feature engineering pipelines for transcript cleaning, tokenization, embedding generation, sentiment labels and routing signals.
Implemented model monitoring for classification accuracy, prediction distribution shifts, drift signals and retraining triggers.
Deployed inference APIs for real time sentiment predictions using containerized services and health monitoring.
Managed experiment tracking and model versioning for repeatable training and evaluation workflows.

### Allied Lane: Data Engineer

Built call data ingestion pipelines processing Twilio call metadata, audio file references, AWS Transcribe transcript outputs, speaker diarization results and sentiment classification scores into structured PostgreSQL tables for downstream reporting and analytics.
Designed data architecture separating raw audio storage in S3 from parsed transcript text, extracted compliance flags, sentiment predictions, routing decisions and agent performance metrics in relational tables with clear schema versioning.
Created batch processing workflows using PySpark on EMR to analyze large-scale historical call transcript datasets generating aggregated sentiment trends, escalation patterns, compliance review volumes and agent coaching opportunity reports reducing processing time by 65%.
Implemented data validation checks for missing call identifiers, incomplete transcript segments, duplicate call records, failed AWS Transcribe jobs and inconsistent speaker-to-agent mapping ensuring data integrity for compliance reporting.
Built document ingestion pipelines for insurance policy PDFs and forms using pdfplumber for text extraction with AWS Textract as OCR fallback processing multi-format documents into chunked and indexed records for policy search systems.
Designed ETL workflows that extracted policy sections, table data, form field values, effective dates and coverage terms from raw documents transforming unstructured insurance content into searchable structured datasets.
Created reindexing pipelines using S3 event triggers with Lambda functions for real-time indexing of newly uploaded policy documents and daily scheduled full-refresh jobs ensuring search data freshness and consistency.
Built pipeline monitoring for transcription job latency, document parsing failure rates, batch processing duration, data freshness metrics and downstream reporting availability providing operational visibility for production support.
Optimized SQL queries and database indexes for call transcript search, audit trail lookup, policy section retrieval, sentiment trend analysis and compliance reporting workloads reducing query response times for dashboard consumers.
Designed audit trail data models storing user queries, retrieved policy sections, answer confidence scores, human handoff events and support follow-up status in DynamoDB with 90-day TTL and S3 long-term archive for compliance.

### Allied Lane: Data Scientist

Trained sentiment classification models on healthcare call transcript data using Scikit-learn achieving 88% accuracy with cross-validation, hyperparameter tuning and domain-specific feature engineering on speaker turns, keyword flags and call duration signals.
Engineered features from call transcripts including speaker sentiment shifts, compliance phrase frequency, call duration patterns, escalation triggers, hold time ratios and historical agent performance scores for classification and routing model training.
Evaluated classification model performance using accuracy, precision, recall and confusion matrix analysis across call categories identifying misclassification patterns and threshold tuning opportunities for production sentiment detection.
Analyzed call patterns across 1,000+ daily insurance agent calls to identify negative sentiment drivers, high-escalation call categories, peak volume periods and coaching opportunity segments informing operational process improvements.
Built analytical views measuring chatbot answer relevance, citation accuracy, low-confidence escalation rates, policy coverage gaps and support workload reduction enabling product team to track 40% decrease in manual support queries.
Designed scoring experiments comparing rule-based, ML-based and hybrid routing approaches using historical call outcome data to optimize automated call distribution accuracy across agent skill categories.
Created reporting datasets connecting call quality metrics, agent coaching recommendations and customer satisfaction proxies providing operational leadership with data-driven performance insights.
Performed statistical analysis on insurance policy query patterns to identify documentation gaps, frequently asked topics and content areas where chatbot answer quality could be improved through targeted policy document updates.

### Allied Lane: Python Developer or Software Engineer

Developed FastAPI services for call transcription processing, real-time sentiment inference, insurance policy Q&A, compliance review workflows and human agent escalation handling with request validation and structured error responses.
Built Django REST endpoints for administrative workflows including agent performance dashboards, compliance review queues and operational configuration screens where built-in ORM models and admin tooling reduced development time.
Built Python backend modules for Twilio webhook integration, AWS Transcribe streaming output parsing, transcript text cleaning, classification request routing and structured result formatting across call intelligence workflows.
Created REST API endpoints with Pydantic validation, structured logging and health checks serving real-time sentiment predictions and policy answers for healthcare operations teams.
Implemented OAuth2 and OpenID Connect authentication flows with JWT validation, token lifecycle management and role-based access controls for protected healthcare backend APIs.
Implemented asynchronous processing patterns using Celery workers for long-running transcription jobs, batch document ingestion tasks, policy reindexing workflows and analytics report generation with progress tracking and retry handling.
Integrated S3 document storage, RDS PostgreSQL metadata tables, DynamoDB conversation logs and Redis session caching into backend service layer providing consistent data access patterns across call and chatbot workflows.
Designed Redis Streams-based messaging for passing call processing events between transcription, classification, compliance and routing service components enabling loose coupling and independent scaling.
Built event-triggered serverless functions using Lambda for real-time document reindexing on S3 uploads, automated policy embedding generation and scheduled consistency verification jobs.
Supported healthcare workflow controls with audit logging, access restrictions, encrypted storage and traceable API activity aligned with HIPAA and clinical data handling expectations.
Created PostgreSQL schemas for call metadata, transcript segments, sentiment outputs, compliance flags, routing decisions, policy chunks, user queries, citation references and audit trail records.

---

# PROJECT P3: MULTI-AGENT CALL INTELLIGENCE SYSTEM

Company: Allied Health Agency
Project type: Call intelligence, transcription, compliance, sentiment, routing and coaching
Architecture: Live call to Twilio to transcription service to compliance checks to sentiment classification to routing and coaching workflows
Business outcome: Improved call QA visibility, sentiment tracking, compliance review and routing support

## P3 Truth Base

The system processed live or recorded calls using Twilio, AWS Transcribe Streaming, Python services, sentiment models, compliance logic, Redis Streams, RDS PostgreSQL, S3, PySpark batch analytics, CloudWatch, Prometheus and audit controls.
When AI intensity is high, this can be described as a multi agent workflow using LangGraph state machines.
When AI intensity is low or target role is Data Engineer or Python Developer, avoid calling it agentic and describe it as call processing, transcription, classification and routing workflow.

## P3 AI Engineer Bullet Bank

Designed a call intelligence workflow with specialized AI components for transcription, compliance validation, sentiment detection, routing and coaching.
Implemented LangGraph based state transitions for coordinating transcription, compliance, sentiment and routing steps when the JD asks for agentic AI.
Built GPT based compliance validation prompts that reviewed flagged phrases against healthcare disclosure rules and escalation criteria.
Created coaching outputs that summarized call quality, sentiment shifts and improvement opportunities for operational teams.
Implemented human review paths for low confidence compliance or coaching outputs to reduce automation risk.
Designed traceability for AI decisions through logged state transitions, prompts, model responses and source transcript segments.

## P3 ML Engineer Bullet Bank

Fine tuned a DistilBERT based sentiment classifier on healthcare call transcript data for low latency call sentiment prediction.
Trained routing support models using historical call outcomes, transcript features and escalation labels to recommend call distribution paths.
Built feature engineering workflows for transcript cleaning, speaker separation, phrase extraction, sentiment labels and routing features.
Implemented model monitoring for sentiment distribution shifts, prediction confidence and retraining triggers.
Evaluated model performance using accuracy, precision, recall and confusion matrix analysis across call categories.
Deployed classification inference behind FastAPI services with health checks, logging and performance monitoring.

## P3 Data Engineer Bullet Bank

Built call data ingestion pipelines that processed Twilio call metadata, audio files, streaming transcript output, sentiment scores and routing outcomes.
Designed structured data models for calls, speakers, transcripts, compliance flags, sentiment predictions, routing decisions and coaching summaries.
Created batch analytics workflows using PySpark to process large transcript datasets and generate operational reporting tables.
Implemented data quality checks for missing call identifiers, incomplete transcripts, duplicate call records, failed transcription jobs and inconsistent agent mappings.
Stored raw audio in cloud object storage while maintaining call metadata, transcript text and scoring outputs in PostgreSQL.
Built pipeline monitoring for transcription latency, failed jobs, data freshness, batch processing duration and downstream reporting availability.
Created audit friendly logging for call processing events, data transformations, classification outputs and review status changes.
Optimized SQL queries for transcript search, call history lookup, sentiment trend analysis and compliance reporting.

## P3 Data Scientist Bullet Bank

Analyzed call transcripts to identify sentiment patterns, escalation signals, agent coaching opportunities and routing decision trends.
Engineered features from call duration, speaker turns, sentiment shifts, keyword flags, transcript text and historical outcomes.
Evaluated sentiment classification models using accuracy, precision, recall and confusion matrix outputs to improve monitoring reliability.
Studied correlation between sentiment changes, escalation outcomes and agent performance to guide operational improvements.
Built analytical views measuring call quality, compliance review volume, routing success and support team workload.
Translated model outputs into clear insights for operations teams reviewing agent performance and customer experience.

## P3 Python Developer or Software Engineer Bullet Bank

Developed Python backend services for call ingestion, transcript processing, sentiment inference, compliance checks and routing recommendations.
Integrated Twilio voice events and streaming transcription outputs with backend APIs and processing workers.
Built FastAPI endpoints for call status, transcript retrieval, sentiment scoring, compliance review and reporting access.
Implemented Redis Streams based messaging for passing call events between transcription, classification and routing services.
Created PostgreSQL schemas for call metadata, transcript segments, sentiment outputs, compliance flags and routing decisions.
Implemented retry handling, timeout management and structured logging for unreliable external call and speech APIs.
Built secure service patterns with encryption, role based access and audit logs for healthcare related call data.

## P3 Platform Engineer Bullet Bank

Deployed call processing APIs, worker services and classification endpoints with containerized infrastructure and health monitoring.
Configured monitoring for streaming transcription latency, queue depth, API failures, model endpoint health and infrastructure utilization.
Built autoscaling patterns for transcription and classification workloads during call volume spikes.
Implemented secrets management, audit logging and encrypted storage for call recordings and transcript data.
Supported production reliability through service separation, retry policies, circuit breakers and failure isolation.

---

# PROJECT P4: INSURANCE RAG CHATBOT

Company: Allied Health Agency
Project type: Insurance policy Q&A, document ingestion, retrieval, citations and support handoff
Architecture: Documents to processing to chunking to embeddings to vector store to retrieval to LLM answer with citations to handoff workflow
Business outcome: Reduced support workload by 40% through self service policy Q&A

## P4 Truth Base

The system ingested insurance policy documents, parsed PDFs and forms, chunked content, generated embeddings, stored vectors, retrieved relevant chunks and generated cited answers.
Core components included pdfplumber, AWS Textract, LangChain RecursiveCharacterTextSplitter, OpenAI embeddings, Pinecone or pgvector, Claude via Bedrock, FastAPI, React chat UI, S3 event based reindexing, Lambda, DynamoDB, S3 archive, RDS metadata, CloudWatch and LangSmith.
For Data Engineer roles, describe this as document ingestion, indexing, metadata management, reindexing and audit storage.
For AI Engineer roles, describe it as RAG, retrieval, citations, prompt control and hallucination reduction.

## P4 AI Engineer Bullet Bank

Built an insurance policy Q&A system using RAG architecture with document chunking, embedding generation, vector retrieval and citation controlled answer generation.
Designed retrieval prompts that injected numbered policy chunks and required the model to return source backed answers with citations.
Implemented low confidence detection and human handoff when retrieved context was insufficient or user frustration was detected.
Improved answer grounding by combining top K retrieval, MMR retrieval and metadata filtering across policy type, date and section.
Created evaluation checks for citation accuracy, answer relevance, hallucination risk and source traceability.
Integrated Claude via managed cloud LLM service for policy answer generation with strong instruction following.
Built reindexing workflows to keep vector indexes synchronized with updated policy documents.

## P4 ML Engineer Bullet Bank

Built embedding and retrieval pipelines for insurance policy search using vector similarity, metadata filters and relevance evaluation workflows.
Evaluated retrieval strategies including top K similarity, MMR and hybrid keyword matching to improve answer relevance.
Designed retrieval quality metrics measuring source recall, citation accuracy, low confidence rate and user escalation rate.
Implemented monitoring for embedding pipeline failures, vector index freshness, retrieval latency and answer quality signals.
Created experimentation workflows to compare chunk sizes, overlap settings, embedding models and retrieval thresholds.
Built FastAPI inference flows connecting retrieval, generation and confidence scoring for user facing Q&A.

## P4 Data Engineer Bullet Bank

Built document ingestion pipelines for insurance policy PDFs, forms and HTML content using Python parsers, OCR fallback and cloud storage.
Designed ETL workflows that extracted policy sections, tables, form fields, document metadata, effective dates and section level references.
Created chunking and indexing pipelines that transformed policy documents into searchable records with metadata for type, date and section.
Implemented reindexing workflows using storage event triggers and scheduled full refresh jobs to keep search data current.
Built data validation checks for missing documents, failed OCR extraction, duplicate policy versions, invalid metadata and stale vector indexes.
Stored raw documents in cloud object storage with metadata, user queries, document sections and audit records in relational and NoSQL stores.
Created audit trail datasets for user questions, retrieved documents, answer confidence, handoff events and support follow up.
Built monitoring for document ingestion failures, reindexing latency, retrieval freshness and policy data availability.

## P4 Data Scientist Bullet Bank

Analyzed user questions, retrieval success, low confidence events and handoff reasons to improve policy answer coverage.
Built metrics for answer relevance, citation accuracy, escalation rate, document coverage and support workload reduction.
Evaluated chunking strategies, retrieval thresholds and embedding options to improve source recall and user satisfaction.
Segmented policy queries by topic, product type and failure category to identify documentation gaps.
Translated chatbot performance metrics into recommendations for updating policy content and support workflows.

## P4 Python Developer or Software Engineer Bullet Bank

Developed FastAPI services for document upload, indexing, query handling, answer generation, citation return and human handoff workflows.
Built backend modules for PDF parsing, OCR fallback, chunk generation, metadata extraction, vector upsert and retrieval orchestration.
Implemented SSE streaming for chat responses and REST endpoints for document management, query history and support handoff.
Created PostgreSQL and DynamoDB data models for documents, chunks, queries, citations, confidence scores and audit events.
Built event triggered reindexing using storage events and serverless processing for newly uploaded policy documents.
Implemented error handling, retries, structured logging and monitoring for document processing and retrieval failures.
Secured policy document access with role based controls, encryption and audit trails.

## P4 Platform Engineer Bullet Bank

Configured document processing, indexing and chat services across cloud storage, serverless triggers, API services and monitoring systems.
Built observability for indexing latency, retrieval latency, chat API errors, vector index freshness and handoff event volume.
Implemented secure storage, encryption and audit logging for policy documents, query logs and support handoff records.
Created deployment workflows for backend APIs, indexing workers and chat service updates.
Improved reliability through scheduled reindexing, failure alerts, retry queues and health checks.

---

# 7. COMPANY 3: BYJU'S — BANGALORE, INDIA

Default role title: Data Engineer
Default cloud: GCP
Primary focus: Data engineering, analytics, recruitment analytics, sales performance analytics, predictive modeling support
AI projects: None. Do not overstate GenAI here.

## BYJU'S TRUTH BASE

BYJU'S work focused on data engineering, analytics and predictive modeling in education technology and sales operations. Work included Salesforce CRM ingestion, BigQuery warehouse design, Dataproc or PySpark batch processing, dashboards, recruitment funnel analytics, trainee scoring, sales performance analysis, Python automation and reporting.

## BYJU'S Bullet Bank: Data Engineer

Built ETL pipelines using Python to extract Salesforce CRM and operational data, apply business transformation rules and load structured datasets into BigQuery.
Designed BigQuery tables, partitioning strategies, materialized views and optimized SQL queries for sales performance and recruitment funnel reporting.
Created batch processing workflows using PySpark and Dataproc to prepare large scale recruitment and sales datasets for analytics and predictive scoring.
Automated reporting workflows that connected BigQuery outputs with stakeholder dashboards and reduced manual reporting effort by 60%.
Implemented data quality checks for duplicate leads, missing recruiter metadata, invalid funnel stages and inconsistent sales activity records.
Built reusable data models for candidate pipeline stages, recruiter performance, sales conversion metrics and training outcome analysis.
Optimized warehouse query performance and cost by using partitioning, clustering and scheduled transformation jobs.

## BYJU'S Bullet Bank: Data Scientist

Built predictive scoring models to estimate candidate success and identify high potential sales trainees using Python, Scikit-learn and XGBoost.
Engineered features from recruiter activity, training performance, assessment scores, funnel movement and historical conversion outcomes.
Analyzed recruitment funnel performance to identify bottlenecks, high cost stages and conversion improvement opportunities.
Created model evaluation workflows using accuracy, precision, recall and validation splits to compare candidate success prediction models.
Developed sales performance analytics measuring trainee productivity, recruiter quality and regional conversion patterns.
Translated analytical findings into operational recommendations for hiring, training and sales leadership teams.

## BYJU'S Bullet Bank: Analytics Engineer or BI Engineer

Created BigQuery based analytical models for sales performance, recruitment funnel metrics, candidate outcomes and training effectiveness reporting.
Built Tableau or Power BI dashboards that enabled stakeholders to monitor funnel conversion, recruiter productivity and sales team performance.
Developed SQL transformations and materialized views that standardized business definitions across recruitment and sales reporting.
Automated recurring performance reports using Python and warehouse queries to reduce manual spreadsheet based workflows.
Partnered with business stakeholders to define KPIs, dashboard filters, drill downs and refresh logic for executive reporting.

## BYJU'S Bullet Bank: Python Developer or Software Engineer

Developed Python automation scripts for data extraction, transformation, validation and reporting across CRM and internal operations systems.
Built reusable modules for data cleansing, file processing, API extraction, report generation and scheduled workflow execution.
Optimized SQL queries and Python data processing logic to reduce reporting delays and improve data availability.
Created validation logic that flagged missing fields, duplicate records and inconsistent business stage mappings before dashboard refresh.
Integrated warehouse outputs with reporting tools and Google Sheets based stakeholder workflows.

---

# 8. COMPANY 4: COGNIZANT TECHNOLOGY SOLUTIONS — BANGALORE, INDIA

Default role title: Program Analyst
Default environment: On premise, SQL Server, SSIS, Python, JavaScript and enterprise application support
Primary focus: Software engineering, ETL, SQL, data processing and PLM platform customization
AI projects: None. Do not add AI here.

## COGNIZANT TRUTH BASE

Cognizant work focused on enterprise software support, data processing, SQL Server, SSIS, Python automation, Excel file processing, backend customizations, JavaScript UI components and data quality validation.

## Cognizant Bullet Bank: Data Engineer

Built ETL workflows using SSIS and Python scripts to extract operational data, apply transformation rules and load curated datasets into SQL Server.
Automated large Excel processing workflows using Python, Pandas and openpyxl for 100K+ row financial and operational datasets.
Created SQL validation scripts to check referential integrity, calculation accuracy, duplicate records and missing business fields.
Optimized SQL Server queries, indexes and stored procedures to improve reporting and data processing performance.
Implemented automated backup support, query tuning and data quality checks for enterprise reporting datasets.

## Cognizant Bullet Bank: Python Developer or Software Engineer

Engineered custom Python modules for Sopheon Accolade PLM workflows including backend data processing, validation and integration logic.
Developed JavaScript UI components with form validation, dynamic grids and user interaction improvements for enterprise application users.
Built reusable Python scripts for file processing, data transformation, validation reporting and operational automation.
Implemented secure SQL development practices including parameterized queries, role based access and audit logging.
Supported production issue resolution by debugging backend logic, SQL procedures and data integration failures.

## Cognizant Bullet Bank: Analytics Engineer or BI Engineer

Created SQL Server reporting datasets and validation checks to support financial and operational analytics.
Built transformation logic that standardized operational data for downstream reporting and audit review.
Automated recurring data preparation tasks using Python and SQL scripts to reduce manual spreadsheet work.
Improved data reliability by reconciling source files, transformed outputs and reporting tables.

---

# 8A. JD TO RESUME SELECTION EXAMPLES

Example 1:
JD: Python Engineer, FastAPI, Django, AI agents, LangChain, PostgreSQL, Redis, Docker, cloud, async task queues
Primary Role: Python Developer
Secondary Role: AI Engineer
AI Intensity: Level 4
Use: Bee Data Python lane, selected Bee Data AI backend bullets, Allied Python lane, P3 Python lane
Avoid: Data Scientist scoring-heavy bullets, Data Engineer warehouse-heavy bullets, LoRA unless explicitly required
Summary tone: Python backend engineer building AI agent infrastructure

Example 2:
JD: Data Engineer, Spark, Airflow, BigQuery, ETL, data quality, GCP
Primary Role: Data Engineer
Secondary Role: None or Analytics Engineer
AI Intensity: Level 0 or Level 1
Use: Bee Data Data Engineer lane, Allied Data Engineer lane, BYJU'S Data Engineer lane
Avoid: RAG, GPT, Claude, prompt engineering, LangGraph, LoRA
Summary tone: Cloud data engineer building pipelines and warehouse workflows

Example 3:
JD: Machine Learning Engineer, model deployment, feature pipelines, MLflow, drift, inference APIs
Primary Role: ML Engineer
Secondary Role: Platform Engineer
AI Intensity: Level 2
Use: Bee Data ML lane, P1 ML lane, Allied ML lane, P3 ML lane
Avoid: too much dashboard language, too much pure LLM rewriting unless JD asks
Summary tone: ML engineer building training, serving and monitoring workflows

Example 4:
JD: Data Scientist, regression, classification, experiments, Python, SQL, business metrics
Primary Role: Data Scientist
Secondary Role: Data Engineer
AI Intensity: Level 1 or Level 2
Use: Bee Data Data Scientist lane, Allied Data Scientist lane, BYJU'S Data Scientist lane
Avoid: Kubernetes-heavy platform bullets and backend-only API bullets
Summary tone: Data scientist turning models and analysis into business decisions

---

# 9. ROLE SPECIFIC RESUME SUMMARY BANK

Use only one summary style based on the classified Primary Role.

AI Engineer Summary Pattern:
AI Engineer with 7 years of experience building production GenAI, RAG, LLM workflow and AI platform solutions using Python, FastAPI, LangChain, vector databases, cloud services and model serving workflows. Experienced in turning AI prototypes into reliable user facing systems with monitoring, guardrails and measurable business impact.

ML Engineer Summary Pattern:
ML Engineer with 7 years of experience building model training, feature engineering, inference, monitoring and MLOps workflows using Python, Scikit-learn, PyTorch, MLflow, cloud platforms and FastAPI. Skilled in deploying models into production systems with experiment tracking, drift monitoring and retraining workflows.

Data Scientist Summary Pattern:
Data Scientist with 7 years of experience applying Python, SQL, statistical analysis, feature engineering and machine learning to solve business problems across healthcare, education technology and AI products. Experienced in building scoring models, analyzing user behavior, evaluating model performance and translating insights into operational decisions.

Data Engineer Summary Pattern:
Data Engineer with 7 years of experience building Python based ETL pipelines, cloud data workflows, batch processing systems, warehouse models and data quality frameworks across healthcare, education technology and AI product environments. Skilled in Spark, SQL, PostgreSQL, BigQuery, cloud storage, orchestration and production data monitoring.

Python Developer Summary Pattern:
Python Developer with 7 years of experience building backend services, APIs, async processing workflows and cloud deployed applications using Python, FastAPI, Django, PostgreSQL, Redis, Docker and Kubernetes. Experienced in designing reliable service layers with OAuth2 authentication, Celery task queues, API gateway routing and production monitoring across healthcare, education and AI product environments.

Software Engineer Summary Pattern:
Software Engineer with 7 years of experience developing backend platforms, API driven applications, data processing services and cloud deployed systems using Python, FastAPI, Django, PostgreSQL, Docker, Kubernetes and modern observability practices. Skilled in building scalable services with clear API contracts, async task management, secure authentication and production reliability across enterprise and startup environments.

---

# 10. SKILLS INVENTORY BY ROLE

The writer must only list skills that appear in the selected resume bullets. Do not dump the entire inventory.

## AI Engineer Skills
Programming: Python, SQL, JavaScript, TypeScript
AI Frameworks: LangChain, LlamaIndex, LangGraph, Hugging Face Transformers, PEFT, LoRA
LLM and GenAI: GPT-4, GPT-3.5, Claude, Llama, RAG, prompt engineering, embeddings, vector search, guardrails, model evaluation
Vector Databases: Pinecone, FAISS, pgvector
Backend: FastAPI, REST APIs, WebSocket, SSE, Pydantic, OAuth 2.0
Cloud: AWS or Azure or GCP based on selected environment only
MLOps: MLflow, SageMaker or equivalent, model monitoring, dataset versioning, drift detection

## ML Engineer Skills
Programming: Python, SQL
ML Frameworks: Scikit-learn, PyTorch, TensorFlow, XGBoost, Hugging Face Transformers
MLOps: MLflow, model registry, experiment tracking, dataset versioning, model monitoring, drift detection, retraining workflows
Serving: FastAPI, Docker, Kubernetes, REST APIs
Data: Pandas, NumPy, Spark, PySpark, feature engineering
Cloud: AWS or Azure or GCP based on selected environment only

## Data Scientist Skills
Programming: Python, SQL
Analysis: Pandas, NumPy, SciPy, statistical analysis, time series analysis, feature engineering
Modeling: Scikit-learn, XGBoost, PyTorch only if JD asks
Evaluation: precision, recall, accuracy, cross validation, confusion matrix, threshold tuning
Visualization: Tableau preferred, Power BI only if JD or Microsoft environment asks
Data Platforms: BigQuery, Snowflake, PostgreSQL based on JD

## Data Engineer Skills
Programming: Python, SQL
Data Processing: Apache Spark, PySpark, ETL, ELT, batch processing, data quality, orchestration
Cloud Data: S3 or Cloud Storage or Azure Blob Storage, BigQuery or Snowflake or Synapse, Dataproc or Databricks or EMR
Databases: PostgreSQL, SQL Server, BigQuery, Snowflake
Orchestration: Airflow, Kubeflow only if ML pipeline JD, cloud workflows based on selected environment
Monitoring: CloudWatch or Azure Monitor or Cloud Monitoring, logging, pipeline alerts

## Python Developer or Software Engineer Skills
Programming: Python, SQL, JavaScript, TypeScript
Backend: FastAPI, Django, Flask, REST APIs, WebSocket, SSE, Pydantic, Celery
Authentication: OAuth2, OpenID Connect, JWT, role-based access controls
Databases: PostgreSQL, Redis, MongoDB (document storage), SQL Server, DynamoDB only if AWS environment
Cloud and DevOps: Docker, Kubernetes, GitHub Actions, CI/CD, cloud monitoring
Cloud Platforms: AWS (EKS, Lambda, S3, RDS, API Gateway, CloudWatch), GCP (Cloud Run, GKE, Cloud Storage, Cloud SQL, Pub/Sub) — list only clouds used in bullets
Data Processing: Pandas, openpyxl, batch jobs, file processing, API integrations
Service Architecture: API Gateway routing, internal service communication, async task queues

---

# 11. FINAL WRITER RULES

Generation order:
1. Read the JD completely.
2. Classify Primary Role, Secondary Role, AI Intensity, Cloud Environment and Role Family.
3. Build the Evidence Plan for required and preferred skills.
4. Select company lanes based on Primary Role.
5. Add Secondary Role bullets only where the JD requires them.
6. Select cloud and tool substitutions.
7. Write Summary, Skills and Experience.
8. Run Role Drift Score, ATS Keyword Coverage Score, Believability Score, Skill Proof Score and Cloud Consistency Score.
9. Rewrite weak sections before final output.

Bullet writing discipline:
Each bullet should contain one core responsibility, one technical method and one outcome or purpose.
Preferred length: 22 to 34 words.
Maximum length: 42 words unless the bullet is highly technical and still readable.
Avoid stacking 5+ tools in the same bullet.
Do not start every bullet with the same verbs.
Avoid overusing Architected, Implemented, Designed, Built, Created and Developed.
Use stronger but natural verbs such as engineered, delivered, automated, optimized, integrated, standardized, productionized, migrated, modeled, validated and monitored.
Each recent role should have 8 to 10 bullets unless the user asks for more.
Second role should have 7 to 9 bullets.
Older roles should have 4 to 6 bullets.

ATS coverage discipline:
The top required skills from the JD must appear across Summary, Skills and Experience.
A skill must not be listed in Skills unless it appears in selected bullet content or is clearly supported by a replaceable skill group.
For required skills, prefer at least one proof bullet in the latest or second latest role.
Do not hide important required skills only in the Skills section.

AI content rules:
If Primary Role is Python Developer, Software Engineer, Backend Engineer, Data Engineer, Analytics Engineer or Platform Engineer, AI-related bullets must be controlled by AI Intensity.
If AI Intensity is Level 0 or Level 1, limit AI-related terms to maximum 2 across the entire resume.
If AI Intensity is Level 3 or Level 4 because the JD explicitly asks for AI frameworks, AI agents, LangChain, LlamaIndex, embeddings, vector databases or RAG, AI-related bullets are allowed. They must be written as engineering responsibilities, not research claims.
For Python AI backend roles, use language like state persistence, long-running task management, agent workflow orchestration, tool routing, API integration, async workers and observability.
Do not lead with LoRA, fine-tuning, prompt engineering or model research unless the JD explicitly requires those terms.

Service mesh and architecture language:
Do not use "service mesh" unless naming a specific tool such as Istio, Linkerd or AWS App Mesh.
Prefer "API Gateway routing and internal service communication patterns" because it is accurate and interview-safe.
Use "service mesh" only when the JD explicitly asks for it and the generated bullet names the implementation.

Tool specificity rule:
When mentioning a tool, be specific enough that an interviewer would believe it.
Bad: "Worked on authentication."
Good: "Implemented OAuth2 and OpenID Connect flows with JWT validation, token expiration handling and role-based access controls."
Bad: "Used async queues."
Good: "Built Celery workers with Redis broker for long-running parsing and scoring jobs with retries, progress tracking and timeout handling."

MongoDB usage rule:
Include MongoDB in bullets only when the JD explicitly asks for MongoDB or NoSQL.
When used, frame it as document-oriented storage for schema-variable data such as parsed resume structures, job posting metadata or configuration objects.
Do not list MongoDB prominently if no bullet supports it. Use "MongoDB exposure" or "MongoDB for document storage" only when necessary.

Django usage rule:
If Django appears in required or preferred skills, include one Django proof bullet where relevant.
Use Django for admin workflows, ORM-backed modules, internal dashboards, authentication-backed portals or Django REST endpoints.
Do not list Django only in Skills if the JD strongly asks for it.

Identity and security rule:
If OAuth2, JWT or OpenID Connect appear in the JD, include one proof bullet with token validation, expiration handling, role-based access and protected endpoints.
Use AWS Cognito, Entra ID, Firebase Auth or a cloud-neutral identity provider based on selected environment.

Async task queue rule:
If the JD asks for asynchronous task queues, include Celery, Redis Queue, SQS, Pub/Sub, Kafka or Redis Streams depending on selected environment and project lane.
The bullet must explain what the queue handled, such as parsing jobs, scoring jobs, document reindexing, transcription processing or analytics aggregation.

Good Clinical Practice and healthcare wording:
If the JD asks for Good Clinical Practice, clinical systems, healthcare or regulated workflows, use careful wording.
Allowed: clinical data handling expectations, audit logging, traceable API activity, access restrictions, healthcare workflow controls, HIPAA aligned handling.
Avoid claiming formal GCP compliance unless the JD specifically needs it and the experience supports it.

Metric discipline:
Use measurable outcomes where available: 5,000+ users, 30% quality improvement, 40% support workload reduction, 88% accuracy and 60% reporting effort reduction.
Do not overload one role with too many metrics.
Maximum 2 or 3 strong metrics per recent role unless the user asks for a metrics-heavy resume.
Avoid unrealistic combinations like sub-100ms latency, 10,000+ daily requests, 99.9% uptime and 75% cost reduction in the same role.

Cloud consistency:
Keep each company internally consistent with one cloud environment.
Use the JD's cloud emphasis, but do not rewrite all companies to the same cloud unless the selected Cloud Environment and truth base allow it.
Only list cloud services in Skills that appear in the generated bullets.

Role lane selection:
Use the selected Primary Role lane first.
Use Secondary Role only for 1 or 2 supporting bullets per recent role.
Do not combine all role lanes in one resume.
Do not invent tools, companies, projects, metrics or responsibilities outside this file.
Do not mention internal product names that are too specific to one company unless needed.

Final scoring requirements:
Before final output, run these checks:
Role Drift Score: Does the resume sound like the target role?
ATS Keyword Coverage Score: Are the required skills visible in Summary, Skills and Experience?
Skill Proof Score: Are required skills supported by believable bullets?
Believability Score: Are bullets specific, not overstuffed and interview-safe?
Cloud Consistency Score: Does each company use one cloud ecosystem?
Length Score: Is the resume readable and not overloaded?

If any score is weak, rewrite before final output.

