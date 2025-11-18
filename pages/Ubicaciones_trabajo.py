import streamlit as st
import pandas as pd
import time

from consultas.consultas_cliente import obtener_datos  # para traer cliente
from consultas.consulta_ubicacion_trabajo import obtener_datos_ubicacion_trabajo,ingresar_datos_ubicacion,actualizar_datos,eliminar_datos,verificar_domicilio_existente
@st.dialog("Modificar Ubicacion")
def editar_ubicacion(serie_seleccionada):
    
    _col_domicilio, _col_ciudad = st.columns(2)
    with _col_domicilio:
        txt_domicilio = st.text_input("Domicilio", value=serie_seleccionada["DOMICILIO"])
    with _col_ciudad:
        txt_ciudad = st.text_input("Ciudad", value=serie_seleccionada["CIUDAD"])

    
    _col_relleno, _col_boton, _col_eliminacion = st.columns([4, 2, 0.6])
    
    with _col_boton:
            btn_guardar_usuario_editado = st.button('Guardar',use_container_width=True,icon=':material/save_as:')
            if btn_guardar_usuario_editado:
                try:
                    id_ubicacion = int(serie_seleccionada["ID"])
                    actualizar_datos(id_ubicacion, txt_domicilio, txt_ciudad)
                    st.success("Ubicación modificada correctamente.")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Error al guardar los cambios: {e}")
            
def formulario_ingresar_datos():
    _contenedor_formulario = st.container(border=True)
    with _contenedor_formulario:
        st.subheader("📍 Registrar ubicación de trabajo")

        clientes = obtener_datos()

        df_clientes = pd.DataFrame(clientes)
        
        if df_clientes.empty:
            st.error("⚠️ No hay clientes cargados en el sistema.")
            st.stop()
        cliente_seleccionado = None

        seleccion = st.selectbox("Seleccionar cliente", df_clientes["CUILT"])
        if seleccion:
            cliente_seleccionado = df_clientes[df_clientes["CUILT"] == seleccion].iloc[0]

        # ✅ Definí el checkbox después de seleccionar cliente
        usar_direccion_cliente = st.checkbox("Usar mismo domicilio que el cliente", value=True)

        if cliente_seleccionado is not None and usar_direccion_cliente:
            txt_domicilio = cliente_seleccionado["DOMICILIO"]
            txt_ciudad = cliente_seleccionado["CIUDAD"]
        else:
            _col_domicilio, _col_ciudad = st.columns(2)
            with _col_domicilio:
                txt_domicilio = st.text_input(label="Ingrese Domicilio", max_chars=45)
            with _col_ciudad:
                txt_ciudad = st.text_input("Ciudad")


        _col_relleno, _col_boton = st.columns([4, 2])
        with _col_boton:
            btn_guardar = st.button("Guardar ubicación", use_container_width=True, icon=":material/save_as:")

        if btn_guardar:
            if not txt_domicilio or not txt_ciudad:
                st.error("Debe completar domicilio y ciudad.")
            else:
                resultado=obtener_datos_ubicacion_trabajo()
                ubicaciones_existente=pd.DataFrame(resultado)
                
            if ubicaciones_existente.empty or "DOMICILIO" not in ubicaciones_existente.columns:
                ingresar_datos_ubicacion(txt_domicilio,txt_ciudad)
                st.success("ubicacion registrada correctamente")
                time.sleep(2)
                st.rerun()
            try:
                if  verificar_domicilio_existente(txt_domicilio,txt_ciudad):
                    st.error("El domicilio ya existe")
                    time.sleep(2)
                    st.rerun()
                ingresar_datos_ubicacion(txt_domicilio,txt_ciudad)
            except Exception as e:
                st.error(f"ocurrior un error de conexion {e}")
                

def visualizar_datos():
    resultado = obtener_datos_ubicacion_trabajo()
    resultado = pd.DataFrame(resultado)
    st.subheader("📍 Ubicaciones registradas")
    dic_ubicacion_seleccionada= st.dataframe  ( resultado,
                                                height=300,
                                                selection_mode="single-row",
                                                on_select="rerun",
                                                hide_index=True)
    indice=dic_ubicacion_seleccionada["selection"]  ["rows"][0] if dic_ubicacion_seleccionada["selection"] ["rows"] else None
    
    serie_seleccionada=resultado.loc[indice] if indice!= None else None
    _col_relleno,col_edicion,_col_eliminacion=st.columns ([6,3,3])
    desactivado= False if serie_seleccionada is not None else True
    
    with col_edicion:
        btn_edicion=st.button("Editar",use_container_width=True,icon="✏️",disabled=desactivado)
        if btn_edicion:
            editar_ubicacion(serie_seleccionada)
            
    with _col_eliminacion:
        btn_eliminar = st.button("Eliminar", use_container_width=True, icon="🚮",disabled=desactivado)
        if btn_eliminar:
            try:
                id_ubicacion = int(serie_seleccionada["ID"])
                eliminar_datos(id_ubicacion)
                st.toast("Ubicación eliminada correctamente.")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Error al eliminar la ubicación: {e}")

def main():
    formulario_ingresar_datos()
    visualizar_datos()

main()
