import React, { useState } from 'react'

const WORK_AUTH = {
  contract: "I am on an H1B visa and can work on W2 as well.",
  fulltime: "I am on an H1B visa and can work on W2 as well.",
  gc: "I hold a Green Card and am authorized to work in the US without sponsorship.",
}

function getColor(s) { return s >= 90 ? '#059669' : s >= 80 ? '#2563eb' : s >= 70 ? '#d97706' : '#dc2626' }

function extractCoreSkills(jd) {
  const patterns = [
    /(?:mandatory|required|must.have|key|essential)\s*(?:skills|qualifications|requirements)\s*[:\-]?\s*([\s\S]*?)(?:\n\s*\n|preferred|nice|bonus|$)/i,
    /(?:responsibilities|what you.ll do|requirements)\s*[:\-]?\s*([\s\S]*?)(?:\n\s*\n|preferred|qualifications|$)/i,
  ]
  for (const p of patterns) {
    const m = jd.match(p)
    if (m) {
      const terms = m[1].match(/\b(?:Python|SQL|PySpark|PyTorch|TensorFlow|NLP|LLM|LLMs|RAG|AWS|Azure|GCP|Kubernetes|Docker|Spark|Kafka|Airflow|Snowflake|Databricks|FastAPI|LangChain|ML|AI|GenAI|Tableau|Power BI|Scikit.learn|Pandas|React|BigQuery|PostgreSQL|Redis|Pinecone|Terraform|MLflow|Hugging Face|Transformers|Deep Learning|Machine Learning|Computer Vision)\b/gi)
      if (terms) return [...new Set(terms.map(t => t.trim()))].slice(0, 4)
    }
  }
  return []
}

function buildEmailBody(name, role, location, jobType, jd) {
  const auth = WORK_AUTH[jobType] || WORK_AUTH.contract
  const first = name.split(' ')[0] || 'Hi'
  const skills = extractCoreSkills(jd)
  const skillsLine = skills.length > 0 ? skills.join(', ') : 'the core requirements listed'
  const locLine = location ? `\nWork Location: ${location}` : ''

  return `Hi ${first},

I came across the ${role || 'open position'} role${location ? ' in ' + location : ''} and wanted to express my interest.

The role aligns well with my background — I have hands-on experience with ${skillsLine} in production environments and have delivered real-world solutions in these areas.

Role: ${role || 'As mentioned'}${locLine}
Work Authorization: ${auth}

I have attached my resume for your review. Please let me know if you would like to schedule a call to discuss further.

Best regards,
Srikanth`
}

function CopyButton({ label, text }) {
  const [copied, setCopied] = useState(false)
  const handleCopy = () => {
    navigator.clipboard.writeText(text).then(() => {
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    })
  }
  return (
    <button onClick={handleCopy} style={{
      flex: 1, padding: '8px', background: copied ? '#059669' : '#f3f4f6',
      color: copied ? '#fff' : '#374151', border: '1px solid #d1d5db',
      borderRadius: '6px', fontSize: '12px', fontWeight: '600',
      cursor: 'pointer', transition: 'all 0.2s',
    }}>
      {copied ? '✓ Copied' : label}
    </button>
  )
}

