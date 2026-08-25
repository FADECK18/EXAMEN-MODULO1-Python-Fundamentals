import streamlit as st
import numpy as np

st.title("Proyecto Python for Analytics")
st.sidebar.title("Modulo")
st.write("Elaborado por: Farid Estefano Garibay Fabian")

st.image("foto de python.jpg", width = 450)
st.sidebar.image("IMAGEN DMC.png", width = 100)

modulos = st.sidebar.selectbox ("Selecione un módulo", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
if modulos == "Home":
  st.write("Bienvenido al módulo Home")

elif modulos == "Ejercicio 1":
  st.write("Bienvenido al Ejercicio 1")

elif modulos == "Ejercicio 2":
  st.write("Bienvenido al Ejercicio 2")

elif modulos == "Ejercicio 3":
  st.write("Bienvenido al Ejercicio 3")
  
else:
  st.write("Bienvenido al Ejercicio 4")
