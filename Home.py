import streamlit as st
# <- importante: hace la app de ancho completo

import streamlit as st



col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("statics/logo_herreria.png", width=200)

# CSS y HTML en un único contenedor
st.markdown("""
<style>
.card-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2em;
    margin-top: 2em;
    width: 100%;
    box-sizing: border-box;
    padding: 0 2rem;
}
.card {
    background-color: #1e1e1e;
    border-radius: 12px;
    padding: 1.2em;
    width: 280px;
    max-width: 30%;
    box-shadow: 2px 2px 12px rgba(0,0,0,0.3);
    text-align: center;
    color: white;
    cursor: pointer;

    display: block !important;     /* <- IMPORTANTE */
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}

.card:hover {
    transform: translateY(-8px) scale(1.03) !important;
    box-shadow: 4px 4px 20px rgba(0,0,0,0.5) !important;
}

@media (max-width: 900px) {
    .card { max-width: 45%; width: 45%; }   /* responsive */
}
@media (max-width: 600px) {
    .card { max-width: 100%; width: 100%; } /* phones: apilan */
}
.card-icon { font-size: 2.5em; margin-bottom: 0.5em; color: #a29bfe; }
.card-title { font-size: 1.2em; font-weight: bold; margin-bottom: 0.5em; }
.card-desc { font-size: 0.95em; color: #ccc; margin-bottom: 1em; }
a.card-link { color: inherit; text-decoration: none; display:block; margin-top:0.5em; }
a.card-link:hover { text-decoration: underline; }
</style>

<div class="card-grid">
  <div class="card">
    <div class="card-icon">👥</div>
    <div class="card-title">Clientes</div>
    <div class="card-desc">Registrá, editá y consultá los datos de tus clientes.</div>
    <a class="card-link" href="pages/_Cliente.py">Ir</a>
  </div>

# Botón Streamlit para navegar
if st.button("Ir a Clientes", key="btn_clientes"):
    st.switch_page("pages/Clientes.py")
  <div class="card">
    <div class="card-icon">🛠️</div>
    <div class="card-title">Proveedores</div>
    <div class="card-desc">Gestioná la información de tus proveedores.</div>
    <a class="card-link" href="pages/Proveedores.py">Ir</a>
  </div>

  <div class="card">
    <div class="card-icon">📊</div>
    <div class="card-title">Presupuestos</div>
    <div class="card-desc">Creá y administrá presupuestos asociados a tus clientes.</div>
    <a class="card-link" href="pages/Presupuestos.py">Ir</a>
  </div>
</div>
""", unsafe_allow_html=True)
