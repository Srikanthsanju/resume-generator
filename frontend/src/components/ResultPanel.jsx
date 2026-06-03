import React, { useState } from 'react'

const WORK_AUTH = { contract: "H1B visa, can work on W2.", fulltime: "H1B visa, can work on W2.", gc: "Green Card holder, no sponsorship needed." }

function getColor(s) { return s >= 90 ? '#059669' : s >= 80 ? '#2563eb' : s >= 70 ? '#d97706' : '#dc2626' }
function getDriftColor(s) { return s <= 10 ? '#059669' : s <= 25 ? '#2563eb' : s <= 50 ? '#d97706' : '#dc2626' }

function copyToClipboard(text) {
  if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text)
  return new Promise((resolve, reject) => {
    const el = document.createElement('textarea')
    el.value = text; el.style.position = 'fixed'; el.style.left = '-9999px'
    document.body.appendChild(el); el.focus(); el.select()
    try { document.execCommand('copy') ? resolve() : reject() }
    catch (e) { reject(e) }
    finally { document.body.removeChild(el) }
  })
}

function CopyBtn({ label, text }) {
  const [ok, setOk] = useState(false)
  return <button onClick={() => copyToClipboard(text).then(() => { setOk(true); setTimeout(() => setOk(false), 2000) }).catch(() => window.prompt('Copy:', text))}
    style={{ flex: 1, padding: '8px', background: ok ? '#059669' : '#f3f4f6', color: ok ? '#fff' : '#374151', border: '1px solid #d1d5db', borderRadius: '6px', fontSize: '12px', fontWeight: '600', cursor: 'pointer' }}>
    {ok ? '✓ Copied' : label}
  </button>
}

function ScoreBar({ label, score, isDrift }) {
  const color = isDrift ? getDriftColor(score) : getColor(score)
  return <div style={{ marginBottom: '6px' }}>
    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '12px', marginBottom: '2px' }}>
      <span style={{ color: '#6b7280' }}>{label}</span><span style={{ fontWeight: '700', color }}>{score}</span>
    </div>
    <div style={{ height: '6px', background: '#e5e7eb', borderRadius: '3px' }}>
      <div style={{ height: '6px', background: color, borderRadius: '3px', width: `${isDrift ? 100 - score : score}%`, transition: 'width 0.5s' }} />
    </div>
  </div>
}

