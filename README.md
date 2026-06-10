# 🤖 Smart Chatbot — OpenAI GPT

A lightweight, conversational chatbot built with Python and the OpenAI API. Supports multi-turn memory, conversation export, and easy customization.

## ✨ Features

- **Multi-turn conversation memory** — the bot remembers context across messages
- **Customizable system prompt** — define the bot's personality/role
- **Save conversations** — export chat history to a `.txt` file
- **Clean CLI interface** — simple and easy to use

## 🛠️ Tech Stack

- Python 3.10+
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- GPT-4o-mini (configurable)

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/smart-chatbot.git
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your API key
```bash
export OPENAI_API_KEY="your-api-key-here"
```

### 4. Run
```bash
python chatbot.py
```

## 💬 Usage

```
You: What is machine learning?
Bot: Machine learning is a branch of AI that enables systems to learn from data...

You: save        → exports conversation to a .txt file
You: reset       → clears conversation history
You: exit        → quits the program
```

## 🔧 Customization

```python
bot = SmartChatbot(
    model="gpt-4o",                        # change model
    system_prompt="You are a sarcastic assistant who speaks only in rhymes."
)
```

## 📄 License

MIT License — free to use and modify.
