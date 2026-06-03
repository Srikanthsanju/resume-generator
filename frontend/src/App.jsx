import React, { useState } from 'react'
import InputForm from './components/InputForm'
import StrategyCard from './components/StrategyCard'
import ResultPanel from './components/ResultPanel'

export default function App() {
  const [strategy, setStrategy] = useState(null)
  const [recruiter, setRecruiter] = useState(null)
  const [formData, setFormData] = useState(null)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(null) // null, 'reading', 'generating'
  const [error, setError] = useState(null)

  const handleReadJd = async (fd) => {
    setLoading('reading'); setError(null); setStrategy(null); setResult(null); setFormData(fd)
    try {
      const r = await fetch('/api/read-jd', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ jd: fd.jd, job_type: fd.job_type, role_type: fd.role_type }) })
      if (!r.ok) { const e = await r.json(); throw new Error(e.detail || 'Read JD failed') }
      const data = await r.json()
      setStrategy(data.strategy)
      setRecruiter(data.recruiter)
    } catch (e) { setError(e.message) }
    finally { setLoading(null) }
  }

  const handleGenerate = async (approvedStrategy) => {
    setLoading('generating'); setError(null); setResult(null)
    try {
      const r = await fetch('/api/generate', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...formData, strategy: approvedStrategy })
      })
      if (!r.ok) { const e = await r.json(); throw new Error(e.detail || 'Generation failed') }
      setResult(await r.json())
    } catch (e) { setError(e.message) }
    finally { setLoading(null) }
  }

  const handleReset = () => { setStrategy(null); setRecruiter(null); setResult(null); setFormData(null); setError(null) }

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px', fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif', color: '#1a1a1a' }}>
      <header style={{ textAlign: 'center', marginBottom: '32px', paddingBottom: '16px', borderBottom: '2px solid #e5e7eb' }}>
        <h1 style={{ fontSize: '24px', fontWeight: '700', margin: '0 0 6px 0' }}>AI Resume Generator</h1>
        <p style={{ fontSize: '14px', color: '#6b7280', margin: 0 }}>Read JD → Review Strategy → Generate Resume</p>
      </header>

      {!strategy && !result && <InputForm onReadJd={handleReadJd} loading={loading === 'reading'} />}

      {error && <div style={{ padding: '12px 16px', marginTop: '16px', background: '#fef2f2', border: '1px solid #fecaca', borderRadius: '8px', color: '#b91c1c', fontSize: '14px' }}>{error}</div>}

      {loading === 'reading' && <div style={{ textAlign: 'center', padding: '32px', marginTop: '16px', background: '#f9fafb', borderRadius: '12px' }}>
        <p style={{ fontSize: '16px', fontWeight: '600', margin: 0 }}>Reading JD and building strategy...</p>
        <p style={{ fontSize: '13px', color: '#6b7280', margin: '6px 0 0' }}>Planner is classifying role, skills, and priorities</p>
      </div>}

      {strategy && !result && <StrategyCard strategy={strategy} onGenerate={handleGenerate} onBack={handleReset} loading={loading === 'generating'} />}

      {loading === 'generating' && <div style={{ textAlign: 'center', padding: '32px', marginTop: '16px', background: '#f9fafb', borderRadius: '12px' }}>
        <p style={{ fontSize: '16px', fontWeight: '600', margin: 0 }}>Generating resume from strategy...</p>
        <p style={{ fontSize: '13px', color: '#6b7280', margin: '6px 0 0' }}>Writer → Scorer → Rewrite → Final Score (30-60 seconds)</p>
      </div>}

      {result && <ResultPanel result={result} jobType={formData?.job_type || 'contract'} recruiter={recruiter} onReset={handleReset} />}
    </div>
  )
}
