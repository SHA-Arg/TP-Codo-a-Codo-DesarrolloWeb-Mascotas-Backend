# Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector

# from SQLAlchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow

# db = SQLAlchemy()
# ma = Marshmallow()


def connectionBD():
    mydb = mysql.connector.connect(
        host="S3B4.mysql.pythonanywhere-services.com",
        user="S3B4",
        passwd="",
        database="S3B4$login_TP"
    )
    return mydb
    '''       
    if mydb:
        return ("Conexion exitosa")
    else:
        return ("Error en la conexion a BD")
    '''
