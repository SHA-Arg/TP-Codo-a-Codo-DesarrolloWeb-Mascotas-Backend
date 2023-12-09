from flask import session


# creando una funcion y dentro de la misma una data (un diccionario)
# con valores del usuario ya logueado
def dataLoginSesion():
    inforLogin = {
        "idLogin": session['id'],
        "tipoLogin": session['tipo_user'],
        "nombre": session['nombre'],
        "apellido": session['apellido'],
        "emailLogin": session['email'],
        "direccion": session['direccion'],
    }
    return inforLogin


def dataPerfilUsuario():
    conexion_MySQLdb = connectionBD()
    mycursor = conexion_MySQLdb.cursor(dictionary=True)
    idUser = session['id']

    querySQL = ("SELECT * FROM login_python WHERE id='%s'" % (idUser,))
    mycursor.execute(querySQL)
    datosUsuario = mycursor.fetchone()
    mycursor.close()  # cerrrando conexion SQL
    conexion_MySQLdb.close()  # cerrando conexion de la BD
    return datosUsuario
