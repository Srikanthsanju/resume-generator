import re

def extract_jd_details(jd_text: str) -> dict:
    """Extract recruiter email, name, job title, work location from JD text."""
    result = {"recruiter_email": "", "recruiter_name": "", "job_title": "", "work_location": ""}

    # ── Email ──
    emails = re.findall(r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}', jd_text)
    if emails:
        result["recruiter_email"] = emails[-1]

    # ── Job title ──
    for pat in [
        r'(?:Hiring|Position|Job Title|Role Title|Title)\s*[:\-]\s*(.+?)(?:\n|$)',
        r'(?:We are (?:seeking|looking for|hiring) (?:a|an)\s+)(.+?)(?:\s+(?:to |with |who ))',
    ]:
        m = re.search(pat, jd_text, re.IGNORECASE)
        if m:
            t = m.group(1).strip().strip('*').strip()
            if len(t) < 80:
                result["job_title"] = t
                break

    # ── Location ──
    for pat in [
        r'(?:📍\s*)?(?:Location|Work Location|Job Location|Office)\s*[:\-]\s*(.+?)(?:\n|$)',
        r'(?:📍)\s*(.+?)(?:\n|$)',
    ]:
        m = re.search(pat, jd_text, re.IGNORECASE)
        if m:
            loc = m.group(1).strip().strip('*').strip()
            if len(loc) < 60:
                result["work_location"] = loc
                break

    # ── Recruiter name ──
    if result["recruiter_email"]:
        email = result["recruiter_email"]
        pos = jd_text.find(email)
        if pos > 0:
            before = jd_text[max(0, pos - 300):pos]
            lines = [l.strip() for l in before.split('\n') if l.strip()]
            for line in reversed(lines):
                clean = re.sub(r'[*_#\-:📧📍🕒]', '', line).strip()
                skip_words = ['email', 'e-mail', 'recruiter', 'phone', 'contact', 'address',
                    'drive', 'suite', 'ste', 'inc', 'llc', 'ltd', 'corp', 'senior',
                    'technical', 'principal', '@', 'http', 'www', 'global', 'pvt']
                if clean and len(clean) < 40 and not any(kw in clean.lower() for kw in skip_words):
                    words = clean.split()
                    if 1 <= len(words) <= 4 and all(w[0].isupper() for w in words if len(w) > 1 and w.isalpha()):
                        result["recruiter_name"] = clean
                        break
        if not result["recruiter_name"]:
            prefix = email.split('@')[0]
            result["recruiter_name"] = prefix.replace('.', ' ').replace('_', ' ').replace('-', ' ').title()

    return result
