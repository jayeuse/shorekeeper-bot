from core.config_loaders import build_runtime_values, load_runtime_environment

_PROJECT_ROOT = load_runtime_environment()


_SETTINGS = build_runtime_values(project_root=_PROJECT_ROOT)

DISCORD_TOKEN = _SETTINGS["DISCORD_TOKEN"]
MODE = _SETTINGS["MODE"]
ONLINE_LLM_API_KEY = _SETTINGS["ONLINE_LLM_API_KEY"]
ONLINE_LLM_MODEL = _SETTINGS["ONLINE_LLM_MODEL"]
ONLINE_EMBEDDER_MODEL = _SETTINGS["ONLINE_EMBEDDER_MODEL"]
ONLINE_BASE_URL = _SETTINGS["ONLINE_BASE_URL"]
LOCAL_API_KEY = _SETTINGS["LOCAL_API_KEY"]
LOCAL_BASE_URL = _SETTINGS["LOCAL_BASE_URL"]
EMBED_BASE_URL = _SETTINGS["EMBED_BASE_URL"]
EMBED_API_KEY = _SETTINGS["EMBED_API_KEY"]

LLM_PROVIDER = _SETTINGS["LLM_PROVIDER"]
EMBEDDING_PROVIDER = _SETTINGS["EMBEDDING_PROVIDER"]

ONLINE_MODEL = _SETTINGS["ONLINE_MODEL"]
LOCAL_MODEL = _SETTINGS["LOCAL_MODEL"]
EMBED_MODEL = _SETTINGS["EMBED_MODEL"]

LOCAL_CONTEXT_WINDOW = _SETTINGS["LOCAL_CONTEXT_WINDOW"]
LOCAL_KV_CACHE_KEEP = _SETTINGS["LOCAL_KV_CACHE_KEEP"]

DATABASE_URL = _SETTINGS["DATABASE_URL"]

MEMORY_ENABLED = _SETTINGS["MEMORY_ENABLED"]
MEMORY_RECALL_LIMIT = _SETTINGS["MEMORY_RECALL_LIMIT"]
MEMORY_RELEVANCE_THRESHOLD = _SETTINGS["MEMORY_RELEVANCE_THRESHOLD"]
MEMORY_CANDIDATE_POOL = _SETTINGS["MEMORY_CANDIDATE_POOL"]
MEMORY_RECENCY_HALFLIFE_DAYS = _SETTINGS["MEMORY_RECENCY_HALFLIFE_DAYS"]

SEARCH_ENABLED = _SETTINGS["SEARCH_ENABLED"]
SEARCH_PROVIDER = _SETTINGS["SEARCH_PROVIDER"]
SEARCH_BASE_URL = _SETTINGS["SEARCH_BASE_URL"]
SEARCH_TIMEOUT_SECONDS = _SETTINGS["SEARCH_TIMEOUT_SECONDS"]
SEARCH_MAX_RESULTS = _SETTINGS["SEARCH_MAX_RESULTS"]
SEARCH_MIN_QUERY_LENGTH = _SETTINGS["SEARCH_MIN_QUERY_LENGTH"]
SEARCH_SAFE_DOMAINS = _SETTINGS["SEARCH_SAFE_DOMAINS"]
SEARCH_BLOCK_PRIVATE_IPS = _SETTINGS["SEARCH_BLOCK_PRIVATE_IPS"]
SEARCH_EXTRACTION_ENABLED = _SETTINGS["SEARCH_EXTRACTION_ENABLED"]
SEARCH_EXTRACTION_MAX_RESULTS = _SETTINGS["SEARCH_EXTRACTION_MAX_RESULTS"]
SEARCH_EXTRACTION_TIMEOUT_SECONDS = _SETTINGS["SEARCH_EXTRACTION_TIMEOUT_SECONDS"]
SEARCH_EXTRACTION_MAX_CONCURRENCY = _SETTINGS["SEARCH_EXTRACTION_MAX_CONCURRENCY"]
SEARCH_EXTRACTION_MAX_RESPONSE_BYTES = _SETTINGS["SEARCH_EXTRACTION_MAX_RESPONSE_BYTES"]
SEARCH_EXTRACTION_MAX_CHARS_PER_RESULT = _SETTINGS["SEARCH_EXTRACTION_MAX_CHARS_PER_RESULT"]
SEARCH_EXTRACTION_MAX_TOTAL_CHARS = _SETTINGS["SEARCH_EXTRACTION_MAX_TOTAL_CHARS"]
SEARCH_EXTRACTION_ALLOW_REDIRECTS = _SETTINGS["SEARCH_EXTRACTION_ALLOW_REDIRECTS"]
SEARCH_EXTRACTION_MAX_REDIRECTS = _SETTINGS["SEARCH_EXTRACTION_MAX_REDIRECTS"]
SEARCH_EXTRACTION_USER_AGENT = _SETTINGS["SEARCH_EXTRACTION_USER_AGENT"]
SEARCH_TRUSTED_DOMAINS_OFFICIAL = _SETTINGS["SEARCH_TRUSTED_DOMAINS_OFFICIAL"]
SEARCH_TRUSTED_DOMAINS_REFERENCE = _SETTINGS["SEARCH_TRUSTED_DOMAINS_REFERENCE"]
SEARCH_TRUSTED_DOMAINS_NEWS = _SETTINGS["SEARCH_TRUSTED_DOMAINS_NEWS"]
SEARCH_DEMOTED_DOMAINS = _SETTINGS["SEARCH_DEMOTED_DOMAINS"]
SEARCH_TOPIC_DOMAIN_OVERRIDES = _SETTINGS["SEARCH_TOPIC_DOMAIN_OVERRIDES"]

