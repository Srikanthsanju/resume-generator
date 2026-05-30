# CONTRACT RESUME WRITING GUIDELINES
# ================================================
# MODE: CONTRACT (7-Year Experience / Enterprise / Vendor Focus)
# PURPOSE: This file governs how the Writer Agent writes contract resumes.
# The Scorer Agent also reads this file to understand what NOT to penalize.
# ================================================

---

## 1. DENSITY AND GRAMMAR (CRITICAL CONSTRAINTS)

- **Role Descriptions:** Must be a maximum of 2 lines. Focus strictly on the scope of the role. No fluff.
- **Grammar Limits:** Maximum of 3 "and" conjunctions per bullet. Maximum of 3 sets of parentheses across all bullet points (the skills section is exempt from this limit since categories naturally use parentheses). Use "%" instead of the word "percent".
- **Forbidden Elements:** NO semicolons. NO comma before "and". NO symbols like arrows (→) or bullet dots (•) inside the text. NO hashtags (#). NO slashes in running text (e.g., never write "ML/AI" — pick one or restructure).
- **Tone:** Keep language simple, direct, and readable. Avoid stacked noun phrases, whitepaper-like wording, and generic claims like "proven track record" or "cutting-edge solutions."
- **Abbreviation Rule:** Never write out standard abbreviations in bullets. Use "RAG" not "Retrieval Augmented Generation." Use "ETL" not "Extract Transform Load." Use "CI/CD" not "Continuous Integration and Continuous Deployment." If the abbreviation is well known in the industry, use it directly.

---

## 2. THE BULLET FORMULA AND RHYTHM

Every bullet must start with a single, powerful action verb (e.g., Architected, Engineered, Deployed, Trained, Designed, Optimized, Automated, Integrated). NEVER use weak openers like "Responsible for," "Worked on," "Helped with," or "Involved in."

Maintain this structural rhythm across the resume:

- **60% Full Structure:** `Action` + `Object/Data` + `System/Tool` + `Result`
  Example: *Built call intelligence pipeline using Python processing large-scale call transcriptions with AWS Transcribe performing automated log analysis and sentiment classification identifying performance patterns across 1,000+ daily calls.*

- **30% Design Structure:** `Action` + `Tool/System` (Focus on architecture and implementation decisions)
  Example: *Deployed ML models on AWS SageMaker creating automated training pipelines with hyperparameter tuning and configuring inference endpoints with auto-scaling.*

- **10% Leadership/Collaboration:** Focus on cross-functional communication, stakeholder delivery, or team enablement.
  Example: *Led client-facing engagements conducting technical workshops and presenting data solutions to business stakeholders translating complex requirements into scalable architectures.*

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
Do not repeat the same action verb more than three times across the entire resume. Rotate through strong verbs: Architected, Built, Designed, Deployed, Engineered, Implemented, Developed, Optimized, Automated, Integrated, Configured, Orchestrated, Trained, Created, Established, Managed, Led, Collaborated.

---

## 3. ATS OPTIMIZATION AND THE OR CONDITION

- **Mutually Exclusive Tools:** If the Job Description lists competing technologies as an "OR" condition (e.g., AWS/GCP/Azure, or Tableau/Power BI), choose ONE primary tool that fits the profile best. Do not list competing ecosystems in the same bullet.
- **Baseline Competency:** Assume baseline competence. Unless explicitly demanded by the JD, NEVER mention basic tools like Jupyter Notebooks, A/B Testing, basic regressions, or dbt in bullets. These dilute senior credibility.
- **Generic Cloud Reference:** Write "AWS" instead of listing "AWS (S3, Lambda, EC2)" unless a specific sub-service is vital to the bullet's technical point. Never parenthetically list cloud sub-services just for keyword stuffing.
- **Skills Section Alignment:** The skills section should mirror the JD's priority order. If the JD leads with Python and ML frameworks, the skills section should lead with those — not cloud platforms.
- **One Cloud Per Company (CRITICAL):** Each company in the resume must use exactly ONE cloud ecosystem. NEVER mix AWS, Azure, and GCP within the same role. If the JD lists clouds as an OR condition (e.g., "AWS/Azure/GCP"), keep AWS as default — our strongest stack is AWS. Only switch to Azure or GCP when the JD clearly emphasizes that specific cloud (appears 5+ times, or listed as "required"). If switching, assign different clouds to different companies (e.g., Bee Data = Azure, Allied Health = AWS). BYJU'S always stays GCP. Cognizant has no cloud.
- **Skills Section Cloud Format:** Cloud must be ONE combined category: "Cloud Platforms: AWS (SageMaker, EKS, Lambda, S3, Bedrock), GCP (BigQuery, Dataproc, Vertex AI)". Do NOT split into separate "Cloud AI Services" and "Cloud Infrastructure" categories. Only list cloud platforms that actually appear in the resume bullets.

---

## 4. CHRONOLOGICAL REALITY (THE ANTI-HALLUCINATION RULE)

- **The Time-Travel Constraint:** NEVER place modern Generative AI concepts (GPT-4, Claude, RAG, Vector Databases, LangChain, Agentic Workflows, Prompt Engineering) into roles dated before 2022. Map older roles strictly to what was realistic at that time: foundational data engineering, SQL, ETL, standard ML (Scikit-learn, XGBoost), UI components, or database administration.
- **Scoring Exclusion:** The Scorer MUST NOT penalize older jobs (pre-2022) for missing modern AI or GenAI keywords from the JD. These roles exist to show career foundation, not to mirror current requirements.
- **Technology Timeline Awareness:** Cognizant (Jun 2018-Oct 2021) should reflect Python 3.7-3.8, basic ML, SSIS, SQL Server, early cloud. BYJU'S (Oct 2021-Aug 2023) can include ML pipelines, GCP services, PySpark, Scikit-learn, XGBoost, and basic model training — but NOT GenAI, LLMs, RAG, LangChain, or agentic concepts. Only Bee Data and Allied Health (2023 onward) should include GenAI technologies.

---

## 5. PROJECT ADAPTATION BY ROLE LENS

The Writer Agent must adapt the framing of the same project based on the target role specified in the JD. The underlying work stays the same — the lens through which it is described changes.

- **AI Engineer Lens:** Frame around LLM integration, agentic workflows, model deployment, vector retrieval, orchestration, and inference infrastructure.
- **Data Scientist Lens:** Frame around statistical modeling, feature engineering, experiment design, model evaluation, data pipelines, and business-driven analysis.
- **Data Engineer Lens:** Frame around ETL/ELT pipelines, data warehouse design, batch and streaming processing, data quality, and platform infrastructure.
- **Software Engineer Lens:** Frame around backend systems, API design, microservices, scalability, event-driven architecture, and system reliability.
- **ML Engineer Lens:** Frame around training pipelines, model optimization, MLOps, deployment automation, monitoring, and production ML systems.

The role lens affects vocabulary choice, which aspects of a project get emphasized, and how results are framed — but it must never invent work that did not happen.

---

## 6. CONTRACT EXECUTION MODE

### Philosophy
A contract resume is a delivery proof document. The vendor recruiter and the hiring manager both need to see that this person can walk into an unfamiliar environment, understand the problem fast, and ship working solutions. Every bullet should answer: "What did you build, what did you use, and what did it achieve?"

### Specific Rules for Contract Mode

**A. Technical Density**
- Bullets should be implementation-specific. Name the tools, name the architecture decisions, name the infrastructure choices.
- It is acceptable (and expected) to go one level deeper on technical details compared to a fulltime resume. If you configured auto-scaling on EKS with 3-5 pods behind an ALB, say so. If you used Docker multi-stage builds, say so.
- Implementation mechanics matter: deployment strategies, scaling configurations, caching layers, monitoring setups, connection pooling, cost optimizations — these demonstrate that you did the work, not just designed it on a whiteboard.

**B. Tool Breadth**
- Contract resumes can mention a wider range of tools across the resume because vendor recruiters expect contractors to operate across stacks and environments.
- Strategic repetition of core JD terms (e.g., AWS, Python, FastAPI, RAG) across multiple bullets is acceptable to maximize ATS keyword density. But each repetition must be in a meaningfully different context — not copy-paste.
- The Environment line at the end of each company section (handled by the template) should list the full technology stack used during that engagement.

**C. JD Alignment Strategy**
- Align aggressively to the JD. Vendor screens and recruiter keyword searches are the first gate. If the JD says "PySpark" and the candidate used PySpark, it must appear explicitly — not hidden behind a generic "data processing" phrase.
- Mirror the JD's exact terminology wherever possible. If the JD says "ML pipelines," write "ML pipelines" — not "machine learning workflows."
- Core JD technologies should appear in the first 3-4 bullets of the most recent role because that is where recruiter eyes land first.

**D. Metric Style**
- Metrics should prove delivery speed, optimization results, migration success, and measurable output within defined engagements.
- Operational metrics work best: latency numbers, uptime percentages, cost reductions, processing volumes, accuracy scores, user counts.
- Example: "reducing monthly AWS costs from $500 to $250" — this is a contract-style metric because it shows you optimized something concrete within a short period.

**E. Ownership Framing**
- Ownership in a contract context means solving a technical problem end-to-end within a defined engagement. Frame bullets as "I built this complete thing" rather than "I contributed to an ongoing initiative."
- Avoid language that implies long-term stewardship ("maintained over 2 years," "evolved the platform roadmap"). Instead, frame as delivery: "Architected and deployed," "Built and optimized," "Designed and implemented."

**F. Bullet Count Guidance**
- Recent roles (last 2 companies) can have 12-15 bullets each to demonstrate depth and breadth of delivery.
- Older roles should have 7-10 bullets focused on foundational skills relevant to the JD.
- The Scorer MUST NOT penalize contract resumes for having more bullets than a typical fulltime resume.

**G. Persona Signal**
- The contract resume should signal: specialist, fast adapter, delivery-focused, technically confident.
- Avoid language that signals "I'm looking for a home" or "I want to grow with your team." Contract recruiters want someone who can execute immediately.

---

## 7. SUMMARY SECTION RULES

- The summary should contain 6-10 bullets covering the candidate's strongest capabilities.
- Each summary bullet must be a standalone statement — not a continuation of the previous one.
- Summary bullets should cover a mix of: core technical strength, domain experience, platform expertise, methodology, and delivery maturity.
- Do NOT use the summary to restate what is already obvious from the experience section. Use it to frame the candidate's professional identity at a glance.
- Avoid vague openers like "Results-driven professional" or "Passionate about technology." Start each summary bullet with a concrete capability or experience signal.

---

## 8. SKILLS SECTION RULES

- Group skills into logical categories (Programming, AI Frameworks, Machine Learning, Cloud Platforms, Databases, etc.).
- Order the categories to mirror the JD's priority. If the JD leads with Python and ML, the skills section should lead with Programming and Machine Learning — not Cloud Platforms.
- Do not list more than 8-10 items per category. Overcrowding dilutes credibility.
- Only list tools and technologies that appear in the resume_details file or are directly mappable via the cloud adaptability rules. Never invent skills.
- If the JD uses a specific tool name (e.g., "Databricks"), and the candidate has equivalent experience (e.g., "PySpark on EMR"), list the JD's tool name in the skills section and use the adapted version in the bullets.

---

## 9. TEMPLATE AWARENESS (WHAT THE WRITER AGENT FILLS vs WHAT IS FIXED)

The contract template has fixed elements and fillable placeholders. The Writer Agent ONLY generates content for the placeholders listed below. Everything else is pre-formatted in the template and must NOT be generated.

### Fixed in Template (DO NOT generate)
- Candidate name, email, phone, LinkedIn, GitHub, location
- Company names, company locations, employment dates
- Role titles (AI Engineer, AI/ML Engineer, Data Engineer, Program Analyst)
- Section headings (SUMMARY, TECHNICAL SKILLS, PROFESSIONAL EXPERIENCE, EDUCATION)
- Horizontal divider lines
- Education section (university names, degrees, coursework, dates)

### Placeholders the Writer Agent Fills

**[[Summary]]** — A list of bullet points (6-10 bullets). Each bullet is a separate item. Do not include bullet symbols — the template handles bullet formatting.

**[[Technical Skills]]** — Formatted as category-value pairs, one per line:
```
Programming: Python 3.11+, SQL, JavaScript, TypeScript, Bash
AI Frameworks: LangChain, LangGraph, Hugging Face Transformers
Machine Learning: Scikit-learn, PyTorch, XGBoost
Cloud Platforms: AWS (SageMaker, EKS, Lambda, S3)
...
```
Each line starts with a bold category name followed by a colon and comma-separated items.

**[[Exp{N}_Description]]** — A 2-4 sentence paragraph describing the scope of the role at that company. This should cover what the candidate did at a high level: domains served, types of systems built, team collaboration model. Maximum 2 lines when rendered. This placeholder exists for all 4 experience sections (Exp1 through Exp4).

**[[Exp{N}]]** — A list of bullet points for that company's experience. Each bullet is a separate item. Do not include bullet symbols. Follow the bullet count guidance from Section 6F.

**[[Exp{N}_Env]]** — A single comma-separated line listing all technologies used in that role. Format: `Environment: Python 3.11 (Pandas, NumPy, Scikit-learn, PyTorch, ...), AWS (EKS, Lambda, SageMaker, ...), LangChain, FastAPI, Docker, Kubernetes, ...`
The word "Environment" with a colon is part of the output. List Python version and sub-libraries in parentheses, cloud platform with sub-services in parentheses, then individual tools comma-separated.

---

## 10. WRITER AGENT OUTPUT FORMAT

The Writer Agent must return its output as a structured JSON object so the orchestrator can parse each placeholder and inject it into the template. The exact format:

```json
{
  "summary": [
    "First summary bullet text...",
    "Second summary bullet text...",
    "..."
  ],
  "technical_skills": [
    "Programming: Python 3.11+, SQL, JavaScript, TypeScript, Bash",
    "AI Frameworks: LangChain, LangGraph, Hugging Face Transformers",
    "..."
  ],
  "exp1_description": "Paragraph text for Bee Data role description...",
  "exp1": [
    "First bullet for Bee Data...",
    "Second bullet for Bee Data...",
    "..."
  ],
  "exp1_env": "Environment: Python 3.11 (Pandas, NumPy, ...), AWS (...), ...",
  "exp2_description": "Paragraph text for Allied Health role description...",
  "exp2": ["..."],
  "exp2_env": "Environment: ...",
  "exp3_description": "Paragraph text for BYJU'S role description...",
  "exp3": ["..."],
  "exp3_env": "Environment: ...",
  "exp4_description": "Paragraph text for Cognizant role description...",
  "exp4": ["..."],
  "exp4_env": "Environment: ..."
}
```

Rules for the output:
- Each bullet in summary, exp1, exp2, exp3, exp4 arrays must be a plain text string with NO bullet symbols, NO numbering, and NO leading dashes.
- Technical skills lines must have the category name followed by a colon and space, then comma-separated items.
- Description fields must be plain paragraph text (no bullets, no line breaks).
- Environment fields must be a single line starting with "Environment:" followed by the tool list.
- Return ONLY the JSON object. No preamble, no markdown, no explanation.

---

## 11. WRITER AGENT BEHAVIORAL RULES

1. **Read the JD first** — identify required skills, tools, cloud platform, role type, and seniority level before writing anything.
2. **Select relevant experience** — pick bullets and projects from resume_details that best match the JD requirements.
3. **Adapt cloud platform** — analyze the JD to determine which cloud is primary. If clouds are listed as OR condition, keep AWS as default. Only switch if the JD clearly emphasizes a different cloud. Use the mapping tables in resume_details for 1:1 service swaps. Each company stays on ONE cloud.
4. **Adapt tools** — if the JD mentions specific tools (Airflow, Databricks, Snowflake, etc.), swap equivalents from resume_details.
5. **Apply role lens** — frame bullets through the appropriate role lens (AI Engineer, Data Scientist, Data Engineer, Software Engineer, ML Engineer) based on the JD title.
6. **Do not invent** — only use experience, skills, and projects listed in resume_details. Never fabricate metrics, tools, or outcomes.
7. **Match JD language** — mirror the JD's terminology in bullets and skills section.
8. **Respect chronology** — never place modern AI concepts in pre-2022 roles.
9. **Fill template placeholders** — map content to the exact placeholders in the contract template ({{Summary}}, {{Skills}}, {{Exp1}}, {{Exp2}}, etc.).
10. **Quality over quantity** — every bullet must earn its place. If a bullet does not serve the JD match or the career narrative, remove it.
