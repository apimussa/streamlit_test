import streamlit as st
import pandas as pd
import plotly.express as px

st.header('📊 Mi dashboard')
car_data = pd.read_csv('vehicles_us.csv') # leer los datos


build_histogram = st.checkbox('Construir un histograma') # crear una casilla de verificación
hist_button = st.button('Construir histograma') # crear un botón

if build_histogram: # si la casilla de verificación está seleccionada
  # escribir un mensaje
  st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches con casilla')
  # crear un histograma
  fig = px.histogram(car_data, x="odometer")
  # mostrar un gráfico Plotly interactivo
  st.plotly_chart(fig, use_container_width=True)

if hist_button: # al hacer clic en el botón
  # escribir un mensaje
  st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches con botón')
  # crear un histograma
  fig = px.histogram(car_data, x="odometer")
  # mostrar un gráfico Plotly interactivo
  st.plotly_chart(fig, use_container_width=True)


build_scatter = st.checkbox('Construir un gráfico de dispersión') # crear una casilla de verificación
disp_button = st.button('Construir gráfico de dispersión')

if build_scatter: # si la casilla de verificación está seleccionada
  # escribir un mensaje
  st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches con casilla')
  # crear un histograma
  fig = px.scatter(car_data, x="odometer")
  # mostrar un gráfico Plotly interactivo
  st.plotly_chart(fig, use_container_width=True)

if disp_button: # al hacer clic en el botón
   # escribir un mensaje
  st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches con botón')
  # crear un histograma
  fig = px.scatter(car_data, x="odometer")
  # mostrar un gráfico Plotly interactivo
  st.plotly_chart(fig, use_container_width=True)