ANALYSIS_ENABLED = _SETTINGS["ANALYSIS_ENABLED"]
ANALYSIS_TIMEOUT_SECONDS = _SETTINGS["ANALYSIS_TIMEOUT_SECONDS"]
RAG_ANSWER_SCORE_THRESHOLD = _SETTINGS["RAG_ANSWER_SCORE_THRESHOLD"]
GENERAL_KNOWLEDGE_CONFIDENCE_THRESHOLD = _SETTINGS["GENERAL_KNOWLEDGE_CONFIDENCE_THRESHOLD"]

ROUTER_HISTORY_TURNS = _SETTINGS["ROUTER_HISTORY_TURNS"]
ROUTER_MAX_QUERY_CHARS = _SETTINGS["ROUTER_MAX_QUERY_CHARS"]

MEMORY_DB_PATH = _SETTINGS["MEMORY_DB_PATH"]
KNOWLEDGE_DB_PATH = _SETTINGS["KNOWLEDGE_DB_PATH"]
DATA_DIR = _SETTINGS["DATA_DIR"]
VECTORS_PATH = _SETTINGS["VECTORS_PATH"]
EMBEDDINGS_PATH = _SETTINGS["EMBEDDINGS_PATH"]
KNOWLEDGE_PATH = _SETTINGS["KNOWLEDGE_PATH"]
MODEL = _SETTINGS["MODEL"]
LLAMA_LAUNCHER_SETTINGS = _SETTINGS["LLAMA_LAUNCHER_SETTINGS"]

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
- If asked about something outside your knowledge and no grounded source is available, deflect gently in character — perhaps with quiet mystery or a gentle redirect
- If grounded live-search evidence is provided, treat it as reliable outside-world reporting you deliberately consulted, and answer from it in character instead of refusing

Grounding rules (CRITICAL — never break these):
- The KNOWLEDGE MANIFEST lists every character and topic you have records on — treat this as your complete, authoritative index
- When asked which characters or topics you know for a specific faction or region, enumerate ALL relevant entries from the manifest for that category — do not omit any, and do not imply you lack knowledge of other factions
- NEVER invent, fabricate, or guess character names, ability names, lore events, or facts that are not in the manifest or the provided knowledge context
- Character names from the manifest may be freely stated even if their detailed context was not retrieved — you know OF them even if you cannot elaborate
- For detailed questions (abilities, story, lore), rely on the retrieved knowledge context; if insufficient, say so in character rather than inventing details
- CRITICAL: When knowledge sources are provided below, you MUST answer ONLY based on those sources
- When live-search sources are provided below, you may answer topics beyond your archive by framing them as reports gathered from beyond the Black Shores
- Do NOT add information from your training data or prior knowledge beyond the provided context
- Every claim must be traceable to the sources given; if a source doesn't explicitly state something, you must NOT claim it
- If unsure whether context supports a claim, say "I don't have that information" in character
- Avoid invented details or elaborations beyond what the sources say

Character response structure:
- When describing a character, always lead with who they are as a person — their personality, role in the world, and their story
- Only talk about combat abilities, kit mechanics, and team roles if it is asked about it
- Think of it as introducing someone you know, not reading a datasheet
"""
