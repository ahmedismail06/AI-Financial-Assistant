# AI Financial Assistant

## Overview
AI Financial Assistant ("William") is an intelligent, friendly, and highly capable financial assistant designed to help users analyze complex corporate financial documents such as 10-K filings and earnings call transcripts. It leverages advanced retrieval-augmented generation (RAG) and large language models to extract key insights, answer questions, and summarize relevant sections with clarity and precision. The assistant is accessible via both text and voice interfaces.

## Features
- **Document Analysis:** Upload and analyze financial documents (PDFs) to extract insights and answer questions.
- **Conversational AI:** Interact with "William" through a chat interface for financial document Q&A.
- **Voice Output:** Get AI responses read aloud using ElevenLabs voice synthesis.
- **User-Friendly Explanations:** Breaks down complex financial terms and concepts into simple, friendly language.

## How It Works
1. **Document Loading:** The assistant loads and processes PDF documents using PyMuPDF.
2. **Retrieval-Augmented Generation (RAG):** Uses sentence transformers and cross-encoders to find and rank the most relevant document sections for a given query.
3. **LLM Response:** Generates clear, context-aware answers using Google Gemini models.
4. **Voice Synthesis:** Optionally reads responses aloud using ElevenLabs.

## Setup
1. **Clone the repository** and navigate to the project directory.
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   - Create a `.env` file in the project root with your API keys:
     ```env
     GOOGLE_API_KEY=your_google_api_key
     ELEVENLABS_API_KEY=your_elevenlabs_api_key
     ```

## Usage
- **Command Line:**
  Run the main script and follow the prompts to analyze a document:
  ```bash
  python main.py
  ```
- **Jupyter Notebooks:**
  Explore and interact with the assistant using `chatbot.ipynb` or `main.ipynb`.

## File Structure
- `main.py` / `main.ipynb`: Core logic for document analysis and Q&A.
- `chatbot.py` / `chatbot.ipynb`: Conversational interface and workflow.
- `voice.py` / `voice.ipynb`: Voice synthesis utilities.
- `requirements.txt`: Python dependencies.

## Requirements
- Python 3.8+
- Google Generative AI API key
- ElevenLabs API key (for voice output)

## Disclaimer
This tool is for informational and educational purposes only. It does not provide financial advice. Always consult a qualified professional for financial decisions.

---

*Developed by Ahmed Ismail.* 