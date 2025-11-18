import mysql.connector
import streamlit as st
import pandas as pd
import os 

from consultas.conexion import conexion_general;

def obtener_presupuesto():
    cursor,var_conexion=conexion_general()
    script_consulta="""
    SELECT
        p.id_presupuesto as ID,
        p.fecha_presupuesto as "Fecha De Presupuesto",
        u.id_ubicacion as ubicacion,
        p.tipo_calculo as  " Tipo De Calculo ",
        p.costo_porcentaje as Porcentaje,
        p.costo_hora_trabajo as " Costo Hora",
        p.duracion_hora as " Horas Estimadas "
    FROM
        presupuesto_herreria p 
        
    INNER JOIN ubicacion_trabajo u
        ON p.fk_ubicacion_trabajo= u.id_ubicacion;
        
    """
    cursor.execute(script_consulta)
    resultado=cursor.fetchall()
    return resultado

def ingresar_presupuesto(id,fecha_presupuesto,ubicacion,tipo_calculo,porcentaje,costo_hora,horas_estimada):
    cursor,var_conexion=conexion_general()
    script_consulta="""
        INSERT INTO presupuesto(
            id_presupuesto,
            fecha_presupuesto,
            fk_ubicacion_trabajo,
            tipo_calculo,
            costo_porcentaje,
            costo_hora_trabajo,
            duracion_horas )
        VALUES
            (%s,%s,%s,%s,,%s,%s,%s)
    """
    cursor.execute(script_consulta(id,fecha_presupuesto,ubicacion,tipo_calculo,porcentaje,costo_hora,horas_estimada))
    var_conexion.commit()
    cursor.close()
    var_conexion.close
    
def eliminar_presupuesto(id_presupuesto):
    cursor,var_conexion=conexion_general()
    script_eliminacion="""
    DELETE FROM presupuesto where id_presupuesto= %s
    """
    cursor.execute(script_eliminacion(id_presupuesto))
    var_conexion.commit()
    cursor.close()