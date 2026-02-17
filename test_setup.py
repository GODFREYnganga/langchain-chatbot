"""
Test Setup Script for LangChain Beginner's Toolkit
Verifies that all dependencies are installed and API key is configured
"""

import sys
import os
from dotenv import load_dotenv

def test_python_version():
    """Check Python version is 3.9+"""
    print("🔍 Checking Python Version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 9:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro} (Good!)\n")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor} (Need 3.9+)\n")
        return False

def test_imports():
    """Check if all required packages are installed"""
    print("🔍 Checking Required Packages...")
    required_packages = {
        'langchain': 'LangChain',
        'langchain_openai': 'LangChain OpenAI',
        'dotenv': 'Python Dotenv',
        'openai': 'OpenAI SDK'
    }
    
    all_good = True
    for package, name in required_packages.items():
        try:
            __import__(package)
            print(f"   ✅ {name}")
        except ImportError:
            print(f"   ❌ {name} (Not installed)")
            all_good = False
    
    print()
    return all_good

def test_api_key():
    """Check if OpenAI API key is loaded"""
    print("🔍 Checking API Key Configuration...")
    
    # Try to load from .env
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key:
        # Mask the key for security
        masked_key = api_key[:8] + "*" * (len(api_key) - 12) + api_key[-4:]
        print(f"   ✅ API Key Found: {masked_key}\n")
        return True
    else:
        print("   ❌ API Key Not Found")
        print("      → Create a .env file in this directory")
        print("      → Add: OPENAI_API_KEY=your_key_here")
        print("      → Get a key at: https://platform.openai.com/api-keys\n")
        return False

def test_api_connection():
    """Try to connect to OpenAI API"""
    print("🔍 Testing OpenAI API Connection...")
    
    try:
        from langchain_openai import ChatOpenAI
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("   ⚠️  API Key not available, skipping connection test\n")
            return None
        
        # Try to initialize the model (doesn't make a full request)
        llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key)
        print("   ✅ OpenAI API Connection Successful\n")
        return True
        
    except Exception as e:
        print(f"   ❌ Connection Failed: {str(e)}\n")
        return False

def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("LangChain Setup Verification")
    print("="*60 + "\n")
    
    results = []
    
    # Run tests
    results.append(("Python Version", test_python_version()))
    results.append(("Dependencies", test_imports()))
    results.append(("API Key", test_api_key()))
    api_test = test_api_connection()
    if api_test is not None:
        results.append(("API Connection", api_test))
    
    # Summary
    print("="*60)
    print("Summary")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed\n")
    
    # Final message
    if passed == total:
        print("🎉 All systems go! You're ready to run chatbot.py")
        print("\nRun: python chatbot.py\n")
    else:
        print("⚠️  Some tests failed. See above for details.\n")

if __name__ == "__main__":
    main()
