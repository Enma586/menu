import streamlit as st

st.set_page_config(
    page_title="Dashboard Central",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inyectamos estilos CSS para el texto fijo en la esquina inferior derecha
st.markdown(
    """
    <style>
    .bottom-right {
        position: fixed;
        bottom: 10px;
        right: 10px;
        font-size: 12px;
        color: #888;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar con navegación
st.sidebar.image("logo.png", use_container_width=True)
st.sidebar.title("Menú")
opcion = st.sidebar.radio("Ir a:", [
    "Inicio",
    "Ligas de Fútbol",
    "Películas",
    "Clima en El Salvador"
])

if opcion == "Inicio":
    st.title("🌐 Bienvenido al Dashboard Central")

    # Centramos el bloque de texto en 3 columnas
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        Este sitio te permite acceder rápidamente a tres aplicaciones útiles:

        - **Ligas de Fútbol**: consulta las tablas actualizadas de tus ligas favoritas.  
        - **Películas**: busca información sobre películas por título o palabra clave.  
        - **Clima en El Salvador**: revisa el estado del tiempo en tiempo real.

        Selecciona una opción en el menú lateral para comenzar.
        """)

    # Nombres fijos en la esquina inferior derecha
    st.markdown(
        """
        <div class="bottom-right">
          CARLOS ENMANUEL FLORES MENDEZ<br>
          SAUL EDENILSON PULUNTO ARGUETA
        </div>
        """,
        unsafe_allow_html=True
    )

elif opcion == "Ligas de Fútbol":
    st.title("📊 Tabla de Ligas de Fútbol")
    st.image("ligas_header.png", use_container_width=True)
    st.markdown(
        "[Ir a la aplicación de Ligas](https://api-ligas-3hvon3xntzepkzyjxyrb6m.streamlit.app/)",
        unsafe_allow_html=True
    )

elif opcion == "Películas":
    st.title("🎬 Consulta de Películas")
    st.image("peliculas_header.png", use_container_width=True)
    st.markdown(
        "[Ir a la aplicación de Películas](https://apicine-hfml7sdd8kjxfapyzank9q.streamlit.app/)",
        unsafe_allow_html=True
    )

elif opcion == "Clima en El Salvador":
    st.title("☀️ Estado del Clima")
    st.image("clima_header.png", use_container_width=True)
    st.markdown(
        "[Ir a la aplicación del Clima](https://situacion-clima-myiwpxawitskeylxtxegez.streamlit.app/)",
        unsafe_allow_html=True
    )
