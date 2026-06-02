import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
STATIC_FILES_DIR = BASE_DIR / "static_files"
OUTPUTS_DIR = BASE_DIR / "outputs"
OUTPUTS_DIR.mkdir(exist_ok=True)

# ═══════════════════════════════════════════
# MODEL CONFIGURATION
# ═══════════════════════════════════════════
# To switch models, change WRITER_MODEL and SCORER_MODEL in your .env file.
#
# OpenAI models:  gpt-4o, gpt-4o-mini, gpt-4-turbo
# Anthropic models: claude-sonnet-4-20250514, claude-opus-4-20250514
#
# The writer_agent auto-detects which API to use based on model name.
# If model starts with "claude" → uses Anthropic API
# If model starts with "gpt" → uses OpenAI API
# ═══════════════════════════════════════════

WRITER_MODEL = os.getenv("WRITER_MODEL", "gpt-4o")
SCORER_MODEL = os.getenv("SCORER_MODEL", "gpt-4o")

# API Keys — only the one matching your model choice needs to be set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

MAX_ITERATIONS = 2
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
