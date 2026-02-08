# LangChain Beginner's Toolkit: Building Your First AI Chatbot with Prompt Chaining

## 1. Title & Objective

**Project Title:** "LangChain Fundamentals: A Beginner's Guide to AI Chatbots with Prompt Chaining"

**Technology Chosen:** LangChain (Python library)

**Why LangChain?**
- Simplifies building applications with Large Language Models (LLMs)
- Enables prompt chaining—connecting multiple AI steps into workflows
- Bridges the gap between basic Python and production-grade AI apps
- Growing industry demand (used by startups and enterprises)

**End Goal:**
By the end of this toolkit, you'll build a functional **Customer Support Chatbot** that:
- Answers questions using prompt chaining
- Retrieves context from a simple knowledge base
- Demonstrates core LangChain concepts (chains, prompts, memory)
- Runs locally without complex infrastructure

---

## 2. Quick Summary of the Technology

### What is LangChain?

LangChain is a Python framework that simplifies building AI applications powered by Large Language Models (LLMs like GPT-4, Claude, etc.). Instead of writing complex code to manage API calls and prompt engineering, LangChain provides building blocks for:

- **Chains:** Linking multiple AI steps together
- **Prompts:** Template-based prompt engineering
- **Memory:** Maintaining conversation history
- **Agents:** Creating autonomous AI decision-makers
- **Retrieval:** Connecting LLMs to external data (documents, APIs)

### Where is it used?

- Customer support chatbots
- Document analysis tools
- Code generation assistants
- Personal AI research agents
- Internal knowledge base queriers

### Real-World Example

**Scenario:** A company builds a chatbot that:
1. Takes a customer question
2. Searches their knowledge base for relevant articles
3. Passes the article context + question to an LLM
4. Returns a personalized answer with sources

This entire workflow is simplified with LangChain instead of building from scratch.

---

## 3. System Requirements

### Operating System
- **Windows 10+**, **macOS 10.14+**, or **Linux** (Ubuntu 18.04+)

