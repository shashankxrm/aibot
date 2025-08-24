"""
AI Chatbot Core Module

This module contains the main chatbot logic using Hugging Face APIs.
It's designed to be modular and extensible for different interfaces.
"""

import os
import requests
from typing import Dict, List, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class ChatBot:
    """
    A modular AI chatbot using Hugging Face's Inference API.
    """
    
    def __init__(self, model_name: str = "microsoft/DialoGPT-medium", api_token: Optional[str] = None):
        """
        Initialize the chatbot.
        
        Args:
            model_name: The Hugging Face model to use
            api_token: Hugging Face API token (if None, will use environment variable)
        """
        self.model_name = model_name
        self.api_token = api_token or os.getenv("HUGGINGFACE_API_TOKEN")
        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"
        self.conversation_history: List[str] = []
        
        if not self.api_token:
            raise ValueError("Hugging Face API token is required. Set HUGGINGFACE_API_TOKEN environment variable or pass it directly.")
    
    def _make_request(self, payload: Dict) -> Dict:
        """
        Make a request to the Hugging Face API.
        
        Args:
            payload: The request payload
            
        Returns:
            The API response
        """
        headers = {"Authorization": f"Bearer {self.api_token}"}
        
        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"API request failed: {str(e)}"}
    
    def chat(self, message: str, max_length: int = 100) -> str:
        """
        Send a message to the chatbot and get a response.
        
        Args:
            message: The user's message
            max_length: Maximum length of the response
            
        Returns:
            The chatbot's response
        """
        # Add user message to conversation history
        self.conversation_history.append(f"User: {message}")
        
        # Prepare the input for the model
        conversation_context = "\n".join(self.conversation_history[-5:])  # Keep last 5 exchanges
        
        payload = {
            "inputs": conversation_context,
            "parameters": {
                "max_length": max_length,
                "temperature": 0.7,
                "do_sample": True
            }
        }
        
        # Make the API request
        response = self._make_request(payload)
        
        if "error" in response:
            bot_response = f"Sorry, I encountered an error: {response['error']}"
        else:
            # Extract the generated text
            if isinstance(response, list) and len(response) > 0:
                bot_response = response[0].get("generated_text", "").strip()
                # Remove the conversation context from the response
                if conversation_context in bot_response:
                    bot_response = bot_response.replace(conversation_context, "").strip()
                # Clean up the response
                if bot_response.startswith("Bot:"):
                    bot_response = bot_response[4:].strip()
            else:
                bot_response = "I'm sorry, I couldn't generate a response."
        
        # Add bot response to conversation history
        self.conversation_history.append(f"Bot: {bot_response}")
        
        return bot_response
    
    def clear_history(self):
        """Clear the conversation history."""
        self.conversation_history.clear()
    
    def get_history(self) -> List[str]:
        """Get the conversation history."""
        return self.conversation_history.copy()
    
    def set_model(self, model_name: str):
        """
        Change the model being used.
        
        Args:
            model_name: The new Hugging Face model to use
        """
        self.model_name = model_name
        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"
        self.clear_history()  # Clear history when changing models
