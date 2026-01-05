import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
Claude_API_KEY = os.getenv("CLAUDE_API_KEY")
GEMMINI_API_KEY = os.getenv("GEMMINI_API_KEY")
 