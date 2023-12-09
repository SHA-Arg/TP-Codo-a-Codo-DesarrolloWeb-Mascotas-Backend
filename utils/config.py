# Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector


def connectionBD():
    mydb = mysql.connector.connect(
        host="",
        user="u545683602_Admin",
        passwd="",
        database="u545683602_PatitasFelices"
    )
    return mydb
    '''       
    if mydb:
        return ("Conexion exitosa")
    else:
        return ("Error en la conexion a BD")
    '''
