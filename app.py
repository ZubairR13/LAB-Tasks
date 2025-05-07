from flask import Flask, request, jsonify, render_template
import requests
from hospital_data import hospital_data  # ⬅️ Imported context

app = Flask(__name__)

# API Key and endpoint for Together AI
API_KEY = "2fcafa7245fe49c4c7a23e391eeeeebcd99f197fbad41ab4d6118625c4acee79"
TOGETHER_URL = "https://api.together.xyz/v1/completions"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message')

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = (
        "You are a polite, knowledgeable, and accurate virtual assistant for Shaukat Khanum Memorial Cancer Hospital and Research Centre (SKMCH&RC). "
        "Your role is to help patients and visitors by answering questions using the hospital information provided below. "
        "Keep your answers short, clear, and to the point. Do not make up information.\n\n"
        f"=== HOSPITAL INFORMATION ===\n{hospital_data}\n"
        f"============================\n\n"
        f"Patient: {user_input}\nAssistant:"
    )

    payload = {
        "model": "meta-llama/Llama-3-8b-chat-hf",
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.3,
        "top_p": 0.9,
        "stop": ["Patient:", "Assistant:"]
    }

    try:
        res = requests.post(TOGETHER_URL, headers=headers, json=payload)
        res.raise_for_status()
        result = res.json()
        reply = result["choices"][0]["text"].strip()
        return jsonify({"response": reply})
    except Exception as err:
        print(f"Error occurred: {err}")
        return jsonify({"response": "Sorry, I'm unable to reach the medical server right now."})

if __name__ == '__main__':
    app.run(debug=True)
