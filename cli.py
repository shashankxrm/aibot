"""
Command Line Interface for the AI Chatbot

This module provides a CLI interface for interacting with the chatbot.
"""

import sys
import os
from typing import Optional

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from chatbot import ChatBot


class ChatBotCLI:
    """
    Command Line Interface for the AI Chatbot.
    """
    
    def __init__(self, model_name: str = "microsoft/DialoGPT-medium"):
        """
        Initialize the CLI.
        
        Args:
            model_name: The Hugging Face model to use
        """
        try:
            self.chatbot = ChatBot(model_name=model_name)
            self.model_name = model_name
        except ValueError as e:
            print(f"Error: {e}")
            print("Please set your Hugging Face API token in the .env file or as an environment variable.")
            sys.exit(1)
    
    def print_welcome(self):
        """Print welcome message and instructions."""
        print("=" * 60)
        print("🤖 AI CHATBOT")
        print("=" * 60)
        print(f"Model: {self.model_name}")
        print("\nCommands:")
        print("  /help     - Show this help message")
        print("  /clear    - Clear conversation history")
        print("  /history  - Show conversation history")
        print("  /model    - Change the model")
        print("  /quit     - Exit the chatbot")
        print("\nType your message and press Enter to chat!")
        print("-" * 60)
    
    def print_help(self):
        """Print help message."""
        print("\n📖 HELP")
        print("-" * 30)
        print("Available commands:")
        print("  /help     - Show this help message")
        print("  /clear    - Clear conversation history")
        print("  /history  - Show conversation history")
        print("  /model    - Change the model")
        print("  /quit     - Exit the chatbot")
        print("\nJust type your message to chat with the AI!")
        print()
    
    def show_history(self):
        """Show conversation history."""
        history = self.chatbot.get_history()
        if not history:
            print("\n📋 No conversation history yet.")
            return
        
        print("\n📋 CONVERSATION HISTORY")
        print("-" * 40)
        for entry in history:
            print(entry)
        print()
    
    def change_model(self):
        """Allow user to change the model."""
        print("\n🔧 CHANGE MODEL")
        print("-" * 30)
        print("Popular models:")
        print("1. microsoft/DialoGPT-medium (default)")
        print("2. microsoft/DialoGPT-large")
        print("3. facebook/blenderbot-400M-distill")
        print("4. microsoft/DialoGPT-small")
        print("\nOr enter a custom model name from Hugging Face.")
        
        model_choice = input("\nEnter model name or number (1-4): ").strip()
        
        model_map = {
            "1": "microsoft/DialoGPT-medium",
            "2": "microsoft/DialoGPT-large", 
            "3": "facebook/blenderbot-400M-distill",
            "4": "microsoft/DialoGPT-small"
        }
        
        if model_choice in model_map:
            new_model = model_map[model_choice]
        else:
            new_model = model_choice
        
        try:
            self.chatbot.set_model(new_model)
            self.model_name = new_model
            print(f"✅ Model changed to: {new_model}")
        except Exception as e:
            print(f"❌ Error changing model: {e}")
    
    def run(self):
        """Run the CLI interface."""
        self.print_welcome()
        
        while True:
            try:
                user_input = input("\n👤 You: ").strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.lower() == "/quit":
                    print("\n👋 Goodbye! Thanks for chatting!")
                    break
                elif user_input.lower() == "/help":
                    self.print_help()
                    continue
                elif user_input.lower() == "/clear":
                    self.chatbot.clear_history()
                    print("\n🗑️  Conversation history cleared!")
                    continue
                elif user_input.lower() == "/history":
                    self.show_history()
                    continue
                elif user_input.lower() == "/model":
                    self.change_model()
                    continue
                
                # Get response from chatbot
                print("\n🤖 Bot: ", end="", flush=True)
                response = self.chatbot.chat(user_input)
                print(response)
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye! Thanks for chatting!")
                break
            except Exception as e:
                print(f"\n❌ An error occurred: {e}")


def main():
    """Main function to run the CLI."""
    # Check if a custom model is provided as command line argument
    model_name = "microsoft/DialoGPT-medium"
    if len(sys.argv) > 1:
        model_name = sys.argv[1]
    
    cli = ChatBotCLI(model_name=model_name)
    cli.run()


if __name__ == "__main__":
    main()
