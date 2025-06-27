# AI Financial Assistant - "William"

An intelligent financial assistant to help you analyze complex corporate financial documents like 10-K filings and earnings call transcripts. "William" uses advanced AI to extract key insights, answer your questions, and summarize dense financial information in an easy-to-understand manner.

🌟 **Features**

- 📄 **Document Analysis:** Upload and analyze financial PDF documents.
- 💬 **Conversational AI:** Interact with "William" through an intuitive chat interface.
- 🔊 **Voice Output:** Get responses read aloud for a hands-free experience.
- 🧠 **User-Friendly Explanations:** Simplifies complex financial terminology and concepts.

🚀 **How It Works**

The AI Financial Assistant leverages a powerful combination of technologies to deliver insightful analysis:

- **Document Loading:** It uses PyMuPDF to process and extract text from your uploaded PDF documents.
- **Retrieval-Augmented Generation (RAG):** The core of the assistant, this process uses sentence transformers and cross-encoders to find the most relevant sections of the document to answer your questions.
- **LLM Response Generation:** It uses Google's powerful Gemini models to generate accurate and context-aware answers.
- **Voice Synthesis:** Optionally, it can read the generated responses aloud using ElevenLabs' realistic text-to-speech technology.

🛠️ **Getting Started**

Follow these steps to set up and run the AI Financial Assistant on your local machine.

### Prerequisites

Make sure you have the following installed:
- Python 3.8 or higher
- An API key from Google AI for Developers
- An API key from ElevenLabs (optional, for voice output)

### Installation

Clone the repository:
```bash
git clone https://github.com/ahmedismail06/AI-Financial-Assistant.git
cd AI-Financial-Assistant
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

Set up your environment variables:
Create a file named `.env` in the root directory of the project and add your API keys as follows:
```env
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
ELEVENLABS_API_KEY="YOUR_ELEVENLABS_API_KEY"
```

▶️ **Usage**

You can run the AI Financial Assistant either from the command line or using the provided Jupyter Notebooks.

#### Command Line
To start the assistant from the command line, run:
```bash
python main.py
```

#### Jupyter Notebooks
For a more interactive experience, you can use the Jupyter Notebooks:
- `chatbot.ipynb`: A notebook focused on the conversational interface.
- `main.ipynb`: The main notebook containing the core logic of the application.

📂 **File Structure**
```
.
├── main.py               # Core logic of the application
├── chatbot.py            # Conversational interface
├── voice.py              # Voice synthesis utilities
├── main.ipynb            # Jupyter Notebook with the core logic
├── chatbot.ipynb         # Jupyter Notebook for the conversational interface
├── voice.ipynb           # Jupyter Notebook for voice utilities
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

🤝 **Contributing**

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

📄 **License**

This project is licensed under the Apache 2.0 License. See the LICENSE file for details.

---

**Disclaimer**

This tool is intended for informational and educational purposes only. It is not financial advice. Please consult with a qualified financial professional before making any investment decisions. 