export default function ResultPanel({ result, jobType, recruiter, onReset }) {
  const [showLogs, setShowLogs] = useState(false)
  const [email, setEmail] = useState({ to: recruiter?.recruiter_email || '', name: recruiter?.recruiter_name || '', role: recruiter?.job_title || '', location: recruiter?.work_location || '' })

  const delta = (result.iteration_2_score || 0) - (result.iteration_1_score || 0)
  const scores = result.scores || result.iteration_2_scores || {}
  const subject = `Application for ${email.role || 'the open position'} - Srikanth Manchimchetty`
  const auth = WORK_AUTH[jobType] || WORK_AUTH.contract
  const body = `Hi ${(email.name || '').split(' ')[0] || 'Hi'},\n\nI came across the ${email.role || 'open position'} role${email.location ? ' in ' + email.location : ''} and wanted to express my interest. The role aligns well with my background and I have hands-on experience delivering production solutions in these areas.\n\nRole: ${email.role || 'As mentioned'}${email.location ? '\nWork Location: ' + email.location : ''}\nWork Authorization: ${auth}\n\nI have attached my resume for your review.\n\nBest regards,\nSrikanth`
  const mailto = `mailto:${email.to}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`

  const inp = { width: '100%', padding: '8px 10px', border: '1px solid #d1d5db', borderRadius: '6px', fontSize: '13px', fontFamily: 'inherit', outline: 'none', boxSizing: 'border-box' }
  const lbl = { fontSize: '11px', fontWeight: '600', color: '#6b7280', marginBottom: '3px', display: 'block' }

  return (
    <div style={{ marginTop: '24px', border: '1px solid #e5e7eb', borderRadius: '12px', overflow: 'hidden' }}>

      {/* Score + 5 bars */}
      <div style={{ padding: '24px', borderBottom: '1px solid #e5e7eb' }}>
        <div style={{ textAlign: 'center', marginBottom: '16px' }}>
          <p style={{ fontSize: '13px', fontWeight: '600', color: '#6b7280', textTransform: 'uppercase', margin: '0 0 4px' }}>Final ATS Score</p>
          <p style={{ fontSize: '48px', fontWeight: '800', margin: '0', color: getColor(result.ats_score) }}>{result.ats_score}</p>
          {result.pass === false && <p style={{ fontSize: '12px', color: '#dc2626', fontWeight: '600', margin: '4px 0 0' }}>⚠ Did not pass hard fail conditions</p>}
          {result.pass === true && <p style={{ fontSize: '12px', color: '#059669', fontWeight: '600', margin: '4px 0 0' }}>✓ Passed all quality checks</p>}
        </div>
        {Object.keys(scores).length > 0 && <div style={{ maxWidth: '400px', margin: '0 auto' }}>
          <ScoreBar label="ATS Keyword Coverage" score={scores.ats_keyword_coverage || 0} />
          <ScoreBar label="Role Essence" score={scores.role_essence || 0} />
          <ScoreBar label="Believability" score={scores.believability || 0} />
          <ScoreBar label="Skill Proof" score={scores.skill_proof || 0} />
          <ScoreBar label="Role Drift Risk" score={scores.role_drift_risk || 0} isDrift />
        </div>}
        {result.score_reasoning && <p style={{ fontSize: '13px', color: '#4b5563', margin: '12px auto 0', lineHeight: '1.5', maxWidth: '600px', textAlign: 'center' }}>{result.score_reasoning}</p>}
      </div>

      {/* Download */}
      <div style={{ padding: '16px 24px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', borderBottom: '1px solid #e5e7eb', background: '#f9fafb' }}>
        <span style={{ fontSize: '14px', fontWeight: '500' }}>{result.filename}</span>
        <a href={result.download_url} download style={{ padding: '10px 20px', background: '#111827', color: '#fff', borderRadius: '6px', fontSize: '14px', fontWeight: '600', textDecoration: 'none' }}>Download .docx</a>
      </div>

      {/* Email */}
      <div style={{ padding: '16px 24px', borderBottom: '1px solid #e5e7eb' }}>
        <div style={{ fontSize: '13px', fontWeight: '600', color: '#374151', marginBottom: '12px' }}>Email Recruiter</div>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px', marginBottom: '10px' }}>
          <div><label style={lbl}>Email</label><input style={inp} value={email.to} onChange={e => setEmail(p => ({ ...p, to: e.target.value }))} placeholder="recruiter@co.com" /></div>
          <div><label style={lbl}>Name</label><input style={inp} value={email.name} onChange={e => setEmail(p => ({ ...p, name: e.target.value }))} placeholder="John" /></div>
          <div><label style={lbl}>Role</label><input style={inp} value={email.role} onChange={e => setEmail(p => ({ ...p, role: e.target.value }))} placeholder="GCP Data Engineer" /></div>
          <div><label style={lbl}>Location</label><input style={inp} value={email.location} onChange={e => setEmail(p => ({ ...p, location: e.target.value }))} placeholder="Charlotte, NC" /></div>
        </div>
        <a href={mailto} style={{ display: 'block', padding: '10px', background: '#2563eb', color: '#fff', borderRadius: '6px', fontSize: '14px', fontWeight: '600', textDecoration: 'none', textAlign: 'center', marginBottom: '8px' }}>Email Recruiter</a>
        <div style={{ display: 'flex', gap: '6px' }}>
          <CopyBtn label="Copy Email" text={email.to} />
          <CopyBtn label="Copy Subject" text={subject} />
          <CopyBtn label="Copy Body" text={body} />
        </div>
      </div>

      {/* Iterations */}
      <div style={{ padding: '16px 24px', borderBottom: '1px solid #e5e7eb' }}>
        <div style={{ fontSize: '13px', fontWeight: '600', color: '#374151', marginBottom: '12px' }}>Pipeline Details</div>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
          <div style={{ padding: '12px', background: '#f9fafb', borderRadius: '8px', border: '1px solid #e5e7eb' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '6px' }}>
              <span style={{ fontSize: '12px', fontWeight: '600', color: '#6b7280', textTransform: 'uppercase' }}>Draft</span>
              <span style={{ fontSize: '20px', fontWeight: '700', color: getColor(result.iteration_1_score) }}>{result.iteration_1_score}</span>
            </div>
            <div style={{ fontSize: '12px', color: '#6b7280' }}>{result.iteration_1_feedback_count} issues</div>
            {result.iteration_1_reasoning && <div style={{ fontSize: '12px', color: '#4b5563', marginTop: '4px', lineHeight: '1.4' }}>{result.iteration_1_reasoning}</div>}
            {result.iteration_1_top_fixes?.length > 0 && <ol style={{ margin: '4px 0 0', padding: '0 0 0 16px', fontSize: '11px', color: '#4b5563', lineHeight: '1.5' }}>
              {result.iteration_1_top_fixes.map((f, i) => <li key={i}>{f}</li>)}
            </ol>}
          </div>
          <div style={{ padding: '12px', background: '#f9fafb', borderRadius: '8px', border: '1px solid #e5e7eb' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '6px' }}>
              <span style={{ fontSize: '12px', fontWeight: '600', color: '#6b7280', textTransform: 'uppercase' }}>Final</span>
              <span style={{ fontSize: '20px', fontWeight: '700', color: getColor(result.iteration_2_score) }}>{result.iteration_2_score}</span>
            </div>
            <div style={{ fontSize: '12px', color: '#6b7280' }}>{result.iteration_2_feedback_count} issues</div>
            {result.iteration_2_reasoning && <div style={{ fontSize: '12px', color: '#4b5563', marginTop: '4px', lineHeight: '1.4' }}>{result.iteration_2_reasoning}</div>}
          </div>
        </div>
        <div style={{ fontSize: '13px', fontWeight: '600', textAlign: 'center', padding: '6px 0', color: delta > 0 ? '#059669' : delta < 0 ? '#dc2626' : '#6b7280' }}>
          {delta > 0 ? `+${delta} improvement` : delta < 0 ? `${delta} regression` : 'No change'}
        </div>
      </div>

      {/* Logs */}
      <div style={{ padding: '16px 24px', borderBottom: '1px solid #e5e7eb' }}>
        <button onClick={() => setShowLogs(!showLogs)} style={{ fontSize: '13px', fontWeight: '600', color: '#6b7280', cursor: 'pointer', background: 'none', border: 'none', padding: 0, fontFamily: 'inherit' }}>
          {showLogs ? '▾ Hide' : '▸ Show'} Pipeline Logs
        </button>
        {showLogs && <div style={{ marginTop: '8px', padding: '12px', background: '#f9fafb', borderRadius: '6px', fontSize: '12px', fontFamily: 'monospace', lineHeight: '1.7', maxHeight: '200px', overflowY: 'auto' }}>
          {result.logs?.map((l, i) => <p key={i} style={{ margin: 0 }}>{l}</p>)}
        </div>}
      </div>

      {/* New Resume */}
      <div style={{ padding: '16px 24px', textAlign: 'center' }}>
        <button onClick={onReset} style={{ padding: '12px 24px', background: '#f3f4f6', color: '#374151', border: '1px solid #d1d5db', borderRadius: '8px', fontSize: '14px', fontWeight: '600', cursor: 'pointer' }}>
          ← Generate Another Resume
        </button>
      </div>
    </div>
  )
}
