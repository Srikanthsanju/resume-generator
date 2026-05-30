import React, { useState } from 'react'
import InputForm from './components/InputForm'
import ResultPanel from './components/ResultPanel'

export default function App() {
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [jobType, setJobType] = useState('contract')

  const handleGenerate = async (formData) => {
    setLoading(true); setError(null); setResult(null); setJobType(formData.job_type)
    try {
      const r = await fetch('/api/generate', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(formData) })
      if (!r.ok) { const e = await r.json(); throw new Error(e.detail || 'Generation failed') }
      setResult(await r.json())
    } catch (e) { setError(e.message) }
    finally { setLoading(false) }
  }

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px', fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif', color: '#1a1a1a' }}>
      <header style={{ textAlign: 'center', marginBottom: '32px', paddingBottom: '16px', borderBottom: '2px solid #e5e7eb' }}>
        <h1 style={{ fontSize: '24px', fontWeight: '700', margin: '0 0 6px 0' }}>AI Resume Generator</h1>
        <p style={{ fontSize: '14px', color: '#6b7280', margin: 0 }}>Paste a JD → Get a tailored resume in seconds</p>
      </header>
      <InputForm onGenerate={handleGenerate} loading={loading} />
      {error && <div style={{ padding: '12px 16px', marginTop: '16px', background: '#fef2f2', border: '1px solid #fecaca', borderRadius: '8px', color: '#b91c1c', fontSize: '14px' }}>{error}</div>}
      {loading && <div style={{ textAlign: 'center', padding: '48px 20px', marginTop: '24px', background: '#f9fafb', borderRadius: '12px', border: '1px solid #e5e7eb' }}>
        <div style={{ fontSize: '32px', marginBottom: '12px' }}>⏳</div>
        <p style={{ fontSize: '16px', fontWeight: '600', margin: '0 0 6px 0' }}>Generating your resume...</p>
        <p style={{ fontSize: '13px', color: '#6b7280', margin: 0 }}>Writer → Scorer → Rewrite → Final Score (30-60 seconds)</p>
      </div>}
      {result && <ResultPanel result={result} jobType={jobType} />}
    </div>
  )
}
