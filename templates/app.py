from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.secret_key =os.getenv('FLASK_SECRET_KEY', '123')

app.config['MAIL_SERVER'] = 'smtp.gamil.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USER_NAME'] = os.getenv('MAIL_USER_NAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USER_NAME']


mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']

        #crear el mensaje del correo
        msg = Message('Nuevo mensaje de contacto',
                      sender=app.config['MAIL_USERMANE'],
                      recipients=[app.config['MAIL_USERMANE']])
        msg.body = f"Nombre: {nombre}\nCorreo:{correo}\nMensaje:{mensaje}"

        #enviar mensaje
        mail.send(msg)
        flash("Mensaje enviado correctamente.", "succes")
    except Exception as e:
        print(f"error: {e}")
        flash("Ocurrio un erro al enviar el mensaje. Intenta de nuevo más tarde", "danger")

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)