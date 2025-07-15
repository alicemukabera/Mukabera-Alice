import random
import time
import requests
import schedule
from datetime import datetime
from openai import OpenAI

# ------------------------- Configuration --------------HF-----------

# OpenAI API client
openai_client = OpenAI(api_key="your_openai_api_key")  # Removed for security; replace with your actual key

# Telegram Bot configuration
TELEGRAM_TOKEN = "7617627646:AAE_a2sftEz5tWsY5RZUtbbvz_wnkmmLkt8"  # 🔐 Replace securely in production
CHAT_ID = "6055728788"

# Prompts for AI to generate engaging content
PROMPTS = [
    "Share a mind-blowing fact about real-time multimodal AI systems that’s perfect for a Telegram tech update.",
    "Write a motivational tech tip that encourages developers to embrace AI-assisted coding tools like GPT-5 Copilot.",
    "Describe a futuristic use of robotics powered by self-directed AI agents transforming daily life in smart cities.",
    "Create a brief and imaginative post on how quantum AI is accelerating deep learning model training.",
    "Craft a sharp, insightful line about digital privacy and the ethical implications of surveillance by autonomous AI agents.",
    "Write a tweet-style post showcasing the growing dominance of software engineering fused with AI orchestration tools.",
    "Post a fun, relatable insight about what it's like being a developer in the age of agentic workflows and LLM copilots.",
    "Share a visionary statement about the convergence of AI, IoT, edge computing, and real-time decision-making.",
    ]

# Optional image URL
IMAGE_URL = "https://picsum.photos/512"

# ------------------------- Core Logic -------------------------

def generate_ai_message() -> str:
    """Generates a short tech message using OpenAI."""
    try:
        prompt = random.choice(PROMPTS)
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a tech-savvy assistant who writes short, engaging tech insights."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=60,
            temperature=0.8,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[{datetime.now()}] AI generation error: {e}")
        return " AI is offline. Here's a manual tech tip: Stay curious, stay building! #Tech"

def send_to_telegram(message: str, image_url: str = None) -> None:
    """Sends a message (and optional image) to Telegram."""
    try:
        if image_url:
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
            payload = {
                "chat_id": CHAT_ID,
                "caption": message,
                "photo": image_url
            }
        else:
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            payload = {
                "chat_id": CHAT_ID,
                "text": message
            }

        response = requests.post(url, data=payload)
        if response.ok:
            print(f"[{datetime.now()}]  Telegram message sent successfully.")
        else:
            print(f"[{datetime.now()}] Telegram API error: {response.text}")
    except Exception as e:
        print(f"[{datetime.now()}] Telegram send error: {e}")

def run_bot() -> None:
    """Main function to generate and send AI-powered message."""
    print(f"[{datetime.now()}] Running AI Auto Poster Bot...")
    message = generate_ai_message()
    print(f"[{datetime.now()}] Generated message: {message}")
    send_to_telegram(message, image_url=IMAGE_URL)

# ------------------------- Scheduler -------------------------

if __name__ == "__main__":
    run_bot()  # Run immediately
    schedule.every(1).minutes.do(run_bot)

    print("Scheduling initialized. Bot will run every one minute.\n")

    while True:
        schedule.run_pending()
        time.sleep(1)
        
