from pathlib import Path
from backend.config import STATIC_FILES_DIR


class FileLoader:
    """Loads static files: guidelines, resume_master, and template paths."""

    # Guidelines file mapping
    GUIDELINES_MAP = {
        "contract": "contract_guidelines.md",
        "fulltime": "fulltime_guidelines.md",
        "gc": "gc_guidelines.md",
    }

    # Resume master mapping (GC uses its own)
    RESUME_MASTER_MAP = {
        "contract": "resume_master.md",
        "fulltime": "resume_master.md",
        "gc": "gc_resume_master.md",
    }

    # Template mapping
    TEMPLATE_MAP = {
        "contract": "Contract_Template.docx",
        "fulltime": "Fulltime_Template.docx",
        "gc": "GC_Template.docx",
    }

    def __init__(self):
        self.static_dir = STATIC_FILES_DIR

    def load_guidelines(self, job_type: str) -> str:
        """Load guidelines for the given job type."""
        filename = self.GUIDELINES_MAP.get(job_type)
        if not filename:
            raise ValueError(f"Unknown job type: {job_type}")
        path = self.static_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"Guidelines not found: {path}")
        return path.read_text(encoding="utf-8")

    def load_resume_master(self, job_type: str) -> str:
        """Load the correct resume master for the job type."""
        filename = self.RESUME_MASTER_MAP.get(job_type)
        if not filename:
            raise ValueError(f"Unknown job type: {job_type}")
        path = self.static_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"Resume master not found: {path}")
        return path.read_text(encoding="utf-8")

    def get_template_path(self, job_type: str) -> Path:
        """Get the path to the correct docx template."""
        filename = self.TEMPLATE_MAP.get(job_type)
        if not filename:
            raise ValueError(f"Unknown job type: {job_type}")
        path = self.static_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"Template not found: {path}")
        return path
