import mysql.connector
import streamlit as st
import pandas as pd

from consultas.conexion import conexion_general

def obtener_datos_ubicacion_trabajo ():
    
    cursor, var_conexion= conexion_general()
    script_consulta = """
        SELECT
            ubicacion_trabajo.id_ubicacion as ID,
            ubicacion_trabajo.domicilio as DOMICILIO,
            ubicacion_trabajo.ciudad as CIUDAD
        FROM
            ubicacion_trabajo;
            
    """
    cursor.execute (script_consulta)
    resultado = cursor.fetchall()
    return resultado

def ingresar_datos_ubicacion (du_domicilio,du_ciudad):
    
    cursor, var_conexion= conexion_general()
    script_consulta = """
        INSERT INTO ubicacion_trabajo (domicilio,ciudad)
        
        VALUES 
            (%s, %s)
            
    """
    cursor.execute (script_consulta,(du_domicilio,du_ciudad))
    var_conexion.commit()

def actualizar_datos(_original_du_domicilio,du_domicilio,du_ciudad):
    cursor, var_conexion = conexion_general()
    
    script_actualizacion = """
        UPDATE ubicacion_trabajo
        SET domicilio= %s, 
            ciudad = %s
        WHERE id_ubicacion= %s
    """
    cursor.execute (script_actualizacion,(du_domicilio, du_ciudad, _original_du_domicilio))
    var_conexion.commit()

def eliminar_datos(id_ubicacion):
    cursor, conn = conexion_general()
    script_eliminacion = "DELETE FROM ubicacion_trabajo WHERE id_ubicacion = %s"
    try:
        cursor.execute(script_eliminacion, (id_ubicacion,))  # tupla con un solo valor
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar ubicación: {e}")
        return False
    
def verificar_domicilio_existente(domicilio, ciudad):
    cursor, var_conexion = conexion_general()
    query = """
        SELECT domicilio 
        FROM ubicacion_trabajo 
        WHERE domicilio = %s AND ciudad = %s
    """
    cursor.execute(query, (domicilio, ciudad))
    resultado = cursor.fetchone()
    return True if resultado else False
