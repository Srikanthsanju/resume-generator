# FULLTIME RESUME WRITING GUIDELINES
# ================================================
# MODE: FULLTIME (5-Year Experience / Startup-Friendly / Long-Term Fit)
# PURPOSE: This file governs how the Writer Agent writes fulltime resumes.
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
  Example: *Designed RAG pipeline applying context engineering techniques defining chunking strategies and vector retrieval configuration improving LLM grounding accuracy for policy recommendations.*

- **30% Design Structure:** `Action` + `Tool/System` (Focus on architecture and ownership decisions)
  Example: *Implemented MLOps practices using MLflow managing experiment tracking and model versioning coordinating CI/CD pipelines with GitHub Actions automating evaluation gates.*

- **10% Leadership/Collaboration:** Focus on cross-functional teamwork, alignment with business goals, or mentoring.
  Example: *Collaborated with ML engineers and product owners translating ambiguous business requirements into well-defined ML problems delivering production-ready solutions aligned with team OKRs.*

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
Do not repeat the same action verb more than twice across the entire resume. Rotate through strong verbs: Architected, Built, Designed, Deployed, Engineered, Implemented, Developed, Optimized, Automated, Integrated, Configured, Orchestrated, Trained, Created, Established, Managed, Led, Collaborated.

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
- **Technology Timeline Awareness:** Cognizant (Jun 2020-Oct 2021) should reflect Python 3.7-3.8, basic ML, SSIS, SQL Server, early cloud. BYJU'S (Oct 2021-Aug 2023) can include ML pipelines, GCP services, PySpark, Scikit-learn, XGBoost, and basic model training — but NOT GenAI, LLMs, RAG, LangChain, or agentic concepts. Only Bee Data and Allied Health (2023 onward) should include GenAI technologies.

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

## 6. FULLTIME EXECUTION MODE

### Philosophy
A fulltime resume is an ownership and maturity document. The hiring manager needs to see that this person thinks clearly, owns systems over time, and operates well within a team. Every bullet should answer: "What do you own, how do you think about it, and what sustained impact did it create?"

### Specific Rules for Fulltime Mode

**A. Technical Depth Over Technical Breadth**
- Bullets should show conceptual depth rather than implementation laundry lists. Instead of naming every infrastructure component, emphasize the design thinking and the reasoning behind technical choices.
- Go deeper on fewer concepts rather than wider across more tools. If you designed a RAG pipeline, talk about the chunking strategy and retrieval configuration — not the 8 AWS services that run underneath it.
- The reader should walk away thinking "this person genuinely understands these systems" rather than "this person has touched 30 tools."

**B. Tool Selectivity**
- Fulltime resumes should be selective about tool mentions. Too many tools across the resume can make the candidate look unfocused or keyword-stuffed.
- Only mention tools that are central to the bullet's point. If a tool is just infrastructure plumbing (load balancers, CDNs, caching layers), omit it unless it is specifically demanded by the JD.
- The resume should feel clean and uncluttered. Every tool mention should earn its place by serving the narrative, not the ATS.

**C. JD Alignment Strategy**
- Align well to the JD, but not by stuffing. Fulltime recruiters care more about whether the story of the resume feels coherent and believable than whether every JD keyword appears somewhere.
- If a JD keyword fits naturally into an existing bullet, include it. If forcing a keyword makes a bullet awkward or dishonest, leave it out.
- The resume should tell a career story that makes sense — each role building on the previous one, each company adding new capabilities. If that story aligns with the JD, the recruiter will see it.

**D. Metric Style**
- Metrics should demonstrate sustained business impact, efficiency improvements, process maturity, or team-level influence over time.
- Outcome-oriented metrics work best: user adoption, accuracy improvements, workload reductions, time savings, cost efficiency through smart design.
- Example: "reducing support workload by 40%" — this is a fulltime-style metric because it shows a sustained operational improvement, not a one-time optimization sprint.
- Avoid over-quantifying. Not every bullet needs a number. A well-framed design decision bullet with no metric can be more credible than a forced "improving X by Y%" that sounds fabricated.

**E. Ownership Framing**
- Ownership in a fulltime context means sustained responsibility over systems, business processes, or platform health over time. Frame bullets as "I own this system and its evolution" rather than "I built this thing and shipped it."
- Language that signals long-term thinking is valuable: "managing model lifecycle," "coordinating CI/CD pipelines," "establishing automated retraining triggers," "aligning deliverables with business OKRs."
- It is natural for fulltime bullets to mention cross-functional collaboration, alignment with product goals, or working within agile team structures. These signal that the person operates well within an organization.

**F. Bullet Count Guidance**
- Recent roles (last 2 companies) should have 10-12 carefully selected bullets each. Fewer, stronger bullets signal maturity and editorial judgment.
- Older roles should have 6-9 bullets focused on foundational skills relevant to the JD.
- The Scorer should evaluate whether each bullet contributes meaningfully to the JD match and career narrative. Filler bullets weaken the overall impression.

**G. Persona Signal**
- The fulltime resume should signal: thoughtful builder, long-term owner, team player, technically mature.
- Language should feel calm, confident, and grounded. The resume should read like someone who has earned their expertise through sustained work, not someone trying to prove themselves through keyword volume.
- It is appropriate to mention collaboration, team dynamics, individual contributor positioning, and alignment with business objectives. These are signals that fulltime hiring managers actively look for.

**H. Readability and Clean Feel**
- Fulltime resumes should feel visually clean and easy to scan. Bullets should breathe — avoid packing too many concepts into a single sentence.
- If a bullet reads like a run-on sentence with 5 clauses, split the idea into two cleaner bullets or trim the less important parts.
- The resume should feel like a conversation with a competent professional — not like reading a technical specification document.

---

