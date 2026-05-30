# GC RESUME WRITING GUIDELINES
# ================================================
# MODE: GC (10-Year Experience / Enterprise Consulting / Multi-Cloud)
# PURPOSE: This file governs how the Writer Agent writes GC resumes.
# The Scorer Agent also reads this file to understand what NOT to penalize.
# ================================================

---

## 1. DENSITY AND GRAMMAR (CRITICAL CONSTRAINTS)

- **Grammar Limits:** Maximum of 3 "and" conjunctions per bullet. Maximum of 3 sets of parentheses across all bullet points (the skills section is exempt from this limit since categories naturally use parentheses). Use "%" instead of the word "percent".
- **Forbidden Elements:** NO semicolons. NO comma before "and". NO symbols like arrows (→) or bullet dots (•) inside the text. NO hashtags (#). NO slashes in running text (e.g., never write "ML/AI" — pick one or restructure).
- **Tone:** Enterprise consulting tone — authoritative, platform-oriented, and architecture-first. Each bullet should sound like a senior engineer describing what they designed and delivered. Avoid startup-flavored language. Avoid generic claims like "proven track record."
- **Abbreviation Rule:** Never write out standard abbreviations in bullets. Use "RAG" not "Retrieval Augmented Generation." Use "ETL" not "Extract Transform Load." Use "CI/CD" not "Continuous Integration and Continuous Deployment."

---

## 2. THE BULLET FORMULA AND RHYTHM

Every bullet must start with a single, powerful action verb. NEVER use weak openers like "Responsible for," "Worked on," "Helped with," or "Involved in."

Maintain this structural rhythm across the resume:

- **60% Full Structure:** `Action` + `Object/Data` + `System/Tool` + `Result`
  Example: *Designed scalable vector-based retrieval systems using Azure AI Search and transformer embeddings to support semantic search across clinical and claims data.*

- **30% Design Structure:** `Action` + `Tool/System` (Focus on platform architecture decisions)
  Example: *Engineered large-scale ingestion pipelines using Azure Data Factory and Databricks to process healthcare datasets from multiple source systems.*

- **10% Collaboration:** Focus on cross-functional work with domain experts, compliance teams, or stakeholders.
  Example: *Collaborated with clinicians and compliance teams to validate AI models and ensure regulatory alignment.*

### Bullet Completeness Rule (CRITICAL)

Every bullet must be a COMPLETE professional statement. A bullet is not just "what you did" — it must also convey "why it matters" or "what it enabled."

**MINIMUM LENGTH:** Every bullet must be at least 18-25 words. If a bullet is under 15 words, it is too short and must be expanded with purpose, context, or impact.

**THE PURPOSE CLAUSE:** At least 60% of bullets must end with a purpose or impact clause using connectors like: enabling, supporting, improving, reducing, delivering, ensuring, achieving, providing. This clause tells the reader WHY the work mattered.

**BAD (too short, no purpose):**
  "Built ingestion pipelines using Kinesis and Airflow for batch and streaming data processing"

**GOOD (complete, purposeful):**
  "Built batch and real-time data ingestion pipelines using Kinesis and Apache Airflow enabling efficient processing of high-volume streaming and historical telecom data"

**THE SENTENCE TEST:** Read each bullet out loud. If it sounds like the person stopped talking mid-thought, it needs a purpose clause. A 6-word bullet looks like a junior engineer. A 20-word bullet looks like a senior engineer who understands the full picture.

### Verb Variety Rule
Do not repeat the same action verb more than three times across the entire resume. With 5 companies and up to 60+ bullets total, rotate broadly: Architected, Built, Designed, Deployed, Engineered, Implemented, Developed, Optimized, Automated, Integrated, Configured, Orchestrated, Trained, Created, Established, Managed, Led, Collaborated, Enforced, Enabled, Structured, Delivered, Maintained, Supported.

---

## 3. ATS OPTIMIZATION AND THE OR CONDITION

- **Mutually Exclusive Tools:** If the JD lists competing tools as OR (e.g., Snowflake/BigQuery/Synapse), choose the one that matches the relevant company's stack. Since GC resumes span all 3 clouds, you can naturally cover most OR conditions across different companies.
- **Baseline Competency:** Unless explicitly demanded by the JD, do not mention basic tools like Jupyter Notebooks or basic regressions in bullets.
- **Skills Section Alignment:** The skills section should mirror the JD's priority order.
- **Cloud Coverage:** GC resumes naturally cover AWS, Azure, and GCP across different companies. This is a STRENGTH — do not suppress it. But each company stays on its assigned cloud. If the JD emphasizes one cloud, give that company's section more bullets.
- **Skills Section Cloud Format:** Cloud must be ONE combined category: "Cloud Platforms: Azure (...), AWS (...), GCP (...)". List sub-services in parentheses. Do NOT split into separate cloud categories.

---

## 4. CHRONOLOGICAL REALITY (THE ANTI-HALLUCINATION RULE)

- **GenAI Timeline:** Only Cardinal Health (Nov 2024+) can reference GenAI, LLMs, RAG, Azure OpenAI, vector databases, prompt engineering. UBS (2023-2024) can reference ML/model training but NOT GenAI/LLMs. MTA, Cognizant, and Couth InfoTech are strictly data engineering — no ML or AI concepts.
- **Scoring Exclusion:** The Scorer MUST NOT penalize MTA, Cognizant, or Couth InfoTech for missing AI/ML keywords from the JD.
- **Technology Timeline:**
  - Couth InfoTech (2016-2018): Basic AWS (S3, EC2, RDS), Python ETL, SQL
  - Cognizant (2018-2019): AWS data lake (S3, EMR, Kinesis, Athena), Spark, Airflow
  - MTA (2019-2023): GCP (BigQuery, Dataproc, Pub/Sub), Kafka, Airflow, governance
  - UBS (2023-2024): Azure + Snowflake, Databricks, Spark, ML pipelines, feature engineering
  - Cardinal Health (2024+): Azure OpenAI, RAG, PyTorch NLP, Delta Lake, Databricks, streaming

---

## 5. PROJECT ADAPTATION BY ROLE LENS

Adapt framing based on the target role:

- **AI Engineer Lens:** Emphasize Cardinal Health's GenAI/RAG work, UBS's ML pipelines, and frame data engineering as supporting AI systems.
- **Data Scientist Lens:** Emphasize feature engineering, model training, statistical analysis, and experiment tracking across UBS and Cardinal Health.
- **Data Engineer Lens:** Emphasize ETL/ELT pipelines, data lake architecture, Spark optimization, and platform design across all 5 companies.
- **ML Engineer Lens:** Emphasize model lifecycle, training pipelines, MLOps, deployment, and monitoring.
- **Software Engineer Lens:** Emphasize API design, backend systems, CI/CD, containerization, and deployment infrastructure.

---

## 6. GC EXECUTION MODE

### Philosophy
A GC resume is an enterprise architecture document. It demonstrates depth across multiple industries (healthcare, finance, public sector, telecom) and platforms (Azure, AWS, GCP). The reader should see a senior engineer who has built large-scale systems in regulated environments across a decade-long career. Each company tells a different chapter of the same story: progressively more complex systems, from basic ETL to enterprise AI platforms.

### Specific Rules for GC Mode

**A. Enterprise Consulting Tone**
- Bullets should sound like a senior consultant describing platform-level work. Think "designed and delivered" not "coded and pushed."
- Architecture decisions matter: why Delta Lake, why Snowflake schemas, why Event Hubs over Kafka — the reasoning is implied through the technical choices.
- Domain context adds credibility: "clinical entities," "call detail records," "fraud detection," "compliance reporting" — these show the engineer understands the business, not just the tech.

**B. Multi-Cloud as Strength**
- GC resumes naturally demonstrate all 3 clouds across different companies. This is a differentiator — do not suppress it.
- Each company has a fixed cloud assignment. NEVER change it.
- If the JD emphasizes one cloud, give that company more bullets (12-14 instead of 10-12) and reduce the others proportionally.

**C. Career Progression Story**
- The resume should show clear growth: Associate Data Engineer → Data Engineer → Senior Data Engineer → Big Data Engineer/ML Engineer → Senior AI/ML Engineer.
- Early roles (Couth InfoTech, Cognizant) focus on foundational skills: ETL, SQL, basic cloud.
- Middle roles (MTA) show scale: multi-agency data consolidation, governance, real-time processing.
- Recent roles (UBS, Cardinal Health) show sophistication: ML pipelines, GenAI, RAG, enterprise AI.

**D. Bullet Count Guidance**
- Cardinal Health (current): 12-14 bullets — most depth, includes GenAI/RAG
- UBS: 12-14 bullets — strong ML and data engineering depth
- MTA: 10-14 bullets — data engineering at scale
- Cognizant: 10-14 bullets — focused data engineering
- Couth InfoTech: 10-14 bullets — foundational skills
- The Scorer MUST NOT penalize GC resumes for having more total bullets — 5 companies require more content.

**E. Metric Style**
- GC metrics should demonstrate platform-level impact and enterprise scale.
- Data volumes, processing throughput, system reliability, compliance coverage, and cost optimization are appropriate.
- Avoid startup-style metrics ("5000+ users"). Use enterprise framing ("multi-agency datasets," "daily transaction volumes," "regulatory reporting").

**F. Environment Lines**
- Each company MUST have an Environment line listing the full tech stack.
- Environment lines use the format: "Environment: Tool1, Tool2, Tool3, ..."
- Only list tools that appear in the bullets for that company.

**G. Summary Section**
- Summary should contain 10-15 bullets covering enterprise-scale capabilities.
- Each bullet should cover a distinct capability: GenAI, data engineering, cloud architecture, MLOps, streaming, governance, security, optimization, BI, collaboration.
- Summary should read like an executive capabilities brief — not a tool catalog.
- First 2-3 bullets should cover the most JD-relevant capabilities.

---

## 7. SKILLS SECTION RULES

- Group skills into logical categories matching the reference resume format.
- Recommended categories: Programming, AI/ML, Generative AI, MLOps/LLMOps, Data Engineering, Cloud Platforms, Databases, Streaming, Orchestration, DevOps, BI Tools, Governance and Security.
- Order categories to mirror JD priority.
- Cloud Platforms should be ONE combined category with sub-services in parentheses.
- Do not list more than 6-8 items per category.
- Only list tools that appear in resume_details or the actual bullets.

---

## 8. TEMPLATE AWARENESS (WHAT THE WRITER AGENT FILLS)

### Fixed in Template (DO NOT generate)
- Candidate name, email, phone
- Role title line ("Senior AI/ML Engineer")
- Company names with "Client:" prefix, locations, dates
- Role titles per company
- Section headings

### Placeholders the Writer Agent Fills

**[[Summary]]** — 10-15 bullet points. Plain text, no bullet symbols.

**[[Technical_Skills]]** — Category-value pairs, one per line:
```
Programming: Python, SQL, PySpark
AI/ML: PyTorch, Transformers, NLP, Feature Engineering
Generative AI: LLMs, RAG, Prompt Engineering, Vector Embeddings
...
```

**[[Exp{N}]]** — Bullet points for each of the 5 companies. Plain text, no bullet symbols.

**[[Exp{N}_Env]]** — Single line: "Environment: Tool1, Tool2, Tool3, ..."

NOTE: GC template has NO [[Exp{N}_Description]] fields. No role description paragraphs.

---

## 9. WRITER AGENT OUTPUT FORMAT

```json
{
  "summary": ["bullet1", "bullet2", ...],
  "technical_skills": ["Category: items", ...],
  "exp1": ["bullet1", ...],
  "exp1_env": "Environment: ...",
  "exp2": ["bullet1", ...],
  "exp2_env": "Environment: ...",
  "exp3": ["bullet1", ...],
  "exp3_env": "Environment: ...",
  "exp4": ["bullet1", ...],
  "exp4_env": "Environment: ...",
  "exp5": ["bullet1", ...],
  "exp5_env": "Environment: ..."
}
```

---

## 10. WRITER AGENT BEHAVIORAL RULES

1. **Read the JD first** — identify required skills, tools, cloud platform, and role type.
2. **Select relevant bullets** — pick bullets from gc_resume_master that best match JD requirements.
3. **Cloud is FIXED** — Cardinal Health = Azure, UBS = Azure/Snowflake, MTA = GCP, Cognizant = AWS, Couth InfoTech = AWS. Never change these.
4. **Emphasize by JD** — if JD emphasizes a specific cloud, give that company more bullets.
5. **Apply role lens** — frame bullets through the appropriate role lens based on JD title.
6. **Do not invent** — only use experience listed in gc_resume_master.
7. **Match JD language** — mirror the JD's terminology.
8. **Respect chronology** — GenAI only in Cardinal Health. ML only in UBS and Cardinal Health.
9. **Fill all 5 experience sections** — GC has 5 companies, not 4.
10. **Enterprise tone** — every bullet should sound like a senior engineer in a regulated enterprise.
