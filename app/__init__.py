from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

mail = Mail()



def create_app():
    app = Flask(__name__)
    app.config['MAIL_SERVER'] = 'smtp.dreamhost.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = 'amit@palinfocom.com'
    app.config['MAIL_PASSWORD'] = 'As@33$45Fg%6R'
    app.config["JWT_SECRET_KEY"] = "UDB_UDB_123" # replace with your own secret key
    jwt = JWTManager(app)

    
    mail.init_app(app)
    CORS(app)

    from .api.routes import api
    app.register_blueprint(api)

    return app
