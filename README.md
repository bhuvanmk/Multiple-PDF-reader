## Requirements.txt ##

streamlit
python-dotenv
pypdf2
langchain
langchain-community
langchain-huggingface
langchain-openai
faiss-cpu
llama-cpp-python
transformers
sentence-transformers
torch

# Multiple PDFs Chatbot (Offline AI)

An AI-powered Streamlit application that allows you to **chat with multiple PDFs** using **local AI models** like TinyLlama and **HuggingFace embeddings**.  
The app extracts text from uploaded PDFs, chunks it, stores it in a FAISS vector database, and answers your questions conversationally.

##  Features
-  Upload and process **multiple PDF files**
-  Works **offline** with `LlamaCpp` local models
-  Uses **HuggingFace all-MiniLM-L6-v2** embeddings (~22MB, fast & lightweight)
-  Conversational memory to remember chat history
-  Modern UI with Streamlit

##  Installation

###  Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Multiple-PDF-reader.git
cd Multiple-PDF-reader


## Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


## Install dependencies ##
pip install -r requirements.txt


## Run the Streamlit app ##
streamlit run app.py


📦 Multiple-PDF-reader
├── app.py                 # Main Streamlit app
├── htmlTemplates.py       # HTML & CSS templates
├── requirements.txt       # Python dependencies
├── models/                # Local AI models (TinyLlama)
└── README.md              # Project documentation


##  .env  ###
OPENAI_API_KEY=your_openai_key_here
HUGGINGFACE_TOKEN=your_huggingface_token_here
