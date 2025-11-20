import streamlit as st
import pandas as pd
import time
from consultas.consulta_materiales import ingresar_materiales, obtener_materiales
from consultas.consultas_proveedor import obtener_proveedores

st.title("Gestión de Materiales")

def formulario_ingresar_materiales():
    _contenedor_formulario = st.container(border=True)

    # 1️⃣ Traer proveedores y armar DataFrame
    resultado_proveedores = obtener_proveedores()
    df_proveedores = pd.DataFrame(resultado_proveedores, columns=["ID","Nombre","Rubro","Telefono"])

    with _contenedor_formulario:
        col_desc, col_precio, col_proveedor = st.columns(3)

        with col_desc:
            txt_descripcion = st.text_input("Ingrese Descripción", max_chars=45)

        with col_precio:
            precio = st.number_input("Ingrese Precio", min_value=0.0, format="%.2f")

        with col_proveedor:
            # 2️⃣ Selectbox solo con nombres
            proveedor_seleccionado = st.selectbox(
                "Seleccionar proveedor",
                options=df_proveedores["Nombre"].tolist(),
                placeholder="Elegir proveedor"
            )

        col_relleno, col_boton = st.columns([4,2])
        with col_boton:
            if st.button("Guardar material", use_container_width=True, icon=":material/save_as:"):
                if not txt_descripcion or not precio or not proveedor_seleccionado:
                    st.error("Todos los campos son obligatorios")
                    st.stop()

                try:
                    # 3️⃣ Obtener el ID del proveedor elegido
                    id_proveedor = df_proveedores.loc[
                        df_proveedores["Nombre"] == proveedor_seleccionado, "ID"
                    ].iloc[0]

                    # 4️⃣ Guardar material con clave foránea
                    ingresar_materiales(txt_descripcion, precio, id_proveedor)
                    st.success("Material ingresado correctamente.")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Ocurrió un error: {e}")

def main_usuario():
    formulario_ingresar_materiales()
    # Podés mostrar la lista de materiales si querés
    materiales = obtener_materiales()
    st.write("Lista de materiales registrados:")
    st.dataframe(pd.DataFrame(materiales, columns=["ID", "Descripcion", "Precio", "ID_Proveedor", "Proveedor","rubro"]))
main_usuario()
