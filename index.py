from utils.config import db, ma
from app import app


#Crea las tablas cuando se ejecuta la aplicación
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        ma.init_app(app)
    app.run(debug = True)