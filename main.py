from flask import Flask, render_template, request, redirect
from datetime import datetime
import urllib.parse

def send_whatsapp(name, email, message):
    # Tu número de WhatsApp (sin +)
    phone_number = "584149771310"

    # Codificamos el mensaje para que se vea bien en la URL
    text = f"Hola, soy {name} ({email}). \n\n{message}"
    encoded_text = urllib.parse.quote(text)

    # Creamos el enlace de WhatsApp
    whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_text}"

    # Redirigimos al usuario al chat de WhatsApp
    return redirect(whatsapp_url)

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
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get('message_hidden')
        
        return send_whatsapp(name=name, email=email, message=message)
    return render_template("contact.html", form_sended=["CONTACT", "Let's to talk!"])

@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8000)