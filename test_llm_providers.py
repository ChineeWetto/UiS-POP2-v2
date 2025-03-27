from tools.llm_api import query_llm
import os
from pathlib import Path

def safe_print_key(key: str) -> str:
    """Safely print an API key, showing only first 7 and last 4 characters"""
    if len(key) > 11:
        return f"{key[:7]}...{key[-4:]}"
    return "***"

def read_env_file():
    """Read environment variables directly from .env file"""
    env_path = Path('.env')
    if not env_path.exists():
        print("Error: .env file not found!")
        return {}
    
    env_vars = {}
    print("\nReading .env file contents:")
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                env_vars[key] = value
                # Print the key and a safe version of the value
                print(f"{key}={safe_print_key(value)}")
    
    return env_vars

def set_env_vars(env_vars):
    """Set environment variables directly"""
    for key, value in env_vars.items():
        os.environ[key] = value
        # Verify the environment variable was set correctly
        current_value = os.getenv(key)
        print(f"Verifying {key}: set={safe_print_key(value)}, get={safe_print_key(current_value)}")

def print_env_debug(env_vars):
    print("\nEnvironment Debug Info:")
    env_path = Path('.env')
    print(f"Looking for .env at: {env_path.absolute()}")
    print(f"File exists: {env_path.exists()}")
    
    for key in ['OPENAI_API_KEY', 'ANTHROPIC_API_KEY', 'DEEPSEEK_API_KEY', 'GOOGLE_API_KEY']:
        value = env_vars.get(key, '')
        if value:
            safe_value = safe_print_key(value)
            print(f"{key}: {safe_value}")
            # Also print what we get from os.environ
            env_value = os.getenv(key, '')
            print(f"{key} (from os.environ): {safe_print_key(env_value)}")
        else:
            print(f"{key}: Not found")

def test_provider(provider: str, model: str = None, env_vars: dict = None):
    print(f"\nTesting {provider.upper()} API...")
    print(f"Using model: {model}")
    
    # Print first few characters of the API key (safely)
    key_env_map = {
        "openai": "OPENAI_API_KEY",
        "anthropic": "ANTHROPIC_API_KEY",
        "deepseek": "DEEPSEEK_API_KEY",
        "gemini": "GOOGLE_API_KEY"
    }
    
    env_key = key_env_map[provider]
    key = env_vars.get(env_key, '') if env_vars else ''
    if key:
        safe_key = safe_print_key(key)
        print(f"API Key from env_vars: {safe_key}")
        # Also print what we get from os.environ
        env_value = os.getenv(env_key, '')
        print(f"API Key from os.environ: {safe_print_key(env_value)}")
    else:
        print(f"Warning: No API key found for {provider}")
    
    try:
        response = query_llm(
            prompt="What is 2+2? Answer with just the number.",
            provider=provider,
            model=model
        )
        if response:
            print(f"✓ Success! Response: {response.strip()}")
        else:
            print("✗ Failed: No response received")
    except Exception as e:
        print(f"✗ Error: {str(e)}")

def main():
    # Read and set environment variables
    env_vars = read_env_file()
    if not env_vars:
        print("Failed to load environment variables!")
        return
    
    # Set environment variables
    print("\nSetting environment variables:")
    set_env_vars(env_vars)
    
    # Print debug info
    print_env_debug(env_vars)
    
    # Test providers one at a time
    print("\nWhich provider would you like to test?")
    print("1. OpenAI (GPT-3.5 Turbo)")
    print("2. Anthropic (Claude 3)")
    print("3. DeepSeek")
    print("4. Google (Gemini)")
    print("5. Test all providers")
    
    choice = input("Enter your choice (1-5): ")
    
    providers_to_test = {
        "1": ("openai", "gpt-3.5-turbo"),
        "2": ("anthropic", "claude-3-7-sonnet-20250219"),
        "3": ("deepseek", "deepseek-chat"),
        "4": ("gemini", "gemini-pro")
    }
    
    if choice == "5":
        for provider, model in providers_to_test.values():
            test_provider(provider, model, env_vars)
    elif choice in providers_to_test:
        provider, model = providers_to_test[choice]
        test_provider(provider, model, env_vars)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main() 