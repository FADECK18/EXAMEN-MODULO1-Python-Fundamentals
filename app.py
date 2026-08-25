import streamlit as st
import numpy as np

st.title("Proyecto Python for Analytics")
st.sidebar.title("Parametros")
st.write("Elaborado por: Farid Estefano Garibay Fabian")

st.image("foto de python.jpg", width = 450)
st.sidebar.image("IMAGEN DMC.png", width = 100)

NOMBRE_ESTUDIANTE = "Farid Estefano Garibay Fabian"
MODULO = "Python for Analytics"
AÑO = "2026"

modulos = st.sidebar.selectbox ("Selecione un módulo", ["Módulo Listas", "Módulo Arreglos", "Módulo Funciones"])
if modulos == "Módulo Listas":
  st.write("Bienvenido al módulo Listas")

elif modulos == "Módulo Arreglos":
  st.write("Bienvenido al módulo de Arreglos")

else:
  st.write("Bienvenido al módulo de Funciones")
