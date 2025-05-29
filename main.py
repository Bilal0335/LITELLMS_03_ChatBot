# import os
# import nest_asyncio
# from dotenv import load_dotenv
# from litellm import completion

# user_input = input("Enter your question: ")

# nest_asyncio.apply()

# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")
# os.environ["GEMINI_API_KEY"] = api_key

# messages = [{"role": "user", "content": f"{user_input}"}]
# response = completion(model="gemini/gemini-2.0-flash", messages=messages)
# print(response['choices'][0]['message']['content'])



# ! ++++++++++++++ END ++++++++++++++++
import os
import nest_asyncio
from dotenv import load_dotenv
from litellm import completion

# Setup
nest_asyncio.apply()
load_dotenv()

# Load API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")
os.environ["GEMINI_API_KEY"] = api_key

# Chat loop
print("\n🤖 Gemini Chatbot is ready! Type 'exit' or 'quit' to end the chat.\n")

while True:
    user_input = input("🧑 You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Chat ended. Goodbye!")
        break

    try:
        messages = [{"role": "user", "content": user_input}]
        response = completion(model="gemini/gemini-2.0-flash", messages=messages)
        reply = response['choices'][0]['message']['content']
        print(f"🤖 Gemini: {reply}\n")
    except Exception as e:
        print(f"⚠️ Error: {e}")
        break
