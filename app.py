import os
from flask import Flask, send_from_directory, jsonify
from routes import pets, organization_bp
from utils.config import db, ma
from flask_cors import CORS

# Instancia Flask
app = Flask(__name__)

# Configuración segura usando variables de entorno
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///patitas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = os.environ.get('SQLALCHEMY_ECHO', 'False') == 'True'
app.config['FOLDER_IMG_PETS'] = 'public/images/pets'

# Inicializar extensiones
db.init_app(app)
ma.init_app(app)
CORS(app)

# Registrar Blueprints (API)
app.register_blueprint(pets)
app.register_blueprint(organization_bp)

# --- Endpoint de smoke test ---
@app.route('/health')
def health():
    return jsonify({'status': 'ok'}), 200

# --- Rutas para servir el frontend ---
FRONTEND_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'public'))

@app.route('/')
def serve_index():
    return send_from_directory(FRONTEND_FOLDER, 'index.html')

# Wildcard route DEBE ir al final para no capturar rutas de API
@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory(FRONTEND_FOLDER, filename)

# --- Manejo centralizado de errores (solo para API) ---
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error', 'message': str(error)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='127.0.0.1', port=5000)
