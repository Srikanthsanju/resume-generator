import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
STATIC_FILES_DIR = BASE_DIR / "static_files"
OUTPUTS_DIR = BASE_DIR / "outputs"
OUTPUTS_DIR.mkdir(exist_ok=True)

# Both Writer and Scorer now use OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Writer: GPT-4o for flexible, natural resume writing
WRITER_MODEL = os.getenv("WRITER_MODEL", "gpt-4o")

# Scorer: GPT-4o for structured evaluation
SCORER_MODEL = os.getenv("SCORER_MODEL", "gpt-4o")

# Anthropic key kept for backward compatibility (optional)
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

MAX_ITERATIONS = 2
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))