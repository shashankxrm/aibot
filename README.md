# AI Chatbot

A modular AI chatbot built with Python and Hugging Face APIs. The chatbot is designed with a modular architecture that supports both CLI and web interfaces.

## Features

- 🤖 AI-powered conversations using Hugging Face models
- 💬 Command-line interface for quick interactions
- 🔧 Modular design for easy extension
- 📝 Conversation history management
- 🔄 Model switching capability
- 🌐 Web interface foundation (Flask example included)

## Setup

### 1. Clone and Navigate
```bash
cd aibot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Token
1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your Hugging Face API token:
   ```
   HUGGINGFACE_API_TOKEN=your_actual_token_here
   ```

   Get your free API token from: https://huggingface.co/settings/tokens

## Usage

### Command Line Interface
Run the chatbot in CLI mode:
```bash
python cli.py
```

Or with a specific model:
```bash
python cli.py microsoft/DialoGPT-large
```

### CLI Commands
- `/help` - Show help message
- `/clear` - Clear conversation history
- `/history` - Show conversation history
- `/model` - Change the AI model
- `/quit` - Exit the chatbot

### Available Models
- `microsoft/DialoGPT-medium` (default)
- `microsoft/DialoGPT-large`
- `microsoft/DialoGPT-small`
- `facebook/blenderbot-400M-distill`
- Any other compatible Hugging Face model

## Project Structure

```
aibot/
├── src/
│   ├── chatbot.py          # Core chatbot logic
│   └── web_interface.py    # Web interface foundation
├── cli.py                  # Command-line interface
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

## Modular Design

The chatbot is built with modularity in mind:

- **Core Logic** (`src/chatbot.py`): Contains the main `ChatBot` class with Hugging Face API integration
- **CLI Interface** (`cli.py`): Command-line interface implementation
- **Web Foundation** (`src/web_interface.py`): Base classes and Flask example for web interfaces

## Extending with Web Interface

To add a Flask web interface:

1. Install Flask:
   ```bash
   pip install flask
   ```

2. Uncomment the Flask code in `src/web_interface.py`

3. Run the web server:
   ```python
   from src.web_interface import run_flask_app
   run_flask_app()
   ```

## API Usage

You can also use the chatbot programmatically:

```python
from src.chatbot import ChatBot

# Initialize the chatbot
bot = ChatBot(model_name="microsoft/DialoGPT-medium")

# Chat with the bot
response = bot.chat("Hello, how are you?")
print(response)

# Get conversation history
history = bot.get_history()
print(history)
```

## Requirements

- Python 3.7+
- Hugging Face API token (free)
- Internet connection for API calls

## Troubleshooting

### Common Issues

1. **Missing API Token**: Make sure you've set `HUGGINGFACE_API_TOKEN` in your `.env` file
2. **Model Loading Errors**: Some models may take time to load on first use
3. **Rate Limiting**: Free Hugging Face accounts have rate limits

### Error Messages

- "API token is required": Set your Hugging Face token
- "API request failed": Check your internet connection and token validity
- "Model not found": Verify the model name exists on Hugging Face

## License

MIT License - feel free to use and modify as needed.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Future Enhancements

- [ ] Streamlit web interface
- [ ] FastAPI backend
- [ ] Model fine-tuning support
- [ ] Chat export functionality
- [ ] Voice input/output
- [ ] Multi-language support
