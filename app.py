import streamlit as st

st.title("PROYECTO 1 - APLICACIÓN EN STREAMLIT")
st.sidebar.title("Módulo")

st.write("Elaborado por: Farid Estefano Garibay Fabian")

st.sidebar.image("IMAGEN DMC.png", width=100)

modulos = st.sidebar.selectbox(
    "Seleccione un módulo:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

if modulos == "Home":

    st.title("PROYECTO 1 - APLICACIÓN EN STREAMLIT")

    st.image("foto de python.jpg", width=450)

    st.write("### Nombre completo del estudiante")
    st.write("Farid Estefano Garibay Fabian")

    st.write("### Nombre del módulo")
    st.write("Python Fundamentals")

    st.write("### Información general del estudiante")
    st.write(
        "Soy contador y busco especializarme en análisis de datos "
        "para combinar mi experiencia financiera con nuevas herramientas "
        "tecnológicas y así potenciar mi perfil profesional."
    )

    st.write("### Año")
    st.write("2026")

    st.write("### Breve descripción del proyecto")
    st.write(
        "El proyecto facilita la aplicación práctica de lo aprendido "
        "en clase, consolidando los contenidos del primer módulo de "
        "Python Fundamentals."
    )

    st.write("### Tecnologías utilizadas")
    st.write(
        "Python, Streamlit y GitHub."
    )

elif modulos == "Ejercicio 1":

    st.title("Ejercicio 1")
    st.write("Bienvenido al Ejercicio 1")

elif modulos == "Ejercicio 2":

    st.title("Ejercicio 2")
    st.write("Bienvenido al Ejercicio 2")

elif modulos == "Ejercicio 3":

    st.title("Ejercicio 3")
    st.write("Bienvenido al Ejercicio 3")

elif modulos == "Ejercicio 4":

    st.title("Ejercicio 4")
    st.write("Bienvenido al Ejercicio 4")