### Required Software
- **Python 3.9+** (download from [python.org](https://python.org))
- **pip** (comes with Python 3.9+)
- **Code Editor:** VS Code, PyCharm, or any text editor
- **Git** (optional, for version control)

### Packages Needed
- `langchain` (core framework)
- `langchain-openai` (OpenAI integration)
- `python-dotenv` (environment variables)
- `openai` (LLM API client)

### External Requirements
- **OpenAI API Key** (free trial available at [platform.openai.com](https://platform.openai.com))
  - Sign up → Create API key → Keep it safe!

---

## 4. Installation & Setup Instructions

### Step 1: Create a Project Directory
```bash
mkdir langchain-chatbot
cd langchain-chatbot
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Required Packages
```bash
pip install langchain langchain-openai python-dotenv openai
```

Verify installation:
```bash
python -c "import langchain; print(langchain.__version__)"
```

### Step 4: Set Up Environment Variables
Create a `.env` file in your project folder:
```
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenAI API key.

**Important:** Never commit `.env` to Git! Add to `.gitignore`:
```
.env
```

### Step 5: Verify Setup
Create a test file `test_setup.py`:
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key loaded: {bool(api_key)}")
```

Run:
```bash
python test_setup.py
```

Expected output: `API Key loaded: True`

---

## 5. Minimal Working Example

### Project: Simple Customer Support Chatbot

This example demonstrates:
- Basic LangChain chain setup
- Prompt templates
- Conversation memory
- Integration with OpenAI

#### Code: `chatbot.py`

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7  # Controls randomness (0-1)
)

# Define a prompt template for customer support
prompt = ChatPromptTemplate.from_template(
    """You are a helpful customer support agent. 
    Use the conversation history to provide context-aware responses.
    
    Customer: {input}
    Assistant:"""
)

# Create memory to track conversation history
memory = ConversationBufferMemory(
    memory_key="chat_history",
    human_prefix="Customer",
    ai_prefix="Assistant"
)

# Build the chain
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=True  # Shows internal steps
)

# Main chatbot loop
def run_chatbot():
    print("🤖 Customer Support Chatbot")
    print("Type 'exit' to quit\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        # Get response from chain
        response = chain.run(input=user_input)
        print(f"\nBot: {response}\n")

if __name__ == "__main__":
    run_chatbot()
```

#### Expected Output
```
🤖 Customer Support Chatbot
Type 'exit' to quit

You: What are your business hours?

> Entering new LLMChain...
Prompt after formatting:
You are a helpful customer support agent...
Customer: What are your business hours?

> Finished chain.

Bot: Based on our standard operations, we're typically open Monday through Friday from 9 AM to 6 PM, and Saturday from 10 AM to 4 PM. We're closed on Sundays and major holidays. Is there anything specific you'd like to know about our hours?

You: Are you open right now?

Bot: To give you an accurate answer, I'd need to know your current time zone and what time it is where you are. What timezone are you in, and what's your current time?

You: exit
Goodbye!
```

#### Explanation
- **ChatOpenAI:** Initializes the GPT model
- **ChatPromptTemplate:** Creates reusable prompt structure
- **ConversationBufferMemory:** Stores conversation history for context
- **LLMChain:** Combines prompt + LLM + memory into a callable chain
- **verbose=True:** Shows internal processing (helpful for learning)

---

## 6. AI Prompt Journal

### Prompt 1: Understanding LangChain Basics
**AI Prompt Used:**
> "Explain LangChain in 3 sentences for someone who knows Python but not AI frameworks. Include one use case."

**Response Summary:**
The AI explained LangChain as a framework that connects Python code to LLMs, handling prompt management and memory automatically. Key insight: It abstracts away API complexity so you focus on logic.

**Evaluation:** ⭐⭐⭐⭐⭐
- Clear, concise explanation
- Directly addressed my knowledge level
- Real use case helped me understand scope

---

### Prompt 2: Building the Chatbot Structure
**AI Prompt Used:**
> "I want to build a chatbot with LangChain that maintains conversation history. What are the three key components I need, and what does each do?"

**Response Summary:**
The AI identified: (1) **ChatPromptTemplate** for structuring prompts, (2) **ChatOpenAI** for the LLM, (3) **ConversationBufferMemory** for maintaining history. Each component's responsibility was clearly explained.

**Evaluation:** ⭐⭐⭐⭐⭐
- Architecture-focused answer
- Helped me understand separation of concerns
- Guided my code structure

---

### Prompt 3: Debugging Memory Issues
**AI Prompt Used:**
> "My LangChain chatbot isn't remembering previous messages. What's the most common cause, and how do I verify memory is working?"

**Response Summary:**
The AI explained that memory isn't automatically saved between script runs (each run starts fresh). To persist, I'd need to save/load memory manually. The suggestion to use `verbose=True` helped me debug.

**Evaluation:** ⭐⭐⭐⭐
- Addressed a real pain point
- Taught me a critical debugging technique
- Practical troubleshooting tips

---

### Prompt 4: Implementing Prompt Chaining
**AI Prompt Used:**
> "Give me a code example of prompt chaining in LangChain: taking user input → analyzing sentiment → responding accordingly."

**Response Summary:**
The AI provided a clear example using SequentialChain with two separate LLMChain steps. Made me realize chaining is about connecting outputs to inputs of different prompts.

**Evaluation:** ⭐⭐⭐⭐⭐
- Code example was production-ready
- Clarified the concept of "chaining"
- Showed how to structure multi-step workflows

---

### Prompt 5: Adding Context/Retrieval
**AI Prompt Used:**
> "How do I make my LangChain chatbot answer questions based on a text document instead of general knowledge?"

**Response Summary:**
The AI introduced the concept of retrieval chains and mentioned document loaders, but I realized this was moving beyond the "beginner" scope. Saved for future expansion.

**Evaluation:** ⭐⭐⭐
- Good information but slightly advanced
- Helped me identify scope boundaries
- Clear roadmap for next-level learning

---

**Key Learning Reflection:**
AI prompts were most effective when I:
1. Clearly stated my knowledge level
2. Asked specific questions (vs. vague ones)
3. Asked "why" + "how" together
4. Provided error messages or specific pain points

The AI accelerated my learning by 3-4x compared to reading docs alone.

---

## 7. Common Issues & Fixes

### Issue 1: "ModuleNotFoundError: No module named 'langchain'"
**Cause:** Packages not installed or virtual environment not activated.

**Fix:**
```bash
# Activate your virtual environment first
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows

# Then install
pip install langchain langchain-openai openai python-dotenv
```

---

### Issue 2: "Invalid API Key" or "Authentication Error"
**Cause:** OpenAI API key is missing, invalid, or not loaded.

**Fix:**
1. Verify your API key at [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Check `.env` file format:
   ```
   OPENAI_API_KEY=sk-...
   ```
3. Ensure you have `load_dotenv()` at the top of your script
4. Restart your Python environment after editing `.env`

---

### Issue 3: "RateLimitError" or Slow Responses
**Cause:** You've exceeded OpenAI's rate limits or are using a slow model.

**Fix:**
- Downgrade model: Use `gpt-3.5-turbo` instead of `gpt-4`
- Reduce `temperature` value (0.3 is faster/more deterministic)
- Check your OpenAI account for rate limits
- Add delays between requests: `import time; time.sleep(1)`

---

### Issue 4: Chatbot Responds But Doesn't Remember Previous Messages
**Cause:** Memory isn't persisting between runs OR prompt isn't using memory variables.

**Fix:**
```python
# Make sure memory variable is included in prompt
prompt = ChatPromptTemplate.from_template(
    """Chat history: {chat_history}
    
    User: {input}
    Assistant:"""
)

# And referenced in chain
chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
```

---

### Issue 5: Code Runs But Produces Generic Responses
**Cause:** Prompt is too vague OR temperature is too low (too deterministic).

**Fix:**
- Make prompts more specific:
  ```python
  prompt = ChatPromptTemplate.from_template(
      """You are a knowledgeable tech support specialist...
      Always be friendly and provide step-by-step solutions...
      {input}"""
  )
  ```
- Increase `temperature` slightly: `temperature=0.8`

---

## 8. References

### Official Documentation
- **LangChain Docs:** https://python.langchain.com/
- **LangChain Getting Started:** https://python.langchain.com/docs/get_started
- **OpenAI API Guide:** https://platform.openai.com/docs/
- **LangChain Chains Concept:** https://python.langchain.com/docs/modules/chains/

### Tutorials & Learning Resources
- **LangChain YouTube Tutorial:** Search "LangChain tutorial for beginners" on YouTube
- **Official LangChain Examples:** https://github.com/langchain-ai/langchain/tree/master/docs/docs/modules
- **Build a Chatbot in 5 Minutes:** https://blog.langchain.dev/
- **Prompt Engineering Guide:** https://www.promptingguide.ai/

### Community & Support
- **LangChain Discord:** https://discord.gg/6adMQxSpJS
- **Stack Overflow:** Tag: `langchain`
- **GitHub Issues:** https://github.com/langchain-ai/langchain/issues

### Next Steps (Beyond This Toolkit)
- Add document retrieval: Learn about **RAG (Retrieval Augmented Generation)**
- Build agents: Explore **LangChain Agents** for autonomous decision-making
- Deploy: Learn **LangServe** for deploying chains as REST APIs
- Monitor: Use **LangSmith** for debugging and monitoring

---

## Appendix: Project Structure

```
langchain-chatbot/
├── venv/                    # Virtual environment
├── .env                     # API keys (DON'T commit!)
├── .gitignore              # Git ignore rules
├── chatbot.py              # Main chatbot code
├── test_setup.py           # Setup verification script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

### Generate requirements.txt:
```bash
pip freeze > requirements.txt
```

---

**Last Updated:** February 2025
**LangChain Version:** 0.1+
**Python Version:** 3.9+
