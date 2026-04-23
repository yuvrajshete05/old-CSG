# app1/utils.py

import requests

def get_gemini_key():
    # Replace this with your actual Gemini API key
    return "your-api-key"

def ask_gemini(prompt):
    if not prompt:
        return "Prompt is empty."

    API_KEY = get_gemini_key()
    URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"Error: {e}"
