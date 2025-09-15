# Anime FAQ Chatbot

🌸 **Anime FAQ Chatbot** — A simple Flask-based FAQ assistant with an anime-inspired animated UI. It uses `faqs.json` as the knowledge base and `rapidfuzz` for fuzzy matching.

---

## Features

* Lightweight Flask backend (`app_faq.py`).
* Anime-styled animated UI (`templates/index.html`).
* FAQ storage in `faqs.json` (easy to edit).
* Fast fuzzy matching with `rapidfuzz`.
* Dockerfile included for containerized runs.

---

## Quick setup (one-minute summary)

1. Clone repo
2. Create & activate Python virtual environment
3. Install requirements
4. Run `python app_faq.py`

Full step-by-step instructions below.

---

## Prerequisites

* Python 3.8+ installed
* `git` (optional but recommended)
* (Optional) Docker if you want to run as a container

---

## Step-by-step installation & run

Follow the steps for your platform.

### 1) Clone or copy the repository

If you already have the repo locally skip this step. Otherwise:

```bash
# using HTTPS
git clone https://github.com/YOUR_GITHUB_USERNAME/anime-faq-chatbot.git
cd anime-faq-chatbot
```

Or create the folder and paste the project files manually.

### 2) Create and activate a virtual environment

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell)**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (cmd.exe)**

```cmd
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` prefix in your shell.

### 3) Install Python dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` contains at least:

```
Flask
rapidfuzz
python-dotenv
```

If you plan to deploy with **Gunicorn** (Linux), install it too:

```bash
pip install gunicorn
```

### 4) Inspect `faqs.json` and `app_faq.py`

* Open `faqs.json` and add/edit Q/A pairs. This file is the bot's knowledge base.
* If you want the server to auto-reload FAQs when you edit `faqs.json`, set `AUTO_RELOAD_FAQS = True` inside `app_faq.py` (default is `False`).

**Tip:** Add friendly variations for greetings (`hi`, `hello`, `who are you`) so fuzzy matching finds them.

### 5) Run the app locally

```bash
python app_faq.py
```

You should see output like:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Open your browser at: `http://127.0.0.1:5000/` and test the chatbot.

### 6) (Optional) Use Docker

Build the image:

```bash
docker build -t anime-faq-chatbot .
```

Run the container (maps container port 5000 to host 5000):

```bash
docker run -p 5000:5000 anime-faq-chatbot
```

Then visit `http://localhost:5000`.

### 7) (Optional) Production with Gunicorn + Nginx

**Install gunicorn** (on server):

```bash
pip install gunicorn
```

Run with gunicorn (bind to all interfaces):

```bash
gunicorn --workers 3 --bind 0.0.0.0:5000 app_faq:app
```

Use Nginx as a reverse proxy for SSL and to serve static assets in production.

**Important:** Set `debug=False` in `app_faq.py` for production.

---

## GitHub: create & push (if you want to publish)

```bash
git init
git add .
git commit -m "Initial commit — anime FAQ chatbot"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/anime-faq-chatbot.git
git push -u origin main
```

If you use GitHub CLI (`gh`):

```bash
gh repo create anime-faq-chatbot --public --source=. --remote=origin --push
```

---

## Troubleshooting

* **`FileNotFoundError: faqs.json`**

  * Ensure `faqs.json` is in the project root (same folder as `app_faq.py`).
  * If you moved files, update `FAQ_PATH` in `app_faq.py` accordingly.

* **`ModuleNotFoundError` for rapidfuzz**

  * Run `pip install -r requirements.txt` and ensure the venv is active.

* **Cannot activate venv on PowerShell**

  * You may need to change ExecutionPolicy (run PowerShell as admin):

    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

* **Port 5000 already in use**

  * Stop the process using it or change the `port` argument in `app.run()`.

---

## Customization & next steps

* Replace fuzzy matching with semantic embeddings (`sentence-transformers`) for better natural language understanding.
* Integrate OpenAI or another LLM for richer conversational replies (requires API key).
* Add persistent conversation history (Redis) and authentication.
* Add unit tests for matching logic.

---

## Contributing

PRs welcome. If you add features, update `requirements.txt` and README accordingly.

---

## License

This project is available under the **MIT License**. See `LICENSE` or add one if you need.

---

## Contact

Created by **mohanraj**. Questions or improvements? Open an issue or send a PR.
