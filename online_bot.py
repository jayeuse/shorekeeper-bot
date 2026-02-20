import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env.local
load_dotenv(".env.local")

api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

if not api_key:
    print("❌ Error: GOOGLE_GEMINI_API_KEY not found in .env.local")
    exit(1)

# Configure the Gemini API
genai.configure(api_key=api_key)

# Initialize the model
# Using 'gemini-1.5-flash' as it's a good default balance of speed and quality. 
# You can change this to 'gemini-1.5-pro' for more complex reasoning.
model = genai.GenerativeModel('gemini-2.5-flash-lite-preview-09-2025')

print("✨ Shorekeeper Online (Gemini) Initialized.")
print("Type specific commands or just chat. Type 'exit' to quit.\n")

chat = model.start_chat(history=[])

while True:
    try:
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
            
        if user_input.lower() in ["exit", "quit"]:
            print("Shorekeeper: Goodbye.")
            break
            
        response = chat.send_message(user_input)
        print(f"Shorekeeper: {response.text}")
        print("-" * 20)
        
    except Exception as e:
        print(f"❌ Error: {e}")
