# Importamos librerías
import pandas as pd
import plotly.express as px
import streamlit as st

# Leemos el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Creamos un encabezado para la aplicación
st.header("Gráfico de Dispersión de Precio vs. Odómetro")

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

# Despleagamos el histograma si la casilla está seleccionada
if build_histogram:
    st.write(
        "Construir un histograma para la columna odómetro")

    fig = px.histogram(car_data, x='odometer')

    st.plotly_chart(fig, use_container_width=True)

# Crear una casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:  # si la casilla de verificación está seleccionada
    st.write(
        "Construir un gráfico de dispersión para las columnas odómetro y precio")
# Construimos el gráfico de dispersión
    fig = px.scatter(car_data, x='odometer', y='price')

    st.plotly_chart(fig, use_container_width=True)
