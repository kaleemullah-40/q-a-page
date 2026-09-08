"""
Q&A Academy Portal (Python / Flask)
--------------------------------------
A single mobile-friendly page where visitors answer a question you set,
and their answer is sent to your WhatsApp when they hit Send.

No JavaScript is used anywhere -- the "Send" button submits a normal HTML
form to Flask, which builds a WhatsApp deep link and redirects the
visitor's browser straight to WhatsApp with the message pre-filled.

------------------------------------------------------------------
EDIT THESE THREE VALUES BEFORE RUNNING:
------------------------------------------------------------------
"""

WHATSAPP_NUMBER = "920000000000"   # Your WhatsApp number, country code first, NO + and NO spaces
YOUR_NAME = "Your Name"             # Shown as the second line in the welcome box
CURRENT_QUESTION = "What did you enjoy most about today's session?"  # The question visitors will answer

# ------------------------------------------------------------------

import os
from urllib.parse import quote

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        your_name=YOUR_NAME,
        question=CURRENT_QUESTION,
    )


@app.route("/send", methods=["POST"])
def send():
    answer = (request.form.get("answer") or "").strip()

    if not answer:
        # No answer typed -- just send them back to the page instead of
        # opening WhatsApp with an empty answer.
        return redirect("/")

    message = f"New Q&A Response\n\nQuestion: {CURRENT_QUESTION}\n\nAnswer: {answer}"
    whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"
    return redirect(whatsapp_url)


@app.route("/api/health")
def health():
    return {"ok": True, "service": "Q&A Academy Portal"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    print(f"Q&A Academy Portal running at http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
