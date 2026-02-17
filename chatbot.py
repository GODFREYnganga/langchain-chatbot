"""
LangChain Customer Support Chatbot
A beginner-friendly example of building AI chatbots with prompt chaining
"""

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the LLM (Language Model)
# Using GPT-3.5-turbo: cost-effective and fast
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,  # Controls creativity (0=deterministic, 1=random)
    api_key=os.getenv("OPENAI_API_KEY")
)

# Define a prompt template for customer support
# This is a "template" because {input} will be replaced with user messages
prompt = ChatPromptTemplate.from_template(
    """You are a helpful, friendly customer support agent for a tech company.
Your role is to:
- Answer questions about products and services
- Help with troubleshooting
- Be empathetic and professional
- Keep responses concise but helpful

{input}"""
)

# Create memory to track conversation history
# This allows the chatbot to remember previous messages
memory = ConversationBufferMemory(
    memory_key="chat_history",
    human_prefix="Customer",
    ai_prefix="Support Agent"
)

# Build the chain by combining the LLM, prompt, and memory
# This is the core of LangChain's power: composing different components
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=True  # Shows internal steps (helpful for debugging)
)

def run_chatbot():
    """Main chatbot loop that handles user interaction"""
    print("\n" + "="*60)
    print("🤖 LangChain Customer Support Chatbot")
    print("="*60)
    print("Welcome! I'm here to help. Type 'exit' to quit.\n")
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Exit condition
            if user_input.lower() == "exit":
                print("\nThank you for using our support! Goodbye! 👋")
                break
            
            # Skip empty inputs
            if not user_input:
                print("Please enter a message.\n")
                continue
            
            # Get response from the chain
            # The chain handles: prompt formatting + LLM call + memory management
            print("\n⏳ Thinking...\n")
            response = chain.run(input=user_input)
            
            print(f"Support Agent: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nChatbot interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please check your API key and try again.\n")

if __name__ == "__main__":
    run_chatbot()
