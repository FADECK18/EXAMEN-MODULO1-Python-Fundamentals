import streamlit as st
import numpy as np

st.title("Proyecto Python for Analytics")
st.sidebar.title("Módulo")
st.write("Elaborado por: Farid Estefano Garibay Fabian")

st.sidebar.image("IMAGEN DMC.png", width = 100)

modulos = st.sidebar.selectbox ("Selecione un módulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
if modulos == "Home":
  st.write("Bienvenido al módulo Home")

st.image("foto de python.jpg", width = 450)
st.title("PROYECTO 1 - APLICACIÓN EN STREAMLIT")

st.write("Nombre completo del estudiante: Farid Estefano Garibay Fabian")
st.write("Nombre del módulo: Python Fundamentals")
st.write("Información general del estudiante: Soy contador y busco especializarme en análisis de datos para combinar mi experiencia financiera con nuevas herramientas tecnológicas y así potenciar mi perfil profesional")
st.write("Año : 2026")
st.write("Breve descripción del proyecto : El proyecto facilita la aplicación práctica de lo aprendido en clase, consolidando los contenidos del primer módulo de Python Fundamentals")




elif modulos == "Ejercicio 1":
  st.write("Bienvenido al Ejercicio 1")

elif modulos == "Ejercicio 2":
  st.write("Bienvenido al Ejercicio 2")

elif modulos == "Ejercicio 3":
  st.write("Bienvenido al Ejercicio 3")
  
else:
  st.write("Bienvenido al Ejercicio 4")
