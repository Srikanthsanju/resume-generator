import React, { useState } from 'react'

const lbl = { fontSize: '11px', fontWeight: '600', color: '#6b7280', marginBottom: '3px', display: 'block', textTransform: 'uppercase', letterSpacing: '0.03em' }
const inp = { width: '100%', padding: '8px 10px', border: '1px solid #d1d5db', borderRadius: '6px', fontSize: '13px', fontFamily: 'inherit', outline: 'none', boxSizing: 'border-box' }
const ta = { ...inp, minHeight: '60px', resize: 'vertical' }

export default function StrategyCard({ strategy, onGenerate, onBack, loading }) {
  const [s, setS] = useState({
    primary_role: strategy.primary_role || '',
    role_essence: strategy.role_essence || '',
    ai_intensity: strategy.ai_intensity || 'Level 0',
    primary_skills: (strategy.primary_skills || []).join(', '),
    secondary_skills: (strategy.secondary_skills || []).join(', '),
    suppress: (strategy.suppress || []).join(', '),
    resume_strategy: strategy.resume_strategy || '',
    cloud_decision: strategy.cloud_decision || '',
    forbidden_drift: (strategy.forbidden_drift || []).join(', '),
    bullet_dist: JSON.stringify(strategy.bullet_distribution || {}, null, 0),
    company_strategy: JSON.stringify(strategy.company_strategy || {}, null, 2),
  })

  const u = (k) => (e) => setS(p => ({ ...p, [k]: e.target.value }))

  const handleGenerate = () => {
    const approved = {
      ...strategy,
      primary_role: s.primary_role,
      role_essence: s.role_essence,
      ai_intensity: s.ai_intensity,
      primary_skills: s.primary_skills.split(',').map(x => x.trim()).filter(Boolean),
      secondary_skills: s.secondary_skills.split(',').map(x => x.trim()).filter(Boolean),
      suppress: s.suppress.split(',').map(x => x.trim()).filter(Boolean),
      resume_strategy: s.resume_strategy,
      cloud_decision: s.cloud_decision,
      forbidden_drift: s.forbidden_drift.split(',').map(x => x.trim()).filter(Boolean),
    }
    try { approved.bullet_distribution = JSON.parse(s.bullet_dist) } catch { approved.bullet_distribution = strategy.bullet_distribution }
    try { approved.company_strategy = JSON.parse(s.company_strategy) } catch { approved.company_strategy = strategy.company_strategy }
    onGenerate(approved)
  }

  return (
    <div style={{ border: '1px solid #e5e7eb', borderRadius: '12px', overflow: 'hidden', marginTop: '16px' }}>
      <div style={{ padding: '16px 24px', background: '#eff6ff', borderBottom: '1px solid #bfdbfe' }}>
        <div style={{ fontSize: '15px', fontWeight: '700', color: '#1e40af' }}>Resume Strategy Plan</div>
        <div style={{ fontSize: '12px', color: '#3b82f6', marginTop: '4px' }}>Review and edit before generating. The writer will follow this plan exactly.</div>
      </div>

      <div style={{ padding: '16px 24px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
          <div><label style={lbl}>Primary Role</label><input style={inp} value={s.primary_role} onChange={u('primary_role')} /></div>
          <div><label style={lbl}>AI Intensity</label><input style={inp} value={s.ai_intensity} onChange={u('ai_intensity')} placeholder="Level 0-4" /></div>
        </div>

        <div><label style={lbl}>Role Essence — what should this resume SELL?</label><input style={inp} value={s.role_essence} onChange={u('role_essence')} /></div>

        <div><label style={lbl}>Resume Strategy</label><textarea style={ta} value={s.resume_strategy} onChange={u('resume_strategy')} /></div>

        <div><label style={lbl}>Primary Skills (must prove in bullets, comma separated)</label><textarea style={ta} value={s.primary_skills} onChange={u('primary_skills')} /></div>

        <div><label style={lbl}>Secondary Skills (1-2 bullets max, comma separated)</label><input style={inp} value={s.secondary_skills} onChange={u('secondary_skills')} /></div>

        <div><label style={lbl}>Suppress (DO NOT mention, comma separated)</label><textarea style={{ ...ta, background: '#fef2f2', borderColor: '#fecaca' }} value={s.suppress} onChange={u('suppress')} /></div>

        <div><label style={lbl}>Cloud Decision</label><input style={inp} value={s.cloud_decision} onChange={u('cloud_decision')} /></div>

        <div><label style={lbl}>Forbidden Drift (themes that make it sound like wrong role)</label><input style={inp} value={s.forbidden_drift} onChange={u('forbidden_drift')} /></div>

        <div><label style={lbl}>Company Strategy (JSON — what each company emphasizes)</label><textarea style={{ ...ta, minHeight: '100px', fontFamily: 'monospace', fontSize: '12px' }} value={s.company_strategy} onChange={u('company_strategy')} /></div>
      </div>

      <div style={{ padding: '16px 24px', borderTop: '1px solid #e5e7eb', display: 'flex', gap: '10px' }}>
        <button onClick={onBack} style={{ padding: '12px 20px', background: '#f3f4f6', color: '#374151', border: '1px solid #d1d5db', borderRadius: '8px', fontSize: '14px', fontWeight: '600', cursor: 'pointer' }}>
          ← Back
        </button>
        <button onClick={handleGenerate} disabled={loading} style={{ flex: 1, padding: '12px 20px', background: loading ? '#9ca3af' : '#111827', color: '#fff', border: 'none', borderRadius: '8px', fontSize: '15px', fontWeight: '600', cursor: loading ? 'not-allowed' : 'pointer' }}>
          {loading ? 'Generating...' : '🚀 Generate Resume from Strategy'}
        </button>
      </div>
    </div>
  )
}
