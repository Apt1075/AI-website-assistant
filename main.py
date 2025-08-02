from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import certifi
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class QueryRequest(BaseModel):
    url: str
    question: str

def scrape_website(url: str) -> str:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10, verify=certifi.where())
        soup = BeautifulSoup(response.text, "html.parser")
        texts = soup.get_text(separator=' ', strip=True)
        return texts[:7000] 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def ask_openai(context: str, question: str) -> str:
    prompt = f"""
    You are an assistant who answers questions based strictly on the website content below.
    Website Content:
    '''{context}'''
    
    Question: {question}
    Answer:
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "Answer only from the website content provided."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API Error: {str(e)}")

@app.post("/ask")
def answer_from_website(data: QueryRequest):
    content = scrape_website(data.url)
    answer = ask_openai(content, data.question)
    return {"answer": answer}
