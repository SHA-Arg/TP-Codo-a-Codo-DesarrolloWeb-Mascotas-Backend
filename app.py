# --- Manejo centralizado de errores ---
from flask import jsonify

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found', 'message': str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error', 'message': str(error)}), 500

# --- Endpoint de smoke test ---
@app.route('/health')
def health():
    return jsonify({'status': 'ok'}), 200
import os
from flask import Flask
from routes import pets, organization
from utils.config import db, ma
from flask_cors import CORS

# Instancia Flask
app = Flask(__name__)

# Configuración segura usando variables de entorno
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'mysql://user:password@localhost/patitas')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = os.environ.get('SQLALCHEMY_ECHO', 'False') == 'True'
app.config['FOLDER_IMG_PETS'] = 'public/images/pets'

# Inicializar extensiones
db.init_app(app)
ma.init_app(app)
CORS(app)

# Registrar Blueprints
app.register_blueprint(pets)
app.register_blueprint(organization)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False)
