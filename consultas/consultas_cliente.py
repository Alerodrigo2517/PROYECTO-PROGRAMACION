import mysql.connector
import streamlit as st
import pandas as pd
import os 

from consultas.conexion import conexion_general;


def obtener_datos ():
    
    cursor, var_conexion= conexion_general()
    script_consulta = """
        SELECT
            datos_clientes.cuilt_cliente as CUILT,
            datos_clientes.nombre as NOMBRE,
            datos_clientes.apellido as APELLIDO,
            datos_clientes.direccion as DOMICILIO,
            datos_clientes.ciudad as CIUDAD,
            datos_clientes.telefono as TELEFONO
        From 
            datos_clientes;
            
    """
    cursor.execute (script_consulta)
    resultado = cursor.fetchall()
    return resultado

def ingresar_datos (dc_cuilt,dc_nombre,dc_apellido,dc_direccion,dc_ciudad,dc_telefono):
    
    cursor, var_conexion= conexion_general()
    script_consulta = """
        INSERT INTO datos_clientes (cuilt_cliente, nombre, apellido, direccion, ciudad, telefono)
        
        VALUES 
            (%s, %s, %s, %s, %s,%s)
    
    """
    cursor.execute (script_consulta,(dc_cuilt,dc_nombre,dc_apellido,dc_direccion,dc_ciudad,dc_telefono))
    var_conexion.commit()
    cursor.close()
    var_conexion.close()
    

    
def actualizar_datos(cuilt_original, nuevo_cuilt, nombre, apellido, direccion, ciudad, telefono):
    cursor, var_conexion = conexion_general()
    
    script_actualizacion = """
        UPDATE datos_clientes
        SET cuilt_cliente = %s,
            nombre = %s,
            apellido = %s,
            direccion = %s,
            ciudad = %s,
            telefono = %s
        WHERE cuilt_cliente = %s
    """
    
    cursor.execute(script_actualizacion, (nuevo_cuilt,nombre,apellido,direccion,ciudad,telefono,cuilt_original))
    
    var_conexion.commit()
    cursor.close()
    var_conexion.close()
    
def eliminar_datos(cuilt_cliente):
    cursor,var_conexion=conexion_general()
    script_eliminacion= """
        DELETE FROM datos_clientes where cuilt_cliente= %s
    """
    cursor.execute(script_eliminacion, (cuilt_cliente,))

    var_conexion.commit()
    cursor.close()
    var_conexion.close()
    
def tiene_presupuestos_asociados(cuilt_cliente):
    cursor, conexion = conexion_general()
    
    query = """
        SELECT fk_datos_clientes FROM presupuesto WHERE fk_datos_clientes = %s
    """
    cursor.execute(query, (cuilt_cliente,))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()
    
    return True if resultado else False



def verificar_cuilt_existente(dc_cuilt):
    cursor, var_conexion = conexion_general()
    
    query = "SELECT datos_clientes.cuilt_cliente FROM datos_clientes WHERE datos_clientes.cuilt_cliente = %s"
    cursor.execute(query, (dc_cuilt,))
    resultado = cursor.fetchone()
    return True if resultado else False




