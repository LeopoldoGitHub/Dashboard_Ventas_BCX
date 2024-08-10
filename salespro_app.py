import streamlit as st
import pandas as pd
import plotly.express as px
import mapbrazil as graficobr
import graflineventas as grafline
import grafbarestado as grafbarest
import grafbarvendedor as grafbarvend
import grafbarproducto as grafbarprod
import grafpievendedor as grafpievend
import preprocesamiento as preprocesamiento
from merge import merge_dataframes
import numpy as np

# Configuración de Streamlit
st.set_page_config(
    page_title="Dashboard de Ventas-SalesPro",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Bienvenido al Dashboard de Ventas-SalesPro")
st.image("./img/LogoSales.jpeg", width=350)

# CSS personalizado para el fondo azul oscuro
st.markdown(
    """
    <style>
    .stApp {
        background-color: #00008B;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Insertar logo en el sidebar
st.sidebar.image("./img/BCX.jpg", width=100) 
st.sidebar.image("./img/LogoSales.jpeg", width=100)
# Sidebar
st.sidebar.header("Filtros")

# Cargar datos
try:
    df_itens_pedidos = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_itens_pedidos.csv')
    df_pedidos = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_pedidos.csv')
    df_productos = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_productos.csv')
    df_vendedores = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_vendedores.csv')
    coordenadas_brasil = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/coordenadas_brasil.csv')
except Exception as e:
    st.error(f"Error al cargar los datos: {e}")

df_itens_pedidos, df_pedidos, df_productos, df_vendedores = preprocesamiento.preprocesamiento(df_itens_pedidos, df_pedidos, df_productos, df_vendedores)

#haciendo merging
df_final = merge_dataframes(df_itens_pedidos, df_pedidos, df_productos, df_vendedores, coordenadas_brasil)

# Convertir la columna de fechas a datetime64[ns]
df_final["fecha_compra"] = pd.to_datetime(df_final["fecha_compra"])

# Filtrado por región
region = st.sidebar.multiselect("Región", options=df_final["name_region"].unique(), help="Sul se refiere al Sur en portugués")

# Filtrado dinámico por estado basado en la región seleccionada
if region:
    estados_disponibles = df_final[df_final["name_region"].isin(region)]["name_state"].unique()
else:
    estados_disponibles = df_final["name_state"].unique()

estados = st.sidebar.multiselect("Estado", options=estados_disponibles)

vendedores = st.sidebar.multiselect("Vendedor", options=df_final["nombre_vendedor"].unique())

productos = ["Todos"] + list(df_final["tipo_producto"].unique())
producto = st.sidebar.selectbox("Productos", productos)

# Año seleccionado
todo_el_periodo = st.sidebar.checkbox("Todo el periodo", value=True)
if not todo_el_periodo:
    año = st.sidebar.slider('Año', df_final["fecha_compra"].dt.year.min(), max_value=df_final["fecha_compra"].dt.year.max())

# Filtrar el dataframe
df_filtrado = df_final.copy()

if region:
    df_filtrado = df_filtrado[df_filtrado["name_region"].isin(region)]
if estados:
    df_filtrado = df_filtrado[df_filtrado["name_state"].isin(estados)]
if vendedores:
    df_filtrado = df_filtrado[df_filtrado["nombre_vendedor"].isin(vendedores)]
if producto != 'Todos':
    df_filtrado = df_filtrado[df_filtrado["tipo_producto"] == producto]
if not todo_el_periodo:
    df_filtrado = df_filtrado[df_filtrado['fecha_compra'].dt.year == año]

# Calcular métricas
total_revenue = df_filtrado["total"].sum() / 1e6  # Convertir a millones
total_sales = df_filtrado["cantidad"].sum() / 1e3  # Convertir a miles

if todo_el_periodo:
    max_year = df_final['fecha_compra'].dt.year.max()
    min_year = max_year - 1
    revenue_min_year = df_final[df_final['fecha_compra'].dt.year == min_year]["total"].sum() / 1e6
    revenue_max_year = df_final[df_final['fecha_compra'].dt.year == max_year]["total"].sum() / 1e6
    sales_min_year = df_final[df_final['fecha_compra'].dt.year == min_year]["cantidad"].sum() / 1e3
    sales_max_year = df_final[df_final['fecha_compra'].dt.year == max_year]["cantidad"].sum() / 1e3
else:
    año_anterior = año - 1
    df_año_anterior = df_final[df_final['fecha_compra'].dt.year == año_anterior]
    previous_total_revenue = df_año_anterior["total"].sum() / 1e6  # Convertir a millones
    previous_total_sales = df_año_anterior["cantidad"].sum() / 1e3  # Convertir a miles

    revenue_min_year = previous_total_revenue
    revenue_max_year = total_revenue
    sales_min_year = previous_total_sales
    sales_max_year = total_sales

revenue_variation = (revenue_max_year - revenue_min_year) / revenue_min_year * 100 if revenue_min_year != 0 else 0
sales_variation = (sales_max_year - sales_min_year) / sales_min_year * 100 if sales_min_year != 0 else 0

# Llamar a los gráficos
mapabr = graficobr.crear_grafico(df_filtrado)
fig_bar_estado = grafbarest.crear_grafico_bar_estado(df_filtrado)
fig_bar_vendedor = grafbarvend.crear_grafico_bar_vendedor(df_filtrado)
fig_line = grafline.crear_grafico_linea(df_filtrado)
fig_bar_producto = grafbarprod.crear_grafico_bar_producto(df_filtrado)
fig_pie_vendedor = grafpievend.crear_grafico_pie_vendedor(df_filtrado)

# Crear 2 columnas
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("Total de Revenues")
    st.metric(label="Total Revenue ($)", value=f"{total_revenue:.2f} M", delta=f"{revenue_variation:.2f}%")

    # Mapa de Brasil- Ingresos por Estado
    st.subheader("Ingresos por Estado($)")
    st.plotly_chart(mapabr, use_container_width=True)

    # Gráfico Barras- Top Ingresos por Estado
    st.subheader("Top Ingresos por Estado ($)")
    st.plotly_chart(fig_bar_estado, use_container_width=True)

    # Ingresos por vendedores
    st.subheader("Ingresos por vendedores ($)")
    st.plotly_chart(fig_bar_vendedor, use_container_width=True)

with col2:
    
    st.subheader("Total de Ventas")
    st.metric(label="Total de Ventas (k)", value=f"{total_sales:.2f} k", delta=f"{sales_variation:.2f}%")

    # Gráfico de líneas de Ingresos mensuales
    st.subheader("Ingresos mensuales")
    st.plotly_chart(fig_line, use_container_width=True)

    # Gráfico Top Ingresos por Productos
    st.subheader("Top Ingresos por Producto ($)")
    st.plotly_chart(fig_bar_producto, use_container_width=True)

    # Ventas por vendedores
    st.subheader("Ventas por vendedores")
    st.plotly_chart(fig_pie_vendedor, use_container_width=True)



#---------------------------------------------------------------

#Fusionar itens_pedidos con coordenadas de Brasil
# # # Leer geodataframe de Brasil.Creado con esta referencia : https://github.com/ipeaGIT/geobr
# brasil_geodf = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/brasil_geodf.csv')

# # # Fusionar los datos de los estados de Brasil con el DataFrame df_itens_pedidos
# df_itens_pedidos = df_itens_pedidos.merge(brasil_geodf, left_on='abbrev_state', right_on='abbrev_state', how='inner')
# # Eliminar la columna 'ciudad' ya que es redundante
# df_itens_pedidos=df_itens_pedidos.drop(columns=['ciudad'])
# #Renombramos columna de valor total para diferenciar del valor total de pedidos
# df_itens_pedidos = df_itens_pedidos.rename(columns={'valor_total': 'valor_total_itens'})

# # #Tratamiento y creación de df_final
# merged1 = pd.merge(df_itens_pedidos, df_pedidos, on=['producto_id', 'pedido_id'])
# merged2 = pd.merge(merged1, df_productos, on='producto_id')
# df_final = pd.merge(merged2, df_vendedores, on='vendedor_id')

#----------------------------------------------------------------

