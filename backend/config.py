import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Static files directory (guidelines, templates, resume_master)
STATIC_FILES_DIR = BASE_DIR / "static_files"

# Output directory for generated resumes
OUTPUTS_DIR = BASE_DIR / "outputs"
OUTPUTS_DIR.mkdir(exist_ok=True)

# API Keys
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Model Configuration
WRITER_MODEL = os.getenv("WRITER_MODEL", "claude-sonnet-4-20250514")
SCORER_MODEL = os.getenv("SCORER_MODEL", "gpt-4o")

# Pipeline Configuration
MAX_ITERATIONS = 2

# Server
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
