# 🤖 AI Website Assistant

This is a FastAPI-based AI assistant that reads content from any website and answers questions based **only** on that content using OpenAI's GPT model (`gpt-3.5-turbo` or `gpt-4`).

---

## 🚀 Features

- 🌐 Scrapes any publicly accessible webpage
- 🧠 Uses OpenAI GPT to answer your questions
- 🔒 Answers only from website content (no external hallucination)
- ⚡ Built with FastAPI and BeautifulSoup

---

## 📦 Requirements

- Python 3.8+
- OpenAI API key (get from [OpenAI](https://platform.openai.com/account/api-keys))

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ai-website-assistant.git
   cd ai-website-assistant
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Create a virtual environment:**
   python -m venv venv
   source venv/bin/activate

4. **Set your OpenAI API Key:**
    Create a .env file in the project root:
    OPENAI_API_KEY=sk-your-openai-key

5. **Run the application:**
   uvicorn main:app --reload    
   Visit: http://127.0.0.1:8000/docs to test the API with Swagger UI.

6. **📬 API Endpoint**   
    POST /ask
    Request JSON:
    {
    "url": "https://example.com",
    "question": "What is this site about?"
    }
    Response JSON:
    {
    "answer": "This website is about..."
    }

7. **📁 File Structure**    
    ai-website-assistant/
├── main.py              # FastAPI app
├── .env                 # OpenAI API key
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation