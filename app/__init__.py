from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
mail = Mail()



def create_app():
    app = Flask(__name__)
    app.config['MAIL_SERVER'] = 'smtp.dreamhost.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = 'amit@palinfocom.com'
    app.config['MAIL_PASSWORD'] = 'As@33$45Fg%6R'
    
    mail.init_app(app)
    CORS(app)

    from .api.routes import api
    app.register_blueprint(api)

    return app
