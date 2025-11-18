import streamlit as st
import pandas as pd
import re
import time

from consultas.consultas_cliente import  obtener_datos, ingresar_datos,actualizar_datos,tiene_presupuestos_asociados, eliminar_datos,verificar_cuilt_existente

@st.dialog("Modificar usuario")
def editar_usuario (serie_seleccionada):
    
    cuilt_original = serie_seleccionada.loc["CUILT"]
    
    _col_cuilt,_col_nombre,_col_apellido= st.columns(3)
    with _col_cuilt:
        txt_cuilt=st.text_input("Cuilt", value=serie_seleccionada.loc["CUILT"],disabled=True) 
    with _col_nombre:
        txt_nombre_cliente= st.text_input("Nombre",value=serie_seleccionada.loc["NOMBRE"])
    with _col_apellido:
        txt_apellido_cliente=st.text_input("Apellido",value=serie_seleccionada.loc["APELLIDO"]) 
        
    _col_domicilio,_col_cudad,_col_telefono=st.columns(3)
    
    with _col_domicilio:
        txt_domicilio=st.text_input("Domicilio",value=serie_seleccionada.loc["DOMICILIO"])
    with _col_cudad:
        txt_ciudad= st.text_input("Ciudad",value=serie_seleccionada.loc["CIUDAD"])
    with _col_telefono:
        txt_telefono=st.text_input("Telefono",value=serie_seleccionada.loc["TELEFONO"])
        
        
    _col_relleno, _col_boton = st.columns([4,2])
    
    
    

    with _col_boton:
        btn_guardar_usuario_editado = st.button('Guardar',use_container_width=True,icon=':material/save_as:')
    if btn_guardar_usuario_editado:
        try:
            actualizar_datos(
                cuilt_original,txt_cuilt,txt_nombre_cliente,txt_apellido_cliente,txt_domicilio,txt_ciudad,
txt_telefono
            )
            st.success("Usuario modificado correctamente.")
            time.sleep(2)
            st.rerun()
        except Exception as e:
            st.error(f" Error al guardar los cambios: {e}")
            
# 🔧 CAMBIO: función modal para confirmar eliminación
@st.dialog("Confirmar eliminación de cliente")
def confirmar_eliminacion_cliente(cuilt):
    st.warning("⚠️ Este cliente tiene presupuestos asociados. Al eliminarlo, también se eliminarán automáticamente.")
    confirmar = st.button("Eliminar definitivamente", use_container_width=True, type="primary")
    if confirmar:
        try:
            eliminar_datos(cuilt)
            st.success("Cliente y presupuestos eliminados correctamente.")
            time.sleep(2)
            st.rerun()
        except Exception as e:
            st.error(f"Error al eliminar el cliente: {e}")

        
st.title(" 📋Gestión de Presupuestos")
st.subheader("Datos personales del cliente")

st.text("A continuación complete todos los campos requeridos.")

def visualizar_datos(resultado):
    st.subheader("👥 Clientes registrados ")
    resultado=pd.DataFrame(resultado)
    dic_cliente_seleccionado= st.dataframe( resultado,
                                                height=250,
                                                selection_mode='single-row',
                                                on_select='rerun',
                                                hide_index=True)
    indice=dic_cliente_seleccionado ["selection"]["rows"][0] if  dic_cliente_seleccionado["selection"]["rows"] else None
        
    serie_seleccionada= resultado.loc[indice] if indice!= None else None
            
    col_relleno,_col_edicion,_col_eliminacion= st.columns([6,2,2])
    
    desactivado= False if serie_seleccionada is not None else True
    
    with _col_edicion:
                btn_edicion= st.button("Editar", use_container_width=True,icon="✏️",disabled=desactivado)
                if btn_edicion:
                    editar_usuario(serie_seleccionada)
                    
    # usar ventana emergente si hay presupuestos asociados
    with _col_eliminacion:
        btn_eliminar = st.button("Eliminar", use_container_width=True, icon="🚮", disabled=desactivado)
        if btn_eliminar and serie_seleccionada is not None:
            cuilt = serie_seleccionada.loc["CUILT"]
            if tiene_presupuestos_asociados(cuilt):
                confirmar_eliminacion_cliente(cuilt)  # abre modal
            else:
                try:
                    eliminar_datos(cuilt)
                    st.toast("Cliente eliminado correctamente.")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Error al eliminar el cliente: {e}")

    st.markdown(
        """
        <div>
            <hr style="border: none; height: 0.04em; background-color: #333; margin-top:-0.1em">
        </div>""", unsafe_allow_html=True
    )    
    
def formulario_ingresar_datos ():
    _contenedor_formulario = st.container(border=True)
    with _contenedor_formulario:
        
        _col_nombre, _col_apellido= st.columns(2)
        
        with _col_nombre:
            txt_nombre = st.text_input(label= "Ingrese nombre del Cliente  ", max_chars = 45, placeholder="Juan Carlos ")

        with _col_apellido:
            txt_apellido = st.text_input(label= "Ingrese el apellido del cliente ", max_chars = 45,  placeholder="Perez")


        col_cuilt, col_telefono, _col_domicilio,_col_ciudad = st.columns([2,2,2,2]) 
        with col_cuilt:
            txt_cuilt = st.text_input(label="Ingrese el CUILT ", max_chars=13 , placeholder="20-00000000-7")

        with col_telefono: 
            txt_telefono = st.text_input(label= "Ingrese Teléfono ", max_chars = 12,  placeholder=" Teléfono del cliente ")
        
        with _col_domicilio: 
            txt_domicilio= st.text_input(label= "Ingrese Domicilio ", max_chars = 45, placeholder=" Domicilio")
            
        with _col_ciudad: 
            txt_ciudad= st.text_input(label= "Ingrese Ciudad del cliente", max_chars = 45, placeholder= "Ciudad")
        


        _col_relleno, _col_boton = st.columns([4,2]) 

        with _col_boton:
            btn_guardar_cliente = st.button("Guardar Cliente", use_container_width=True, icon=":material/save_as:")

        if btn_guardar_cliente:
            if not txt_nombre or not txt_apellido:
                st.error("El nombre o el apellido no fueron ingresados")
                time.sleep(2)
                st.stop()
            
            if not txt_cuilt:
                st.error("El Cuilt no fue Ingresado")
                st.stop()
            if not txt_telefono:
                st.error("El Telefono no fue ingresado")
                st.stop()

            if  not txt_domicilio or not  txt_ciudad:
                st.error("El domicilio no fue ingresado ")
                st.stop()

            try:
                if verificar_cuilt_existente(txt_cuilt):
                    st.error("El Cuilt ya existe en la base de datos")
                    time.sleep(2)
                    st.rerun()
                nombre_norm   = txt_nombre.strip().title()     
                apellido_norm = txt_apellido.strip().title()   
                domicilio_norm= txt_domicilio.strip().capitalize()  
                ciudad_norm   = txt_ciudad.strip().capitalize()   
                ingresar_datos(txt_cuilt, nombre_norm, apellido_norm, domicilio_norm, ciudad_norm, txt_telefono)
            except Exception as e:
                st.error(f"Ocurrió un error de conexión: {e}")

            
def main_usuario():
    formulario_ingresar_datos()
    resultado_usuario= obtener_datos()
    visualizar_datos(resultado_usuario)
    
main_usuario()


