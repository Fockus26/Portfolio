from flask import Flask, render_template, request
from dotenv import load_dotenv
from datetime import datetime
import smtplib
import os

load_dotenv()

def send_email(name, email, msg):
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("alejandrorey2654@gmail.com", os.getenv("GMAIL_APP_PASSWORD"))
        server.sendmail("alejandrorey2654@gmail.com", "alejandrorey2654@gmail.com",
                        f"Subject:Portfolio | {name} | {email}\n\n{msg}")

app = Flask(__name__)

@app.context_processor
def inject_datetime():
    return {'datetime': datetime}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        send_email(name=request.form.get("name"), email=request.form.get("email"), msg=request.form.get('message_hidden'))
        return render_template("contact.html", form_sended=["MESSAGE SENDED", "I will contact you!"])
    return render_template("contact.html", form_sended=["CONTACT", "Let's to talk!"])

@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)