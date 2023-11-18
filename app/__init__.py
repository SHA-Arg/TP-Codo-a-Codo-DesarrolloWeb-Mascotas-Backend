from flask import Flask

from utils import db
from models import Pet
from routes import pets

app = Flask(__name__)

app.register_blueprint(pets)

def create_app(enviroment):
    app.config.from_object(enviroment)
    
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app
