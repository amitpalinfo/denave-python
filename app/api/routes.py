from flask import Blueprint, jsonify, request
from flask_mail import Message
from .. import mail

import smtplib
from email.mime.text import MIMEText

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return 'Hello, World!'

@api.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    name = "Amit"
    email = data.get('recipient')
    message = "Following are the download link as per your request"
    
    msg = Message('Denave downlaod link', sender='amit@palinfocom.com', recipients=[email])
    msg.body = f'Hi {name},\n\n{message}'
    msg.html = f'<h1>Hello {name}</h1><br> {message}'

    
    mail.send(msg)
    
    return jsonify({'status': True})
