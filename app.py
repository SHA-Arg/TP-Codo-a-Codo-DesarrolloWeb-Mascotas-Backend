from flask import Flask
from routes import pets, organization
from utils.config import db, ma


# Instancia Flask. __name__ indica el módulo en el que se encuentra.
app = Flask(__name__)

# Conecta con la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/patitas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

#Configura la variable de la carpeta de imágenes
app.config['FOLDER_IMG_PETS'] = 'public/images/pets'


# Asocia la instancia de SQLAlchemy con la aplicación
db.init_app(app)
ma.init_app(app)



# Registra el Blueprint
app.register_blueprint(pets)
app.register_blueprint(organization)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


