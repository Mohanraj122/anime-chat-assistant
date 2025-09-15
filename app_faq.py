import json
from flask import Flask, render_template, request, jsonify
from rapidfuzz import process, fuzz
import os

app = Flask(__name__)

FAQ_PATH = os.path.join(os.path.dirname(__file__), "faqs.json")

def load_faqs():
    """Read faqs.json and return list of dicts."""
    with open(FAQ_PATH, "r", encoding="utf8") as f:
        return json.load(f)

# initial load (we'll optionally reload on each request if you want live edits)
faqs = load_faqs()
questions = [item["q"] for item in faqs]

# You can set this to True to reload faqs.json on every /chat call (no restart needed)
AUTO_RELOAD_FAQS = False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True) or {}
    msg = data.get("message", "").strip()
    if not msg:
        return jsonify({"error": "Empty message"}), 400

    global faqs, questions
    if AUTO_RELOAD_FAQS:
        faqs = load_faqs()
        questions = [item["q"] for item in faqs]

    # fuzzy-match user's message to our questions
    best = process.extractOne(msg, questions, scorer=fuzz.WRatio)
    if best:
        matched_question = best[0]
        score = best[1]
        # tune threshold for your use-case (60 is moderate)
        THRESHOLD = 60
        if score >= THRESHOLD:
            idx = questions.index(matched_question)
            answer = faqs[idx]["a"]
            source = "faq"
        else:
            answer = "Sorry, I don't have that answer. Try contacting student services."
            source = "fallback"
    else:
        answer = "Sorry, I don't understand."
        source = "fallback"
        score = 0

    return jsonify({"answer": answer, "source": source, "score": score})

if __name__ == "__main__":
    # DO NOT use debug=True in production
    app.run(host="127.0.0.1", port=5000, debug=True)
