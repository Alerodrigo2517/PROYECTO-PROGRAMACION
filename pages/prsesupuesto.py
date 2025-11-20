import streamlit as st
import pandas as pd 
import datetime
import time

from consultas.consulta_presupuesto  import ingresar_presupuesto,eliminar_presupuesto
from consultas.consulta_ubicacion_trabajo import obtener_datos_ubicacion_trabajo
from consultas.consultas_cliente import obtener_datos,obtener_cuilt

st.title ("Presupuesto")

def formulario_ingresar_datos ():
    _contenedor_formulario = st.container(border=True)
    txt_cuilt = st.text_input(label="Ingrese el CUILT ", max_chars=13 , placeholder="20-00000000-7")
    datos_clientes=None
    if txt_cuilt:
        datos_clientes=obtener_cuilt(txt_cuilt)
    with _contenedor_formulario:
        
        _col_nombre, _col_apellido= st.columns(2)
        
        with _col_nombre:
            txt_nombre = st.text_input(label= "Ingrese nombre del Cliente  ", max_chars = 45, placeholder="Juan Carlos ",value=datos_clientes.get("NOMBRE") if datos_clientes else"")

        with _col_apellido:
            txt_apellido = st.text_input(label= "Ingrese el apellido del cliente ", max_chars = 45,  placeholder="Perez",value=datos_clientes.get("APELLIDO") if datos_clientes else"")


        col_telefono, _col_domicilio,_col_ciudad = st.columns([2,2,2]) 
        with col_telefono: 
            txt_telefono = st.text_input(label= "Ingrese Teléfono ", max_chars = 12,  placeholder=" Teléfono del cliente",value=datos_clientes.get("TELEFONO") if datos_clientes else"")
        
        with _col_domicilio: 
            txt_domicilio= st.text_input(label= "Ingrese Domicilio ", max_chars = 45, placeholder=" Domicilio",value=datos_clientes.get("DOMICILIO") if datos_clientes else"")
            
        with _col_ciudad: 
            txt_ciudad= st.text_input(label= "Ingrese Ciudad del cliente", max_chars = 45, placeholder= "Ciudad",value=datos_clientes.get("CIUDAD") if datos_clientes else"")
formulario_ingresar_datos()