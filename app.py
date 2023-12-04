from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

from flask import Flask, render_template, request, redirect, url_for, session
from routes import pets, organization
from utils.config import *


# Instancia Flask. __name__ indica el módulo en el que se encuentra.
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# Configuración de la base de datos


# Conexion con la base de datos
# Configura la variable de la carpeta de imágenes
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


# PRUEBA 2

# # Configuración de la base de datos
# app.config['MYSQL_HOST'] = 'S3B4.mysql.pythonanywhere-services.com'
# app.config['MYSQL_USER'] = 'S3B4'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'S3B4$login_TP'

# # Inicialización de la base de datos
# mysql = MySQL(app)

# # Clave secreta para la gestión de sesiones.
# app.secret_key = 'your_secret_key'

# # Ruta para la página de inicio de sesión


# @app.route('/')
# def login():
#     return render_template('login.html')

# # Ruta para manejar la lógica de inicio de sesión


# @app.route('/login', methods=['POST'])
# def login_post():
#     username = request.form['username']
#     password = request.form['password']
#     cursor = mysql.connection.cursor()

#     # Comprobar si el usuario existe en la base de datos.
#     cursor.execute(
#         "SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
#     user = cursor.fetchone()
#     if user:
#         # Si el usuario existe, almacene la información del usuario en la sesión.
#         session['user_id'] = user[0]
#         session['username'] = user[1]
#         return redirect(url_for('dashboard'))
#     else:
#         return redirect(url_for('login'))

# # Ruta para la página de registro de usuario.


# @app.route('/register')
# def register():
#     return render_template('register.html')

# # Ruta para manejar la lógica de registro de usuarios.


# @app.route('/register', methods=['POST'])
# def register_post():
#     username = request.form['username']
#     password = request.form['password']
#     cursor = mysql.connection.cursor()
#     # Compruebe si el nombre de usuario ya está en uso
#     cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
#     existing_user = cursor.fetchone()
#     if existing_user:
#         return "Username already taken. Please choose another."
#     # Insertar el nuevo usuario en la base de datos
#     cursor.execute(
#         "INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
#     mysql.connection.commit()
#     # Inicio de sesión como usuario recién registrado
#     session['user_id'] = cursor.lastrowid
#     session['username'] = username
#     return redirect(url_for('dashboard'))

# # Ruta para el dashboard


# @app.route('/dashboard')
# def dashboard():
#     # Comprobar si el usuario ha iniciado sesión
#     if 'user_id' in session:
#         return f"Welcome, {session['username']}! This is your dashboard."
#     else:
#         return redirect(url_for('login'))

# # Ruta para cerrar sesión


# @app.route('/logout')
# def logout():
#     # Limpiar la sesión
#     session.clear()
#     return redirect(url_for('login'))


# if __name__ == '__main__':
#     app.run(debug=True)
