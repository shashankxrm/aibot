"""
Web Interface Module for the AI Chatbot

This module provides a foundation for web interfaces (Flask, FastAPI, Streamlit, etc.)
Currently includes a simple Flask example that can be extended.
"""

import sys
import os
from typing import Dict, Any

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from chatbot import ChatBot


class ChatBotWebInterface:
    """
    Base class for web interfaces.
    This can be extended for different web frameworks.
    """
    
    def __init__(self, model_name: str = "microsoft/DialoGPT-medium"):
        """
        Initialize the web interface.
        
        Args:
            model_name: The Hugging Face model to use
        """
        self.chatbot = ChatBot(model_name=model_name)
        self.sessions: Dict[str, ChatBot] = {}  # For session management
    
    def get_or_create_session(self, session_id: str) -> ChatBot:
        """
        Get or create a chatbot session for a user.
        
        Args:
            session_id: Unique identifier for the session
            
        Returns:
            ChatBot instance for the session
        """
        if session_id not in self.sessions:
            self.sessions[session_id] = ChatBot(model_name=self.chatbot.model_name)
        return self.sessions[session_id]
    
    def chat_response(self, message: str, session_id: str = "default") -> Dict[str, Any]:
        """
        Get a chat response for web interface.
        
        Args:
            message: User's message
            session_id: Session identifier
            
        Returns:
            Dictionary with response and metadata
        """
        chatbot = self.get_or_create_session(session_id)
        response = chatbot.chat(message)
        
        return {
            "response": response,
            "session_id": session_id,
            "model": chatbot.model_name,
            "history_length": len(chatbot.get_history())
        }
    
    def clear_session(self, session_id: str = "default"):
        """Clear a specific session."""
        if session_id in self.sessions:
            self.sessions[session_id].clear_history()
    
    def get_session_history(self, session_id: str = "default"):
        """Get history for a specific session."""
        if session_id in self.sessions:
            return self.sessions[session_id].get_history()
        return []


# Example Flask implementation (commented out - uncomment and install flask to use)
"""
from flask import Flask, request, jsonify, render_template_string

class FlaskChatBot:
    def __init__(self, model_name: str = "microsoft/DialoGPT-medium"):
        self.app = Flask(__name__)
        self.web_interface = ChatBotWebInterface(model_name=model_name)
        self.setup_routes()
    
    def setup_routes(self):
        @self.app.route('/')
        def index():
            return render_template_string(self.get_html_template())
        
        @self.app.route('/chat', methods=['POST'])
        def chat():
            data = request.json
            message = data.get('message', '')
            session_id = data.get('session_id', 'default')
            
            if not message:
                return jsonify({'error': 'No message provided'}), 400
            
            response_data = self.web_interface.chat_response(message, session_id)
            return jsonify(response_data)
        
        @self.app.route('/clear', methods=['POST'])
        def clear():
            data = request.json
            session_id = data.get('session_id', 'default')
            self.web_interface.clear_session(session_id)
            return jsonify({'message': 'Session cleared'})
    
    def get_html_template(self):
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>AI Chatbot</title>
            <style>
                body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
                .chat-container { border: 1px solid #ccc; height: 400px; overflow-y: scroll; padding: 10px; margin-bottom: 10px; }
                .message { margin-bottom: 10px; }
                .user { color: blue; }
                .bot { color: green; }
                input[type="text"] { width: 70%; padding: 5px; }
                button { padding: 5px 10px; }
            </style>
        </head>
        <body>
            <h1>🤖 AI Chatbot</h1>
            <div id="chat-container" class="chat-container"></div>
            <input type="text" id="message-input" placeholder="Type your message..." onkeypress="handleKeyPress(event)">
            <button onclick="sendMessage()">Send</button>
            <button onclick="clearChat()">Clear</button>
            
            <script>
                function sendMessage() {
                    const input = document.getElementById('message-input');
                    const message = input.value.trim();
                    if (!message) return;
                    
                    addMessage('You: ' + message, 'user');
                    input.value = '';
                    
                    fetch('/chat', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({message: message, session_id: 'web-session'})
                    })
                    .then(response => response.json())
                    .then(data => {
                        addMessage('Bot: ' + data.response, 'bot');
                    })
                    .catch(error => {
                        addMessage('Error: ' + error, 'bot');
                    });
                }
                
                function addMessage(message, className) {
                    const container = document.getElementById('chat-container');
                    const div = document.createElement('div');
                    div.className = 'message ' + className;
                    div.textContent = message;
                    container.appendChild(div);
                    container.scrollTop = container.scrollHeight;
                }
                
                function clearChat() {
                    fetch('/clear', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({session_id: 'web-session'})
                    })
                    .then(() => {
                        document.getElementById('chat-container').innerHTML = '';
                    });
                }
                
                function handleKeyPress(event) {
                    if (event.key === 'Enter') {
                        sendMessage();
                    }
                }
            </script>
        </body>
        </html>
        '''
    
    def run(self, debug=True, port=5000):
        self.app.run(debug=debug, port=port)

def run_flask_app():
    flask_app = FlaskChatBot()
    print("Starting Flask web interface on http://localhost:5000")
    flask_app.run()
"""
