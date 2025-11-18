import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

def conexion_general():
    var_conexion = None 
    cursor = None       
    try:
        var_conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cursor = var_conexion.cursor(dictionary=True)
        print("✅ Conexión exitosa a la base de datos")

    except Error as e:
        print(f"❌ Error al conectar a la base de datos: {e}")

    return cursor, var_conexion

if __name__ == "__main__":
    cursor, conexion = conexion_general()
    if cursor and conexion: # Asegurarse de que la conexión y el cursor existen
        try:
            print("Conexión activa. Aquí puedes realizar operaciones con la DB.")
            # Ejemplo de una operación
            # cursor.execute("SELECT VERSION()")
            # version = cursor.fetchone()
            # print(f"Versión de MySQL: {version}")

        except Error as e:
            print(f"Error durante la operación con la base de datos: {e}")
        finally:
            if cursor:
                cursor.close()
                print("Cursor cerrado.")
            if conexion:
                conexion.close()
                print("Conexión a la base de datos cerrada.")
    else:
        print("No se pudo establecer la conexión a la base de datos.")
        
def obtener_datos():
    cursor,var_conexion=conexion_general()
    
    print (cursor)
    
    script_consulta= "select * FROM usuario "

    resultado= cursor.fetchall()
    
    return resultado