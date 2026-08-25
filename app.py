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

    st.title("Ejercicio 1 - Flujo de caja con listas")

    st.markdown(
        """
        En este ejercicio se registrarán movimientos financieros utilizando una lista.
        Cada movimiento tendrá un concepto, un tipo de movimiento y un valor.
        El sistema calculará el total de ingresos, el total de gastos y el saldo final
        del flujo de caja.
        """
    )

    # Crear la lista de movimientos
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Ingreso de datos
    concepto = st.text_input("Ingrese el concepto:")

    tipo = st.selectbox(
        "Seleccione el tipo de movimiento:",
        ["Ingreso", "Gasto"]
    )

    valor = st.number_input(
        "Ingrese el valor:",
        min_value=0.0,
        step=0.01
    )

    # Botón para agregar movimiento
    if st.button("Agregar movimiento"):

        if concepto == "":
            st.error("Ingrese un concepto para registrar el movimiento.")

        elif valor == 0:
            st.error("Ingrese un valor mayor a 0.")

        else:
            movimiento = {
                "Concepto": concepto,
                "Tipo": tipo,
                "Valor": valor
            }

            st.session_state.movimientos.append(movimiento)

            st.success("Movimiento agregado correctamente.")

    # Mostrar movimientos registrados
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

        # Calcular saldo
        saldo_final = total_ingresos - total_gastos

        # Mostrar resultados
        st.subheader("Resultado del flujo de caja")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total de ingresos", f"S/ {total_ingresos:.2f}")

        with col2:
            st.metric("Total de gastos", f"S/ {total_gastos:.2f}")

        with col3:
            st.metric("Saldo final", f"S/ {saldo_final:.2f}")

        # Estado del flujo de caja
        if saldo_final >= 0:
            st.success("El flujo de caja está a favor.")
        else:
            st.error("El flujo de caja está en contra.")

    else:
        st.markdown("Todavía no hay movimientos registrados.")



elif modulos == "Ejercicio 2":

    st.title("Ejercicio 2")
    st.markdown("Bienvenido al **Ejercicio 2**")

elif modulos == "Ejercicio 3":

    st.title("Ejercicio 3")
    st.markdown("Bienvenido al **Ejercicio 3**")

elif modulos == "Ejercicio 4":

    st.title("Ejercicio 4")
    st.markdown("Bienvenido al **Ejercicio 4**")
