import asyncio
import sys
from pathlib import Path

# Add brain directory to path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.config import LLM_PROVIDER, LOCAL_BASE_URL, ONLINE_BASE_URL
from services.llm import LLMClient


async def verify():
    print("🔍 Testing LLM Connectivity...")
    print("="*40)
    
    try:
        client = LLMClient()

        provider_hint = LLM_PROVIDER
        base_url = ONLINE_BASE_URL if client.provider == "openai" else LOCAL_BASE_URL
        print(f"📡 Sending test request via provider={provider_hint} to model={client.model} ({base_url})...")
        
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say 'Connection Successful!' if you can read this."}
        ]
        
        response = await client.chat(messages)
        content = response["message"]["content"]
        
        print(f"\n🤖 Response: {content}")
        print(f"📊 Usage: {response['prompt_eval_count']} prompt tokens, {response['eval_count']} completion tokens")
        print("\n✅ Verification Complete!")
        
    except Exception as e:
        print(f"\n❌ Connection Failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(verify())
