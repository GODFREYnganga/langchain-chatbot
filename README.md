# 🤖 LangChain Beginner's Toolkit: AI Chatbot with Prompt Chaining

A complete beginner's guide to learning LangChain by building a **Customer Support Chatbot** with conversation memory and prompt chaining.

## 📋 Project Overview

**What You'll Learn:**
- Core LangChain concepts (chains, prompts, memory)
- How to build AI chatbots with conversation history
- Prompt engineering basics
- Integration with OpenAI APIs
- Debugging and troubleshooting LLM applications

**What You'll Build:**
A fully functional chatbot that:
- Responds to user questions intelligently
- Remembers previous conversation messages
- Uses prompt templates for consistent behavior
- Runs entirely locally with minimal setup

**Time to Complete:** 30-45 minutes

## 🚀 Quick Start

### 1. Clone or Download This Repository
```bash
git clone <your-repo-url>
cd langchain-chatbot
```

### 2. Set Up Python Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Get Your OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Sign up (free trial available)
3. Create a new API key
4. Copy it safely

### 5. Create `.env` File
Create a file named `.env` in the project root:
```
OPENAI_API_KEY=sk-your_actual_api_key_here
```

⚠️ **Never commit this file to Git!** (It's in .gitignore)

### 6. Run the Chatbot
```bash
python chatbot.py
```

You should see:
```
============================================================
🤖 LangChain Customer Support Chatbot
============================================================
Welcome! I'm here to help. Type 'exit' to quit.

You: 
```

### 7. Try Some Questions
```
You: What's your company about?
You: How do I reset my password?
You: Remember what we just talked about?
You: exit
```

## 📁 Project Structure

```
langchain-chatbot/
├── chatbot.py                      # Main chatbot application
├── test_setup.py                   # Verify installation
├── requirements.txt                # Python dependencies
├── .env                            # API keys (not committed)
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
└── LangChain_Beginners_Toolkit.md # Complete learning guide
```

## 🔧 System Requirements

- **Python:** 3.9 or higher
- **OS:** Windows, macOS, or Linux
- **OpenAI Account:** With API key and credit ($5 free trial)
- **RAM:** 2GB minimum
- **Internet:** Required for API calls

## 📚 Understanding the Code

### Key Components

**1. ChatOpenAI (The LLM)**
```python
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)
```
- Initializes the language model
- `temperature` controls randomness (0=strict, 1=creative)

**2. ChatPromptTemplate (Prompt Structure)**
```python
prompt = ChatPromptTemplate.from_template(
    """You are a helpful support agent...
    {input}"""
)
```
- Defines the prompt structure
- `{input}` is replaced with user messages

**3. ConversationBufferMemory (Conversation History)**
```python
memory = ConversationBufferMemory()
```
- Stores previous messages
- Passes them to the LLM for context

**4. LLMChain (The Chain)**
```python
chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
```
- Combines all components
- Orchestrates the flow: input → prompt → LLM → memory → output

### Prompt Chaining Explained

This project demonstrates **basic chaining**. In the prompt template, we're essentially:
1. Taking user input
2. Formatting it into a structured prompt
3. Sending to the LLM
4. Storing response in memory

**Advanced chaining** would involve multiple sequential steps (coming in future tutorials).

## 🐛 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'langchain'`
**Solution:** Activate your virtual environment and run `pip install -r requirements.txt`

### Issue: `API Key Error` or `AuthenticationError`
**Solution:** 
1. Check your API key is correct at https://platform.openai.com/api-keys
2. Verify `.env` file has correct format: `OPENAI_API_KEY=sk-...`
3. Restart your terminal/IDE after creating `.env`

### Issue: "RateLimitError"
**Solution:** 
- Wait a few minutes
- Check your OpenAI account for rate limits
- Consider using `gpt-3.5-turbo` instead of `gpt-4`

### Issue: Chatbot doesn't remember previous messages
**Solution:** Make sure you're using the memory object in the chain and that verbose output shows memory being used

## 📖 Complete Learning Guide

For a comprehensive walkthrough with:
- Detailed AI prompt journal
- More troubleshooting tips
- Next steps for advanced learning
- References and resources

See: **`LangChain_Beginners_Toolkit.md`**

## 🎯 Learning Path

### Beginner (This Project)
✅ Basic prompt templates
✅ Simple chains with memory
✅ Conversation history

### Intermediate (Next Steps)
- Retrieval chains (answer questions from documents)
- Sequential chains (multiple steps)
- Output parsing

### Advanced
- Agents (autonomous decision-making)
- LangSmith (debugging/monitoring)
- Production deployment

## 🔗 Useful Resources

- **LangChain Official Docs:** https://python.langchain.com/
- **OpenAI API Documentation:** https://platform.openai.com/docs/
- **Prompt Engineering Guide:** https://www.promptingguide.ai/
- **LangChain Community Discord:** https://discord.gg/6adMQxSpJS

## 📝 What You'll Learn by Doing

By working through this project, you'll understand:

| Concept | What It Is | Why It Matters |
|---------|-----------|----------------|
| **Chains** | Linked sequence of LLM operations | Core building block of LangChain |
| **Prompts** | Instructions sent to the LLM | Control AI behavior and output |
| **Memory** | Conversation history storage | Enable context-aware responses |
| **Templates** | Reusable prompt structures | Keep prompts consistent and maintainable |
| **LLM Integration** | Connecting to OpenAI/other models | The actual AI reasoning happens here |

## 🤝 Contributing & Feedback

Found a bug or have suggestions? Issues and pull requests are welcome!

## 📄 License

This project is open source and available under the MIT License.

## 🎓 Author Notes

This toolkit was created as a capstone project for the Moringa AI Learning Program. It demonstrates how to leverage generative AI (like ChatGPT) to learn new technologies faster while building practical projects.

**Key Takeaway:** You don't need to be an AI expert to build AI applications. LangChain abstracts complexity so you can focus on building cool stuff! 🚀

---

**Last Updated:** February 2025
**Status:** Ready for Production Learning ✨