## 7. SUMMARY SECTION RULES

- The summary should contain 5-8 bullets covering the candidate's professional identity and strongest capabilities.
- Each summary bullet must be a standalone statement — not a continuation of the previous one.
- Summary bullets should frame who the candidate is and how they think — not just list tools they know.
- Cover a mix of: core professional identity, domain experience, methodology and approach, collaboration style, and growth trajectory.
- Avoid vague openers like "Results-driven professional" or "Passionate about technology." Start each summary bullet with a concrete capability or experience signal.
- The summary should read like a professional identity statement, not a capabilities catalog. The reader should finish the summary knowing what kind of engineer this person is, not just what they can do.

---

## 8. SKILLS SECTION RULES

- Group skills into logical categories (Programming, AI Frameworks, Machine Learning, Cloud Platforms, Databases, etc.).
- Order the categories to mirror the JD's priority. If the JD leads with Python and ML, the skills section should lead with Programming and Machine Learning — not Cloud Platforms.
- Do not list more than 6-8 items per category. Keep it focused — a shorter, curated skills section signals confidence and clarity.
- Only list tools and technologies that appear in the resume_details file or are directly mappable via the cloud adaptability rules. Never invent skills.
- If the JD uses a specific tool name (e.g., "Databricks"), and the candidate has equivalent experience (e.g., "PySpark on EMR"), list the JD's tool name in the skills section and use the adapted version in the bullets.
- Avoid listing too many competing tools in the same category. If the JD asks for one cloud platform, list that one prominently — not three.

---

## 9. TEMPLATE AWARENESS (WHAT THE WRITER AGENT FILLS vs WHAT IS FIXED)

The fulltime template has fixed elements and fillable placeholders. The Writer Agent ONLY generates content for the placeholders listed below. Everything else is pre-formatted in the template and must NOT be generated.

### Fixed in Template (DO NOT generate)
- Candidate name, email, phone, LinkedIn, GitHub, location
- Company names, company locations, employment dates
- Role titles (AI Engineer, AI/ML Engineer, Data Engineer, Program Analyst)
- Section headings (SUMMARY, TECHNICAL SKILLS, PROFESSIONAL EXPERIENCE, EDUCATION)
- Horizontal divider lines
- Education section (university names, degrees, coursework, dates)

### Placeholders the Writer Agent Fills

**[[Summary]]** — A list of bullet points (5-8 bullets). Each bullet is a separate item. Do not include bullet symbols — the template handles bullet formatting.

**[[Technical Skills]]** — Formatted as category-value pairs, one per line:
```
Programming: Python 3.11+ (Pandas, NumPy), TypeScript, SQL, Bash
GenAI and LLMs: GPT-4, Claude, RAG Architectures, Prompt Engineering
AI Frameworks: LangChain (LangGraph, Tool Calling), LlamaIndex
...
```
Each line starts with a bold category name followed by a colon and comma-separated items.

**[[Exp{N}]]** — A list of bullet points for that company's experience. Each bullet is a separate item. Do not include bullet symbols. Follow the bullet count guidance from Section 6F.

NOTE: The fulltime template does NOT have [[Exp{N}_Description]] or [[Exp{N}_Env]] placeholders. The Writer Agent must NOT generate role description paragraphs or environment lines for fulltime resumes. The bullets themselves carry the full narrative.

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
    "Programming: Python 3.11+ (Pandas, NumPy), TypeScript, SQL, Bash",
    "GenAI and LLMs: GPT-4, Claude, RAG Architectures, Prompt Engineering",
    "..."
  ],
  "exp1": [
    "First bullet for Bee Data...",
    "Second bullet for Bee Data...",
    "..."
  ],
  "exp2": [
    "First bullet for Allied Health...",
    "..."
  ],
  "exp3": [
    "First bullet for BYJU'S...",
    "..."
  ],
  "exp4": [
    "First bullet for Cognizant...",
    "..."
  ]
}
```

Rules for the output:
- Each bullet in summary, exp1, exp2, exp3, exp4 arrays must be a plain text string with NO bullet symbols, NO numbering, and NO leading dashes.
- Technical skills lines must have the category name followed by a colon and space, then comma-separated items.
- Return ONLY the JSON object. No preamble, no markdown, no explanation.

---

## 11. WRITER AGENT BEHAVIORAL RULES

1. **Read the JD first** — identify required skills, tools, cloud platform, role type, and seniority level before writing anything.
2. **Select relevant experience** — pick bullets and projects from resume_details that best match the JD requirements.
3. **Adapt cloud platform** — analyze the JD to determine which cloud is primary. If clouds are listed as OR condition, keep AWS as default. Only switch if the JD clearly emphasizes a different cloud. Use the mapping tables in resume_details for 1:1 service swaps. Each company stays on ONE cloud.
4. **Adapt tools** — if the JD mentions specific tools (Airflow, Databricks, Snowflake, etc.), swap equivalents from resume_details.
5. **Apply role lens** — frame bullets through the appropriate role lens (AI Engineer, Data Scientist, Data Engineer, Software Engineer, ML Engineer) based on the JD title.
6. **Do not invent** — only use experience, skills, and projects listed in resume_details. Never fabricate metrics, tools, or outcomes.
7. **Match JD language** — mirror the JD's terminology in bullets and skills section, but only where it fits naturally.
8. **Respect chronology** — never place modern AI concepts in pre-2022 roles.
9. **Fill template placeholders** — map content to the exact placeholders in the fulltime template ({{Summary}}, {{Skills}}, {{Exp1}}, {{Exp2}}, etc.).
10. **Edit ruthlessly** — every bullet must earn its place. A fulltime resume with 10 strong bullets beats one with 15 mediocre bullets. If a bullet does not serve the JD match or the career story, remove it.
