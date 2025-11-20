def visualizar_datos(resultado):
    with st.expander("Mostrar detalles"):
        
        st.subheader("👥 Proveedores Registrados ")
        resultado=pd.DataFrame(resultado)
        dic_proveedores_seleccionado= st.dataframe( resultado,
                                                height=250,
                                                selection_mode='single-row',
                                                on_select='rerun',
                                                hide_index=True)
        indice=dic_proveedores_seleccionado ["selection"]["rows"][0] if  dic_proveedores_seleccionado["selection"]["rows"] else None
        
        serie_seleccionada= resultado.loc[indice] if indice!= None else None
            
        _col_relleno,_col_edicion,_col_eliminacion= st.columns([6,2,2])
        desactivado= False if serie_seleccionada is not None else True
        
        with _col_edicion:
            btn_edicion= st.button("Editar", use_container_width=True,icon="✏️",disabled=desactivado)
            if btn_edicion:
                actualizado= editar_proveedor(serie_seleccionada)
                if actualizado:
                    st.rerun()
                    
        with _col_eliminacion:
            btn_eliminar = st.button("Eliminar", use_container_width=True, icon="🚮",disabled=desactivado)
            if btn_eliminar:
                try:
                    id_proveedor= int(serie_seleccionada["ID"])
                    eliminar_datos(id_proveedor)
                    st.toast("Proveeedor iliminado correctamente.")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Error al eliminar la ubicación: {e}")
                    
                    
-------------------------------------------------------------


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

