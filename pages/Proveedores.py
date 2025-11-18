import streamlit as st
import pandas as pd
from datetime import date
import time
from consultas.consultas_proveedor import obtener_proveedores,ingresar_proveedor,actualizar_proveedores,verificar_nombre_proveedor,verificar_telefono_proveedor,eliminar_proveedores

st.title("Gestión de Proveedores")

@st.dialog ("Modificar Proveedor")
def editar_proveedor(serie_seleccionada):
    
        col_nombre, _col_rubro,col_telefono= st.columns(3)
        
        with col_nombre:
            txt_nombre=st.text_input(label=" Nombre del proveedor ",max_chars=45,value=serie_seleccionada["Nombre"],disabled=True)
        
        with _col_rubro:
            txt_rubro=st.text_input(label=" Rubro del proveedor ",max_chars=45,value=serie_seleccionada["Rubro"])
            
        with col_telefono:
            txt_telefono= st.text_input(label=" Telefono", max_chars=12,value=serie_seleccionada["Telefono"])
        
        col_relleno, _col_boton = st.columns([4,2]) 
        with _col_boton:
            btn_guardar_usuario_editado = st.button('Guardar',use_container_width=True,icon=':material/save_as:',type="primary")
            
        if btn_guardar_usuario_editado:
            try:
                actualizar_proveedores(serie_seleccionada["ID"], txt_nombre, txt_rubro, txt_telefono)
                st.success("Usuario modificado correctamente.")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f" Error al guardar los cambios: {e}")


def mostrar_proveedores(df_proveedores):
    st.subheader("Lista de Proveedores")
    df_proveedores = pd.DataFrame(df_proveedores)

    if df_proveedores.empty:
        st.info("ℹ️ No hay proveedores registrados aún.")
        return

    for indice, proveedor in df_proveedores.iterrows():
        with st.container(border=True):
            col_info, col_editar, col_eliminar = st.columns([3,2,2])
            
            with col_info:
                st.markdown(f"### {proveedor['Nombre']}")
                st.markdown(f"Rubro: {proveedor['Rubro']}")
                st.markdown(f" Teléfono: {proveedor['Telefono']}")

            with col_editar:
                if st.button("✏️ Actualizar datos", key=f"edit_{proveedor['ID']}", use_container_width=True, type="primary"):
                    editar_proveedor(proveedor)

            with col_eliminar:
                if st.button("🚮 Quitar proveedor", key=f"del_{proveedor['ID']}", use_container_width=True):
                    try:
                        eliminar_proveedores(int(proveedor["ID"]))
                        st.toast("✅ Proveedor eliminado con éxito")
                        time.sleep(2)
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ No se pudo eliminar el proveedor: {e}")
        st.divider()


def formulario_proveedores():
    _contenedor_formulario=st.container(border=True)
    
    RUBROS=["Metalurgica/ferreteria","Ferreteria","Pintureria","Carpinteria","corralon"]
    
    with _contenedor_formulario:
        col_nombre, _col_rubro,col_telefono= st.columns(3)
        
        with col_nombre:
            txt_nombre=st.text_input(label="ingrese el Nombre del proveedor ",max_chars=45)
        
        with _col_rubro:
            txt_rubro= st.selectbox("Selecciona Rubro del Proveedor",options=RUBROS,index=None,placeholder="Elegir rubro")
            
        with col_telefono:
            txt_telefono= st.text_input(label="ingrese Telefono", max_chars=12)
        
    _col_relleno, _col_boton = st.columns([4,2]) 

    with _col_boton:
        
        if st.button('Guardar Proveedor', use_container_width=True, icon=':material/save_as:',type="primary"):
                if not txt_nombre or not txt_rubro:
                    st.error('El Nombre del proveedor o el rubro no fueron ingresados :(')
                    st.stop()
                
                if not txt_telefono:
                    st.error('El Telefono no fue ingresado :(')
                    st.stop()
                try:
                    if verificar_nombre_proveedor(txt_nombre):
                        st.error("El nombre del proveedor ya existe")
                        time.sleep(2)
                        st.rerun()
                        
                    if verificar_telefono_proveedor(txt_telefono):
                        st.error("El telefono proveedor ya existe")
                        time.sleep(2)
                        st.rerun ()
                    
                    ingresar_proveedor(txt_nombre,txt_rubro,txt_telefono)
                    st.success("Proveedor ingresado correctamente.")
                    time.sleep(2)
                    st.rerun ()
                except Exception as e:
                    st.error(f"ocurrio un error de conexion:{e}")
                    

    
    
def main_usuario():
    formulario_proveedores()
    resultado_proveedores= obtener_proveedores()
    mostrar_proveedores(resultado_proveedores)
    
main_usuario()
    
