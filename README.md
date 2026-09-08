# Q&A Academy Portal

A single mobile-friendly page where visitors answer a question you set,
and their answer is sent straight to your WhatsApp when they hit Send.
Built with **Python (Flask) + HTML only — no JavaScript anywhere.**

## How the WhatsApp part works (no JS needed)
The Send button submits a normal HTML form to Flask. Flask reads the
answer, builds a WhatsApp deep link (`https://wa.me/...?text=...`) with
the question and answer pre-filled, and redirects the visitor's browser
straight to WhatsApp. That's the entire mechanism — no JavaScript, no
API keys, nothing else required.

## Before you run it — edit 3 values
Open `app.py` and change these three lines at the top:

```python
WHATSAPP_NUMBER = "920000000000"   # Your number, country code first, NO + and NO spaces
YOUR_NAME = "Your Name"             # Shown in the welcome box
CURRENT_QUESTION = "What did you enjoy most about today's session?"  # The question visitors answer
```

That's the only editing required to make this fully yours.

## Run locally
```bash
pip install -r requirements.txt
python app.py
```
Open **http://localhost:5000** on your phone or browser.

## Project structure
```
qa-portal/
├── app.py                 Flask app — all 3 config values live here
├── requirements.txt
├── Procfile                For gunicorn-based hosting platforms
├── templates/
│   └── index.html           The page (welcome / question / answer boxes)
└── static/
    └── css/style.css         Neon academy theme
```

## Deploying (Render, Railway, Coolify, VPS, etc.)
- **Root Directory:** the project root (the folder containing `app.py`)
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn -w 2 -b 0.0.0.0:$PORT app:app` (or let the
  platform auto-detect the included `Procfile`)
- The app reads `PORT` from the environment automatically — no changes needed.

## Changing the question later
Just edit `CURRENT_QUESTION` in `app.py` and restart/redeploy — there's
no database or admin panel, since this was built as a simple single-question
tool. If you want to change the question often without redeploying, let me
know and I can add a small config file or admin page for that.

## Note
Nothing typed by visitors is stored anywhere — it goes directly to
WhatsApp and nowhere else, exactly as requested.
