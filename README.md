# AIBOT

This project is an AI ChatBot that utilizes the Hugging Face Transformers library to summarize text and answer questions based on the generated summaries. The chatbot is designed to provide simplified summaries tailored to different age groups and allows users to ask questions about the summaries.

## Project Description

AIBOT is an AI-powered chatbot that utilizes LangChain and HuggingFace Transformers to provide text summarization and question-answering capabilities. The chatbot is designed to understand user queries and generate relevant responses based on the provided text input.

## Features

- Text summarization tailored for different age groups.
- Question answering based on summarized content.
- Built using state-of-the-art transformer models.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Changelog](#changelog)

## Installation

To set up the project, follow these steps:

1. **Clone the repository:**

   ```sh
   git clone https://code.swecha.org/shashankxrm/aibot.git
   cd aibot
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv langchain-env
   langchain-env\Scripts\activate  # For Windows
   # or
   source langchain-env/bin/activate  # For macOS/Linux
   ```

3. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Configure GPU usage (if applicable):**
   Follow the instructions in the `README.md` directory to set up GPU support.

## Usage

To run the chatbot application:

1. Run the main script:

   ```sh
   python main.py
   ```

2. Follow the prompts to enter text for summarization and ask questions about the summary.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](../CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the AGPLv3 License. See the [LICENSE](../LICENSE) file for details.

## Changelog

See the [CHANGELOG.md](../CHANGELOG.md) file for a list of changes and updates to the project.