import mysql.connector
import streamlit as st
import pandas as pd
import os 

from consultas.conexion import conexion_general;

def obtener_materiales():
    cursor, var_conexion = conexion_general()
    script_consulta = """
        SELECT
            m.id_material AS ID,
            m.descripcion AS Descripcion,
            m.precio_unitario AS Precio,
            p.id_proveedor_materiales as ID_PROVEEDOR,
            p.rubro as rubro,
            p.nombre AS Proveedor
        FROM
            materiales m
        INNER JOIN proveedor_materiales p
            ON m.fk_proveedor_materiales = p.id_proveedor_materiales;
    """
    cursor.execute(script_consulta)
    resultado = cursor.fetchall()
    return resultado

def ingresar_materiales(descripcion,precio_unitario,proveedor):
    cursor, var_conexion= conexion_general()
    script_consulta="""
        INSERT INTO  materiales(descripcion,precio_unitario,fk_proveedor_materiales)
        
        VALUES
            (%s,%s,%s)
    """
    cursor.execute(script_consulta,(descripcion,precio_unitario,int(proveedor)))
    var_conexion.commit()
    cursor.close()
    var_conexion.close()
    
def actualizar_material(id_material,descripcion,precio_unitario,proveedor):
    cursor,var_conexion=conexion_general()
    
    script_actualizacion="""
        UPDATE materiales 
        SET descripcion=%s,
            precio_unitario=%s,
            fk_proveedor_materiales=%s
        WHERE id_material=%s
        
    """
    cursor.execute(script_actualizacion, (id_material, descripcion, precio_unitario, proveedor))
    var_conexion.commit()
    cursor.close()    
    var_conexion.close()
    
def  eliminar_materiales(id_materiales):
    cursor,var_conexion=conexion_general()
    script_eliminacion="""
    DELETE FROM  materiales where id_material= %s
    """
    cursor.execute(script_eliminacion(id_materiales))
    var_conexion.commit()
    cursor.close()
    var_conexion.close()
    