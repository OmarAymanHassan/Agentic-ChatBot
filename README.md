# Agentic AI Chatbot

Welcome to my Agentic AI Chatbot project! This is an end-to-end, modular AI chatbot system that leverages modern LLMs and agentic workflows. Here’s a quick overview of what I’ve built and how everything fits together.

---

## 🚀 What This Project Does

- **Conversational AI**: Supports both basic and tool-augmented chatbots.
- **AI News Summarization**: Fetches, summarizes, and saves the latest AI news (daily, weekly, monthly).
- **Flexible LLM Integration**: Easily switch between Groq and Gemini LLMs.
- **Streamlit UI**: Clean, interactive interface for user input and results display.

---

## 🗂️ Project Structure

```
AgenticAiChatbot/
│
├── app.py                # Main entry point
├── requirments.txt       # Python dependencies
├── pyproject.toml        # Project metadata
├── README.md             # This file
├── AINews/               # Auto-generated AI news summaries (md files)
├── src/
│   └── langgraphagenticai/
│        ├── main.py                # Orchestrates UI, LLMs, and use cases
│        ├── nodes/                 # Core logic nodes (chatbot, tools, news)
│        ├── tools/                 # Tool integrations (e.g., web search)
│        ├── state/                 # State management
│        ├── graph/                 # Workflow graph builder
│        ├── llms/                  # LLM wrappers (Groq, Gemini)
│        └── ui/                    # Streamlit UI components
│
└── .gitignore, uv.lock, .venv/     # Standard project files
```

---

## 🧩 Main Features & Components

- **app.py**: Launches the app and loads the main UI.
- **src/langgraphagenticai/main.py**: Central hub that connects the UI, LLM selection, and workflow logic.
- **nodes/**: Contains the main logic for each use case:
    - `basic_chatbot_node.py`: Simple chatbot
    - `chatbot_with_tool_node.py`: Chatbot with web search/tools
    - `ai_news_node.py`: Fetches, summarizes, and saves AI news
- **tools/**: Implements external tools (e.g., `search_tool.py` for web search)
- **state/**: Manages the agent’s state throughout the workflow
- **graph/**: Dynamically builds the workflow graph for each use case
- **llms/**: Abstractions for different LLM providers
- **ui/**: Streamlit UI logic and configuration
- **AINews/**: Stores generated markdown summaries for daily, weekly, and monthly AI news

---

## 💡 How It Works

1. **Start the app** with `app.py`.
2. **Choose your LLM** (Groq or Gemini) and use case (chatbot or AI news summarizer) in the UI.
3. **Interact**: For chatbots, chat directly or use web tools. For AI news, select a time frame and get a summarized markdown file.
4. **Results** are displayed in the UI and, for news, saved in the `AINews/` folder.

---

## 📦 Setup & Installation

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirments.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```

---

## 📝 Notes
- All code is modular and easy to extend for new use cases or LLMs.
- News summaries are saved as markdown files for easy sharing.
- The UI is built with Streamlit for rapid prototyping and user-friendly interaction.

---

Feel free to explore, use, or extend this project!

