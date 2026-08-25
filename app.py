import streamlit as st
import pandas as pd

from libreria_funciones_proyecto1 import calcular_cuota_prestamo_frances
from libreria_clases_proyecto1 import Empleado

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

    st.title("Ejercicio 1 - Flujo de caja con listas")

    st.markdown("""En este ejercicio se registrarán movimientos financieros utilizando una lista. Cada movimiento tendrá un concepto, un tipo de movimiento y un valor. El sistema calculará el total de ingresos, el total de gastos y el saldo final del flujo de caja.""")

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    concepto = st.text_input("Ingrese el concepto:")

    tipo = st.selectbox("Seleccione el tipo de movimiento:",["Ingreso", "Gasto"])

    valor = st.number_input("Ingrese el valor:",min_value=0.0,step=0.01)

    if st.button("Agregar movimiento"):

        if concepto == "":
            st.error("Ingrese un concepto para registrar el movimiento.")

        elif valor == 0:
            st.error("Ingrese un valor mayor a 0.")

        else:
            movimiento = {"Concepto": concepto,"Tipo": tipo,"Valor": valor}

            st.session_state.movimientos.append(movimiento)

            st.success("Movimiento agregado correctamente.")

    st.subheader("Movimientos registrados")

    if len(st.session_state.movimientos) > 0:

        st.dataframe(st.session_state.movimientos)

        # Calcular ingresos y gastos
        total_ingresos = 0
        total_gastos = 0

        for movimiento in st.session_state.movimientos:

            if movimiento["Tipo"] == "Ingreso":
                total_ingresos += movimiento["Valor"]

            else:
                total_gastos += movimiento["Valor"]

        saldo_final = total_ingresos - total_gastos

        st.subheader("Resultado del flujo de caja")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total de ingresos", f"S/ {total_ingresos:.2f}")

        with col2:
            st.metric("Total de gastos", f"S/ {total_gastos:.2f}")

        with col3:
            st.metric("Saldo final", f"S/ {saldo_final:.2f}")

        if saldo_final >= 0:
            st.success("El flujo de caja está a favor.")
        else:
            st.error("El flujo de caja está en contra.")

    else:
        st.markdown("Todavía no hay movimientos registrados.")

elif modulos == "Ejercicio 2":

    st.title("Ejercicio 2 - Registro con NumPy, Arrays y DataFrame")

    st.markdown("""En este ejercicio se registrarán productos utilizando arreglos de NumPy. Cada registro contiene el nombre del producto, categoría, precio, cantidad y total. Los datos registrados serán convertidos en un DataFrame para mostrar la información actualizada en pantalla.""")

    if "productos" not in st.session_state:
        st.session_state.productos = np.array([])
        st.session_state.categorias = np.array([])
        st.session_state.precios = np.array([])
        st.session_state.cantidades = np.array([])
        st.session_state.totales = np.array([])

    nombre = st.text_input("Nombre del producto:")

    categoria = st.selectbox("Seleccione la categoría:",["Alimentos", "Bebidas", "Limpieza", "Tecnología", "Otros"])

    precio = st.number_input("Precio del producto:", min_value=0.0, step=0.01)

    cantidad = st.number_input("Cantidad:", min_value=1, step=1)

    total = precio * cantidad

    st.markdown(f"**Total del registro: S/ {total:.2f}**")

    if st.button("Agregar registro"):

        if nombre == "":
            st.error("Ingrese el nombre del producto.")

        elif precio == 0:
            st.error("Ingrese un precio mayor a 0.")

        else:

            st.session_state.productos = np.append(st.session_state.productos,nombre)

            st.session_state.categorias = np.append(st.session_state.categorias,categoria)

            st.session_state.precios = np.append(st.session_state.precios,precio)

            st.session_state.cantidades = np.append(st.session_state.cantidades,cantidad)

            st.session_state.totales = np.append(st.session_state.totales,total)

            st.success("Registro agregado correctamente.")

    datos = {"Producto": st.session_state.productos,"Categoría": st.session_state.categorias,"Precio": st.session_state.precios,"Cantidad": st.session_state.cantidades,"Total": st.session_state.totales}

    df = pd.DataFrame(datos)

    st.subheader("Registros de productos")

    st.dataframe(df)

