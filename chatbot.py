import os
from openai import OpenAI
from datetime import datetime

class SmartChatbot:
    def __init__(self, model="gpt-4o-mini", system_prompt=None):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.model = model
        self.history = []
        self.system_prompt = system_prompt or (
            "You are a helpful, friendly, and knowledgeable assistant. "
            "Answer clearly and concisely. If you don't know something, say so."
        )

    def chat(self, user_message: str) -> str:
        self.history.append({"role": "user", "content": user_message})

        messages = [{"role": "system", "content": self.system_prompt}] + self.history

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
        )

        assistant_message = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": assistant_message})
        return assistant_message

    def reset(self):
        self.history = []
        print("Conversation history cleared.")

    def save_conversation(self, filename=None):
        if not filename:
            filename = f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for msg in self.history:
                role = "You" if msg["role"] == "user" else "Bot"
                f.write(f"[{role}]: {msg['content']}\n\n")
        print(f"Conversation saved to {filename}")


def main():
    print("=" * 50)
    print("       Smart Chatbot — Powered by OpenAI")
    print("=" * 50)
    print("Commands: 'reset' to clear history | 'save' to export | 'exit' to quit\n")

    bot = SmartChatbot()

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "reset":
            bot.reset()
        elif user_input.lower() == "save":
            bot.save_conversation()
        else:
            response = bot.chat(user_input)
            print(f"\nBot: {response}\n")


if __name__ == "__main__":
    main()

 # Maded by Kourosh-Esmaeli