# Importamos librerías
import pandas as pd
import plotly.express as px
import streamlit as st

# Leemos el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Creamos un encabezado para la aplicación
st.header("Gráfico de Dispersión de Precio vs. Odómetro")

# Creamos un botón que construye un gráfico histograma al ser presionado.
hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        "Creación de un histograma para el conjunto de datos de de anuncios de venta de carros")

    fig = px.histogram(car_data, x='Odometer')

    st.plotly_chart(fig, use_container_width=True)
