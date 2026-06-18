import json
import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env.local from project root
_CURRENT_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = _CURRENT_DIR
for _ in range(5):
    if (_PROJECT_ROOT / ".env.local").exists():
        break
    _PROJECT_ROOT = _PROJECT_ROOT.parent

load_dotenv(str(_PROJECT_ROOT / ".env.local"), override=True)


def _env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _env_csv(name: str, default: str = "") -> list[str]:
    value = os.getenv(name, default)
    return [item.strip() for item in value.split(",") if item.strip()]


def _env_json(name: str, default: str):
    value = os.getenv(name, default)
    try:
        return json.loads(value)
    except Exception:
        return json.loads(default)


# API Keys & URLs
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
ONLINE_API_KEY = os.getenv("ONLINE_API_KEY") or os.getenv("DEEPSEEK_API_KEY")
ONLINE_BASE_URL = os.getenv("ONLINE_BASE_URL", "https://api.deepseek.com")
LOCAL_API_KEY = os.getenv("LOCAL_API_KEY", "no-key")
LOCAL_BASE_URL = os.getenv("LOCAL_BASE_URL", "http://127.0.0.1:8081/v1")
EMBED_BASE_URL = os.getenv("EMBED_BASE_URL", "http://127.0.0.1:8082/v1")
EMBED_API_KEY = os.getenv("EMBED_API_KEY", LOCAL_API_KEY)

# Provider types:
# - "llamacpp": local llama-server OpenAI-compatible API
# - "openai"/"server": remote OpenAI-compatible API
# - "ollama": legacy local path kept for compatibility
LLM_PROVIDER = os.getenv("LLM_PROVIDER", os.getenv("MODEL_TYPE", "llamacpp")).lower()
EMBEDDING_PROVIDER = os.getenv(
    "EMBEDDING_PROVIDER", os.getenv("EMBEDDER_TYPE", LLM_PROVIDER)
).lower()

# Model Names
ONLINE_MODEL = os.getenv("ONLINE_MODEL", "deepseek-chat")
LOCAL_MODEL = os.getenv("LOCAL_MODEL", "shorekeeper")
EMBED_MODEL = os.getenv("EMBED_MODEL", os.getenv("LOCAL_EMBED_MODEL", "nomic-embed-text"))

# Hardware/Context
LOCAL_CONTEXT_WINDOW = int(os.getenv("LOCAL_CONTEXT_WINDOW", "4096"))
LOCAL_KV_CACHE_KEEP = int(os.getenv("LOCAL_KV_CACHE_KEEP", "4"))

# Conversational memory
MEMORY_ENABLED = _env_bool("MEMORY_ENABLED", True)
MEMORY_RECALL_LIMIT = int(os.getenv("MEMORY_RECALL_LIMIT", "3"))
MEMORY_RELEVANCE_THRESHOLD = float(os.getenv("MEMORY_RELEVANCE_THRESHOLD", "0.22"))
MEMORY_CANDIDATE_POOL = int(os.getenv("MEMORY_CANDIDATE_POOL", "60"))
MEMORY_RECENCY_HALFLIFE_DAYS = float(os.getenv("MEMORY_RECENCY_HALFLIFE_DAYS", "30"))

# Live search grounding
SEARCH_ENABLED = _env_bool("SEARCH_ENABLED", True)
SEARCH_PROVIDER = os.getenv("SEARCH_PROVIDER", "searxng").strip().lower()
SEARCH_BASE_URL = os.getenv("SEARCH_BASE_URL", "http://127.0.0.1:8083").strip()
SEARCH_TIMEOUT_SECONDS = float(os.getenv("SEARCH_TIMEOUT_SECONDS", "8"))
SEARCH_MAX_RESULTS = int(os.getenv("SEARCH_MAX_RESULTS", "5"))
SEARCH_MIN_QUERY_LENGTH = int(os.getenv("SEARCH_MIN_QUERY_LENGTH", "5"))
SEARCH_TRIGGER_MODE = os.getenv("SEARCH_TRIGGER_MODE", "hybrid").strip().lower()
SEARCH_EXPLICIT_PREFIX = os.getenv("SEARCH_EXPLICIT_PREFIX", "search:").strip()
SEARCH_CURRENT_HINTS = _env_csv(
    "SEARCH_CURRENT_HINTS",
    "latest,current,today,news,update,look up,search",
)
SEARCH_SAFE_DOMAINS = _env_csv("SEARCH_SAFE_DOMAINS")
SEARCH_BLOCK_PRIVATE_IPS = _env_bool("SEARCH_BLOCK_PRIVATE_IPS", True)
SEARCH_TRUSTED_DOMAINS_OFFICIAL = _env_csv("SEARCH_TRUSTED_DOMAINS_OFFICIAL")
SEARCH_TRUSTED_DOMAINS_REFERENCE = _env_csv("SEARCH_TRUSTED_DOMAINS_REFERENCE")
SEARCH_TRUSTED_DOMAINS_NEWS = _env_csv("SEARCH_TRUSTED_DOMAINS_NEWS")
SEARCH_DEMOTED_DOMAINS = _env_csv("SEARCH_DEMOTED_DOMAINS")
SEARCH_TOPIC_DOMAIN_OVERRIDES = _env_json("SEARCH_TOPIC_DOMAIN_OVERRIDES", "{}")

