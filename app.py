import os
from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
app.secret_key = os.getenv("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", "dev_secret_key")

SYSTEM_PROMPT = (
    "You are a helpful FAQ assistant for a college website. Keep answers short and friendly."
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    # Load or init conversation history in session (keeps last N messages)
    history = session.get("history", [{"role": "system", "content": SYSTEM_PROMPT}])

    # Append user message
    history.append({"role": "user", "content": user_message})

    try:
        # Call OpenAI ChatCompletion
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",           # change model if you have access to others
            messages=history,
            max_tokens=300,
            temperature=0.2,
        )
        assistant_msg = resp["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Append assistant message and trim history to last 10 messages
    history.append({"role": "assistant", "content": assistant_msg})
    session["history"] = history[-10:]

    return jsonify({"answer": assistant_msg})

@app.route("/clear", methods=["POST"])
def clear():
    session.pop("history", None)
    return jsonify({"status": "cleared"})

if __name__ == "__main__":
    app.run(debug=True)
