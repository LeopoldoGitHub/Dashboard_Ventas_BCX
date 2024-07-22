import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Dashboard G2')
st.sidebar.title('Filtros')

### Cargar datos
try:
    df_itens_pedidos = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_itens_pedidos.csv')
    df_pedidos = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_pedidos.csv')
    df_productos = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_productos.csv')
    df_vendedores = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_vendedores.csv')
    df_final = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_final.csv')
except Exception as e:
    st.error(f"Error al cargar los datos: {e}")

st.write('Tabla Items pedidos')
st.dataframe(df_itens_pedidos)
st.write('Tabla pedidos')
st.dataframe(df_pedidos)
st.write('Tabla productos')
st.dataframe(df_productos)
st.write('Tabla vendedores')
st.dataframe(df_vendedores)

st.write('df_final consolidado')
st.dataframe(df_final)