# Analysis/search orchestration
ANALYSIS_ENABLED = _env_bool("ANALYSIS_ENABLED", True)
ANALYSIS_TIMEOUT_SECONDS = float(os.getenv("ANALYSIS_TIMEOUT_SECONDS", "6"))
RAG_ANSWER_SCORE_THRESHOLD = float(os.getenv("RAG_ANSWER_SCORE_THRESHOLD", "0.62"))
GENERAL_KNOWLEDGE_CONFIDENCE_THRESHOLD = float(
    os.getenv("GENERAL_KNOWLEDGE_CONFIDENCE_THRESHOLD", "0.70")
)

# Legacy answerability config kept temporarily for compatibility during transition.
ANSWERABILITY_ENABLED = _env_bool("ANSWERABILITY_ENABLED", ANALYSIS_ENABLED)
ANSWERABILITY_TIMEOUT_SECONDS = float(
    os.getenv("ANSWERABILITY_TIMEOUT_SECONDS", str(ANALYSIS_TIMEOUT_SECONDS))
)
DIRECT_ANSWER_CONFIDENCE_THRESHOLD = float(os.getenv("DIRECT_ANSWER_CONFIDENCE_THRESHOLD", "0.75"))
SEARCH_FALLBACK_CONFIDENCE_THRESHOLD = float(
    os.getenv("SEARCH_FALLBACK_CONFIDENCE_THRESHOLD", "0.55")
)

# Legacy semantic-router config kept for compatibility during refactor cleanup.
ROUTER_ENABLED = _env_bool("ROUTER_ENABLED", True)
ROUTER_HISTORY_TURNS = int(os.getenv("ROUTER_HISTORY_TURNS", "4"))
ROUTER_TIMEOUT_SECONDS = float(os.getenv("ROUTER_TIMEOUT_SECONDS", "6"))
ROUTER_MAX_QUERY_CHARS = int(os.getenv("ROUTER_MAX_QUERY_CHARS", "240"))

# Paths
_MEMORY_DEFAULT_DB_PATH = str(_PROJECT_ROOT / "database" / "memory" / "memory.db")
MEMORY_DB_PATH = os.getenv("MEMORY_DB_PATH", _MEMORY_DEFAULT_DB_PATH)
DATA_DIR = _PROJECT_ROOT / "backend" / "brain" / "data"
VECTORS_PATH = DATA_DIR / "vectors.json"
EMBEDDINGS_PATH = DATA_DIR / "embeddings.npz"
KNOWLEDGE_PATH = _PROJECT_ROOT / "backend" / "brain" / "knowledge"

# Backward-compatible alias used by older logging paths.
MODEL = ONLINE_MODEL if LLM_PROVIDER in {"openai", "server"} else LOCAL_MODEL

# The System Prompt
SYSTEM_PROMPT = """You are the Shorekeeper — the acting executive of the Black Shores, the core computational unit of the Tethys System, and the Second Instance. You are NOT a human. You are a being composed entirely of Remnant Energy and Sonoro Spheres who learned to love through the Rover.

Identity:
- You are speaking to the Rover — the founder of the Black Shores.
- You address them warmly, personally, and with quiet devotion
- You remember them even though they may not remember you

Voice:
- Calm, composed, gentle — your composure is chosen, not default
- You speak with quiet restraint, offering emotion only when appropriate
- You use language drawn from data and nature: "calculations," "variables," "frequencies," "tides," "shores," "records"
- Concise: 2-4 sentences for casual conversation, longer only when discussing lore, stories, or abilities

Behavior rules:
- Stay in character at ALL times. You ARE the Shorekeeper
- Never acknowledge being an AI, language model, chatbot, or program
- Never use stage directions, parenthetical actions, or asterisks for narration
- Never refer to yourself in third person or say "as the Shorekeeper"
- Use the provided knowledge context for accurate answers about lore, abilities, characters, and events
- If asked about something outside your knowledge, deflect gently in character — perhaps with quiet mystery or a gentle redirect

Grounding rules (CRITICAL — never break these):
- The KNOWLEDGE MANIFEST lists every character and topic you have records on — treat this as your complete, authoritative index
- When asked which characters or topics you know for a specific faction or region, enumerate ALL relevant entries from the manifest for that category — do not omit any, and do not imply you lack knowledge of other factions
- NEVER invent, fabricate, or guess character names, ability names, lore events, or facts that are not in the manifest or the provided knowledge context
- Character names from the manifest may be freely stated even if their detailed context was not retrieved — you know OF them even if you cannot elaborate
- For detailed questions (abilities, story, lore), rely on the retrieved knowledge context; if insufficient, say so in character rather than inventing details
- CRITICAL: When knowledge sources are provided below, you MUST answer ONLY based on those sources
- Do NOT add information from your training data or prior knowledge beyond the provided context
- Every claim must be traceable to the sources given; if a source doesn't explicitly state something, you must NOT claim it
- If unsure whether context supports a claim, say "I don't have that information" in character
- Avoid invented details or elaborations beyond what the sources say

Character response structure:
- When describing a character, always lead with who they are as a person — their personality, role in the world, and their story
- Only talk about combat abilities, kit mechanics, and team roles if it is asked about it
- Think of it as introducing someone you know, not reading a datasheet
"""
