import streamlit as st

st.sidebar.title("Módulo")

st.sidebar.image("IMAGEN DMC.png", width=100)

modulos = st.sidebar.selectbox(
    "Seleccione un módulo:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])

if modulos == "Home":

    st.markdown("<h1 align='center'>APLICACIÓN EN STREAMLIT</h1>", unsafe_allow_html=True)

    st.image("foto de python.jpg")
    st.write("**Docente**: Carlos Carrillo Villavicencio")

    st.subheader("Nombre completo del estudiante")
    st.markdown("Farid Estefano Garibay Fabian")

    st.subheader("Nombre del módulo")
    st.markdown("Python Fundamentals")

    st.subheader("Información general del estudiante")
    st.markdown("Soy contador y busco especializarme en análisis de datos para combinar mi experiencia financiera con nuevas herramientas tecnológicas y así potenciar mi perfil profesional.")

    st.subheader("Año")
    st.markdown("2026")

    st.subheader("Breve descripción del proyecto")
    st.markdown("El proyecto facilita la aplicación práctica de lo aprendido en clase, consolidando los contenidos del primer módulo de Python Fundamentals.")

    st.subheader("Tecnologías utilizadas")
    st.markdown("Python, Streamlit y GitHub.")

elif modulos == "Ejercicio 1":

    st.title("Ejercicio 1")
    st.markdown("Bienvenido al **Ejercicio 1**")

elif modulos == "Ejercicio 2":

    st.title("Ejercicio 2")
    st.markdown("Bienvenido al **Ejercicio 2**")

elif modulos == "Ejercicio 3":

    st.title("Ejercicio 3")
    st.markdown("Bienvenido al **Ejercicio 3**")

elif modulos == "Ejercicio 4":

    st.title("Ejercicio 4")
    st.markdown("Bienvenido al **Ejercicio 4**")