elif modulos == "Ejercicio 3":

    st.title("Ejercicio 3 - Cálculo de préstamo")

    st.markdown("""En este ejercicio se utilizará una función de una librería externa para calcular la cuota mensual de un préstamo bajo el sistema francés. El usuario podrá ingresar el monto, la tasa anual y el plazo del préstamo. Los resultados obtenidos se almacenarán en un histórico.""")

    funcion = st.selectbox("Seleccione una función:",["Calcular cuota de préstamo francés"])

    monto = st.number_input("Ingrese el monto del préstamo:", min_value=1.0, step=100.0)

    tasa_anual = st.number_input("Ingrese la tasa anual (%):", min_value=0.0, step=0.1)

    plazo_meses = st.number_input("Ingrese el plazo en meses:", min_value=1, step=1)

    if "historico_prestamos" not in st.session_state:
        st.session_state.historico_prestamos = []

    if st.button("Calcular préstamo"):

        resultado = calcular_cuota_prestamo_frances(monto, tasa_anual, plazo_meses)

        st.subheader("Resultado del préstamo")

        st.write(f"Cuota mensual: S/ {resultado['cuota_mensual']:.2f}")

        st.write(f"Total pagado: S/ {resultado['total_pagado']:.2f}")

        st.write(f"Interés total: S/ {resultado['interes_total']:.2f}")

        registro = {"Monto": monto, "Tasa anual (%)": tasa_anual, "Plazo (meses)": plazo_meses, "Cuota mensual": resultado["cuota_mensual"], "Total pagado": resultado["total_pagado"], "Interés total": resultado["interes_total"]}

        st.session_state.historico_prestamos.append(registro)

        st.success("Cálculo realizado correctamente.")

    df_historico = pd.DataFrame(st.session_state.historico_prestamos)

    st.subheader("Histórico de resultados")

    st.dataframe(df_historico)

elif modulos == "Ejercicio 4":

    st.title("Ejercicio 4 - Registro de empleados con CRUD")

    st.markdown("""
    En este ejercicio se utilizará la clase Empleado desde una
    librería externa para registrar empleados y calcular su bono,
    descuento y salario neto. Se implementarán las operaciones
    CRUD: Crear, Leer, Actualizar y Eliminar.
    """)

    # Crear lista de empleados
    if "empleados" not in st.session_state:
        st.session_state.empleados = []


    # =====================================================
    # CREAR
    # =====================================================

    st.subheader("Crear empleado")

    nombre = st.text_input(
        "Nombre del empleado:"
    )

    salario = st.number_input(
        "Salario base:",
        min_value=0.01,
        step=100.0
    )

    bono = st.number_input(
        "Porcentaje de bono (%):",
        min_value=0.0,
        max_value=100.0,
        step=1.0
    )

    descuento = st.number_input(
        "Porcentaje de descuento (%):",
        min_value=0.0,
        max_value=100.0,
        step=1.0
    )


    if st.button("Agregar empleado"):

        if nombre == "":
            st.error("Ingrese el nombre del empleado.")

        else:

            empleado = Empleado(
                nombre,
                salario,
                bono,
                descuento
            )

            st.session_state.empleados.append(
                empleado
            )

            st.success(
                "Empleado agregado correctamente."
            )


    # =====================================================
    # LEER
    # =====================================================

    st.subheader("Empleados registrados")

    datos = []

    for empleado in st.session_state.empleados:

        datos.append(
            empleado.resumen()
        )

    df = pd.DataFrame(datos)

    st.dataframe(df)


    # =====================================================
    # ACTUALIZAR
    # =====================================================

    st.subheader("Actualizar empleado")

    if len(st.session_state.empleados) > 0:

        nombres = []

        for empleado in st.session_state.empleados:

            nombres.append(
                empleado.nombre
            )

        empleado_seleccionado = st.selectbox(
            "Seleccione el empleado:",
            nombres
        )

        nuevo_salario = st.number_input(
            "Nuevo salario base:",
            min_value=0.01,
            step=100.0
        )

        nuevo_bono = st.number_input(
            "Nuevo porcentaje de bono (%):",
            min_value=0.0,
            max_value=100.0,
            step=1.0
        )

        nuevo_descuento = st.number_input(
            "Nuevo porcentaje de descuento (%):",
            min_value=0.0,
            max_value=100.0,
            step=1.0
        )

        if st.button("Actualizar empleado"):

            for empleado in st.session_state.empleados:

                if empleado.nombre == empleado_seleccionado:

                    empleado.salario_base = nuevo_salario

                    empleado.porcentaje_bono = nuevo_bono

                    empleado.porcentaje_descuento = nuevo_descuento

                    st.success(
                        "Empleado actualizado correctamente."
                    )


    # =====================================================
    # ELIMINAR
    # =====================================================

    st.subheader("Eliminar empleado")

    if len(st.session_state.empleados) > 0:

        empleado_eliminar = st.selectbox(
            "Seleccione el empleado a eliminar:",
            nombres,
            key="empleado_eliminar"
        )

        if st.button("Eliminar empleado"):

            for empleado in st.session_state.empleados:

                if empleado.nombre == empleado_eliminar:

                    st.session_state.empleados.remove(
                        empleado
                    )

                    st.success(
                        "Empleado eliminado correctamente."
                    )