export default function ResultPanel({ result, jobType }) {
  const [showLogs, setShowLogs] = useState(false)
  const [email, setEmail] = useState({
    to: result.recruiter_email || '',
    name: result.recruiter_name || '',
    role: result.job_title || '',
    location: result.work_location || '',
  })

  const delta = result.iteration_2_score - result.iteration_1_score
  const emailSubject = `Application for ${email.role || 'the open position'} - Srikanth Manchimchetty`
  const emailBody = buildEmailBody(email.name, email.role, email.location, jobType, '')
  const mailtoUrl = `mailto:${email.to}?subject=${encodeURIComponent(emailSubject)}&body=${encodeURIComponent(emailBody)}`

  const inp = { width: '100%', padding: '8px 10px', border: '1px solid #d1d5db', borderRadius: '6px', fontSize: '13px', fontFamily: 'inherit', outline: 'none', boxSizing: 'border-box' }
  const lbl = { fontSize: '11px', fontWeight: '600', color: '#6b7280', marginBottom: '3px', display: 'block' }

  return (
    <div style={{ marginTop: '24px', border: '1px solid #e5e7eb', borderRadius: '12px', overflow: 'hidden' }}>

      {/* ── Score ── */}
      <div style={{ padding: '24px', textAlign: 'center', borderBottom: '1px solid #e5e7eb' }}>
        <p style={{ fontSize: '13px', fontWeight: '600', color: '#6b7280', textTransform: 'uppercase', letterSpacing: '0.05em', margin: '0 0 8px' }}>Final ATS Score</p>
        <p style={{ fontSize: '48px', fontWeight: '800', margin: '0', color: getColor(result.ats_score) }}>{result.ats_score}</p>
        {result.score_reasoning && <p style={{ fontSize: '14px', color: '#4b5563', margin: '8px auto 0', lineHeight: '1.5', maxWidth: '600px' }}>{result.score_reasoning}</p>}
      </div>

      {/* ── Download ── */}
      <div style={{ padding: '16px 24px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', borderBottom: '1px solid #e5e7eb', background: '#f9fafb' }}>
        <span style={{ fontSize: '14px', fontWeight: '500', color: '#374151' }}>{result.filename}</span>
        <a href={result.download_url} download style={{ padding: '10px 20px', background: '#111827', color: '#fff', border: 'none', borderRadius: '6px', fontSize: '14px', fontWeight: '600', textDecoration: 'none' }}>Download .docx</a>
      </div>

      {/* ── Email Recruiter ── */}
      <div style={{ padding: '16px 24px', borderBottom: '1px solid #e5e7eb' }}>
        <div style={{ fontSize: '13px', fontWeight: '600', color: '#374151', marginBottom: '12px' }}>Email Recruiter</div>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px', marginBottom: '10px' }}>
          <div>
            <label style={lbl}>Recruiter Email</label>
            <input style={inp} value={email.to} onChange={e => setEmail(p => ({ ...p, to: e.target.value }))} placeholder="recruiter@company.com" />
          </div>
          <div>
            <label style={lbl}>Recruiter Name</label>
            <input style={inp} value={email.name} onChange={e => setEmail(p => ({ ...p, name: e.target.value }))} placeholder="John Smith" />
          </div>
          <div>
            <label style={lbl}>Role Name</label>
            <input style={inp} value={email.role} onChange={e => setEmail(p => ({ ...p, role: e.target.value }))} placeholder="Senior AI Engineer" />
          </div>
          <div>
            <label style={lbl}>Work Location</label>
            <input style={inp} value={email.location} onChange={e => setEmail(p => ({ ...p, location: e.target.value }))} placeholder="Remote / New York, NY" />
          </div>
        </div>

        {/* mailto — opens Gmail app on mobile */}
        <a href={mailtoUrl}
          style={{ display: 'block', padding: '10px', background: '#2563eb', color: '#fff', border: 'none', borderRadius: '6px', fontSize: '14px', fontWeight: '600', textDecoration: 'none', textAlign: 'center', cursor: 'pointer', marginBottom: '8px' }}>
          Email Recruiter
        </a>

        {/* Copy buttons — for desktop where mailto opens Outlook */}
        <div style={{ display: 'flex', gap: '6px' }}>
          <CopyButton label="Copy Email" text={email.to} />
          <CopyButton label="Copy Subject" text={emailSubject} />
          <CopyButton label="Copy Body" text={emailBody} />
        </div>

        <p style={{ fontSize: '11px', color: '#9ca3af', margin: '6px 0 0', lineHeight: '1.4' }}>
          Mobile: "Email Recruiter" opens Gmail app with composed email. Desktop: use copy buttons to paste into Gmail tab.
          {jobType === 'gc' ? ' Work auth: Green Card.' : ' Work auth: H1B + W2.'}
        </p>
      </div>

      {/* ── Iteration Comparison ── */}
      <div style={{ padding: '16px 24px', borderBottom: '1px solid #e5e7eb' }}>
        <div style={{ fontSize: '13px', fontWeight: '600', color: '#374151', marginBottom: '12px' }}>Pipeline Details</div>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
          <div style={{ padding: '12px', background: '#f9fafb', borderRadius: '8px', border: '1px solid #e5e7eb' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
              <span style={{ fontSize: '12px', fontWeight: '600', color: '#6b7280', textTransform: 'uppercase' }}>Draft</span>
              <span style={{ fontSize: '20px', fontWeight: '700', color: getColor(result.iteration_1_score) }}>{result.iteration_1_score}</span>
            </div>
            <div style={{ fontSize: '12px', color: '#6b7280' }}>{result.iteration_1_feedback_count} issues found</div>
            {result.iteration_1_reasoning && <div style={{ fontSize: '12px', color: '#4b5563', lineHeight: '1.4', marginTop: '6px' }}>{result.iteration_1_reasoning}</div>}
            {result.iteration_1_top_fixes?.length > 0 && (
              <ol style={{ margin: '6px 0 0', padding: '0 0 0 16px', fontSize: '12px', color: '#4b5563', lineHeight: '1.5' }}>
                {result.iteration_1_top_fixes.map((f, i) => <li key={i}>{f}</li>)}
              </ol>
            )}
          </div>
          <div style={{ padding: '12px', background: '#f9fafb', borderRadius: '8px', border: '1px solid #e5e7eb' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
              <span style={{ fontSize: '12px', fontWeight: '600', color: '#6b7280', textTransform: 'uppercase' }}>Final</span>
              <span style={{ fontSize: '20px', fontWeight: '700', color: getColor(result.iteration_2_score) }}>{result.iteration_2_score}</span>
            </div>
            <div style={{ fontSize: '12px', color: '#6b7280' }}>{result.iteration_2_feedback_count} issues remaining</div>
            {result.iteration_2_reasoning && <div style={{ fontSize: '12px', color: '#4b5563', lineHeight: '1.4', marginTop: '6px' }}>{result.iteration_2_reasoning}</div>}
          </div>
        </div>
        <div style={{ fontSize: '13px', fontWeight: '600', textAlign: 'center', padding: '6px 0', color: delta > 0 ? '#059669' : delta < 0 ? '#dc2626' : '#6b7280' }}>
          {delta > 0 ? `+${delta} improvement` : delta < 0 ? `${delta} regression (used draft)` : 'No change between iterations'}
        </div>
      </div>

      {/* ── Pipeline Logs ── */}
      <div style={{ padding: '16px 24px' }}>
        <button onClick={() => setShowLogs(!showLogs)} style={{ fontSize: '13px', fontWeight: '600', color: '#6b7280', cursor: 'pointer', background: 'none', border: 'none', padding: '0', fontFamily: 'inherit' }}>
          {showLogs ? '▾ Hide' : '▸ Show'} Pipeline Logs
        </button>
        {showLogs && (
          <div style={{ marginTop: '8px', padding: '12px', background: '#f9fafb', borderRadius: '6px', fontSize: '12px', fontFamily: '"SF Mono", Monaco, monospace', color: '#374151', lineHeight: '1.7', maxHeight: '200px', overflowY: 'auto' }}>
            {result.logs.map((l, i) => <p key={i} style={{ margin: 0 }}>{l}</p>)}
          </div>
        )}
      </div>
    </div>
  )
}
