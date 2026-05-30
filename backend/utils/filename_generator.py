from datetime import datetime
from backend.config import OUTPUTS_DIR

ROLE_ABBREV = {
    "AI Engineer": "AI",
    "ML Engineer": "ML",
    "Data Scientist": "DS",
    "Data Engineer": "DE",
    "Software Engineer": "SE",
}

NAME_PREFIX = {
    "contract": "SrikanthM",
    "fulltime": "Srikanth",
    "gc": "S.Srikanth",
}


def generate_filename(company_name: str, job_type: str, role_type: str) -> str:
    """
    Generate filename:
      Fulltime:  Srikanth AI TekTechno 4.2.docx
      Contract:  SrikanthM AI TekTechno 4.2.docx
      GC:        S.Srikanth AI TekTechno 4.2.docx
    """
    name_prefix = NAME_PREFIX.get(job_type, "Srikanth")
    role_abbrev = ROLE_ABBREV.get(role_type, "AI")
    clean_company = "".join(c for c in company_name if c.isalnum() or c == " ").strip()

    now = datetime.now()
    date_str = f"{now.month}.{now.day}"

    filename = f"{name_prefix} {role_abbrev} {clean_company} {date_str}.docx"

    filepath = OUTPUTS_DIR / filename
    if not filepath.exists():
        return filename

    counter = 2
    while True:
        dup_filename = f"{name_prefix} {role_abbrev} {clean_company} {date_str} ({counter}).docx"
        if not (OUTPUTS_DIR / dup_filename).exists():
            return dup_filename
        counter += 1
