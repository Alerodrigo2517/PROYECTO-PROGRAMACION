import mysql.connector
import streamlit as st
import pandas as pd
import os 

from consultas.conexion import conexion_general;

def obtener_proveedores():
    cursor,var_conexion=conexion_general()
    script_consulta= """
        SELECT
            proveedor_materiales.id_proveedor_materiales as ID,
            proveedor_materiales.nombre as Nombre,
            proveedor_materiales.rubro as Rubro,
            proveedor_materiales.telefono as Telefono
        From
            proveedor_materiales 
    """
    cursor.execute(script_consulta)
    resultado=cursor.fetchall()
    cursor.close()
    var_conexion.close()
    return True if resultado else False



def ingresar_proveedor(nombre,rubro,telefono):
    cursor,var_conexion=conexion_general()
    script_consulta="""
        INSERT INTO proveedor_materiales(nombre,rubro,telefono)
        
        VALUES
            (%s, %s, %s)
    """
    cursor.execute (script_consulta,(nombre,rubro,telefono))
    var_conexion.commit()
    cursor.close()
    var_conexion.close()
    
def actualizar_proveedores(id_proveedor,nombre,rubro,telefono):
    cursor,var_conexion=conexion_general()
    script_actualizacion="""
        UPDATE  proveedor_materiales
        SET  nombre= %s,
            rubro= %s,
            telefono= %s
        WHERE id_proveedor_materiales= %s
    """
    cursor.execute(script_actualizacion, (nombre, rubro, telefono, int(id_proveedor)))
    var_conexion.commit()
    cursor.close()
    var_conexion.close()
    
def verificar_nombre_proveedor(nombre):
    cursor, var_conexion = conexion_general()
    
    query = "SELECT proveedor_materiales.nombre FROM proveedor_materiales WHERE proveedor_materiales.nombre = %s"
    cursor.execute(query, (nombre,))
    resultado = cursor.fetchone()
    cursor.close()
    var_conexion.close()
    return True if resultado else False

    
def verificar_telefono_proveedor(telefono):
    cursor, var_conexion = conexion_general()
    
    query = "SELECT proveedor_materiales.telefono FROM proveedor_materiales WHERE proveedor_materiales.telefono = %s"
    cursor.execute(query, (telefono,))
    resultado = cursor.fetchone()
    cursor.close()
    var_conexion.close()
    return True if resultado else False


def eliminar_proveedores(id_proveedor):
    cursor,var_conexion=conexion_general()
    script_eliminacion= """
        DELETE FROM proveedor_materiales where id_proveedor_materiales= %s
    """
    cursor.execute(script_eliminacion,(int(id_proveedor),))
    var_conexion.commit()
    cursor.close()
    var_conexion.close()


    