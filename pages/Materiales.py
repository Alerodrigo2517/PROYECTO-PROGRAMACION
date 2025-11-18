import streamlit as st
import pandas as pd
from datetime import date
import time
from consultas.consulta_materiales import obtener_materiales,ingresar_materiales,actualizar_material,eliminar_materiales

st.title("Gestión de Materiales")

def formulario_ingresar_materiales():
    _contenedor_formulario=st.container(border=True)
    with _contenedor_formulario:
        _col_descripcion,_col_precio,_col_fk_proveedor= st.columns(3)
        
        with _col_descripcion:
            txt_descripcion=st.text_input(label="Ingrese Descripcion",max_chars=45)
        
        with _col_precio:
            precio=st.number_input(label="Ingrese Precio", min_value=0.0, format="%.2f")
        
        with _col_fk_proveedor:
            id=st.number_input(label="id proveedor")
            
        _col_relleno,col_boton=st.columns([4,2])

        with col_boton:
            btn_guardar_cliente= st.button("Guardar cliente",use_container_width=True, icon=':material/save_as:')
def main_usuario():
    resultado_usuario=obtener_materiales()
    
formulario_ingresar_materiales() 
main_usuario()