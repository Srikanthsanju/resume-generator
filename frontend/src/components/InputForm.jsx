import React, { useState } from 'react'

const s = {
  form: { display: 'flex', flexDirection: 'column', gap: '16px' },
  label: { fontSize: '13px', fontWeight: '600', color: '#374151', marginBottom: '4px', display: 'block' },
  textarea: { width: '100%', minHeight: '200px', padding: '12px', border: '1px solid #d1d5db', borderRadius: '8px', fontSize: '14px', fontFamily: 'inherit', resize: 'vertical', outline: 'none', boxSizing: 'border-box' },
  row: { display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' },
  select: { width: '100%', padding: '10px 12px', border: '1px solid #d1d5db', borderRadius: '8px', fontSize: '14px', fontFamily: 'inherit', background: '#fff', outline: 'none', boxSizing: 'border-box' },
  input: { width: '100%', padding: '10px 12px', border: '1px solid #d1d5db', borderRadius: '8px', fontSize: '14px', fontFamily: 'inherit', outline: 'none', boxSizing: 'border-box' },
  btn: { padding: '14px 24px', background: '#111827', color: '#fff', border: 'none', borderRadius: '8px', fontSize: '15px', fontWeight: '600', cursor: 'pointer', marginTop: '4px' },
  btnOff: { padding: '14px 24px', background: '#9ca3af', color: '#fff', border: 'none', borderRadius: '8px', fontSize: '15px', fontWeight: '600', cursor: 'not-allowed', marginTop: '4px' },
  fg: { display: 'flex', flexDirection: 'column' },
}

export default function InputForm({ onGenerate, loading }) {
  const [fd, setFd] = useState({ jd: '', job_type: 'contract', role_type: 'AI Engineer', role_name: '', company_name: '' })
  const u = (k) => (e) => setFd((p) => ({ ...p, [k]: e.target.value }))
  const ok = fd.jd.trim() && fd.role_name.trim() && fd.company_name.trim()

  return (
    <form onSubmit={(e) => { e.preventDefault(); if (ok) onGenerate(fd) }} style={s.form}>
      <div style={s.fg}>
        <label style={s.label}>Job Description</label>
        <textarea style={s.textarea} placeholder="Paste the full job description here..." value={fd.jd} onChange={u('jd')} />
      </div>
      <div style={s.row}>
        <div style={s.fg}>
          <label style={s.label}>Job Type</label>
          <select style={s.select} value={fd.job_type} onChange={u('job_type')}>
            <option value="contract">Contract</option>
            <option value="fulltime">Fulltime</option>
            <option value="gc">GC</option>
          </select>
        </div>
        <div style={s.fg}>
          <label style={s.label}>Role Type</label>
          <select style={s.select} value={fd.role_type} onChange={u('role_type')}>
            <option value="AI Engineer">AI Engineer</option>
            <option value="Data Scientist">Data Scientist</option>
            <option value="ML Engineer">ML Engineer</option>
            <option value="Data Engineer">Data Engineer</option>
            <option value="Software Engineer">Software Engineer</option>
          </select>
        </div>
      </div>
      <div style={s.row}>
        <div style={s.fg}>
          <label style={s.label}>Role Name (from JD)</label>
          <input style={s.input} type="text" placeholder="e.g. Senior AI Engineer" value={fd.role_name} onChange={u('role_name')} />
        </div>
        <div style={s.fg}>
          <label style={s.label}>Company Name</label>
          <input style={s.input} type="text" placeholder="e.g. Dell Technologies" value={fd.company_name} onChange={u('company_name')} />
        </div>
      </div>
      <button type="submit" style={!ok || loading ? s.btnOff : s.btn} disabled={!ok || loading}>
        {loading ? 'Generating...' : 'Generate Resume'}
      </button>
    </form>
  )
}
