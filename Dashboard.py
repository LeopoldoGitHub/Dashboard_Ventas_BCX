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

# Configuración de Streamlit
st.set_page_config(
    page_title="Dashboard de Ventas-G2",
    layout="wide",
    initial_sidebar_state="expanded",
)
# Página principal
st.title("DASHBOARD DE VENTAS 🛒")

# Cargar datos
try:
    df_itens_pedidos = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_itens_pedidos.csv')
    df_pedidos = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_pedidos.csv')
    df_productos = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_productos.csv')
    df_vendedores = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_vendedores.csv')
    df_final = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_final.csv')
except Exception as e:
    st.error(f"Error al cargar los datos: {e}")
df_itens_pedidos, df_pedidos, df_productos, df_vendedores= preprocesamiento.preprocesamiento(df_itens_pedidos, df_pedidos, df_productos, df_vendedores)

#Fusionar itens_pedidos con coordenadas de Brasil
# # Leer geodataframe de Brasil.Creado con esta referencia : https://github.com/ipeaGIT/geobr
brasil_geodf = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/brasil_geodf.csv')

# # Fusionar los datos de los estados de Brasil con el DataFrame df_itens_pedidos
df_itens_pedidos = df_itens_pedidos.merge(brasil_geodf, left_on='abbrev_state', right_on='abbrev_state', how='inner')
# Eliminar la columna 'ciudad' ya que es redundante
df_itens_pedidos=df_itens_pedidos.drop(columns=['ciudad'])
#Renombramos columna de valor total para diferenciar del valor total de pedidos
df_itens_pedidos = df_itens_pedidos.rename(columns={'valor_total': 'valor_total_itens'})



# #Tratamiento y creación de df_final
merged1 = pd.merge(df_itens_pedidos, df_pedidos, on=['producto_id', 'pedido_id'])
merged2 = pd.merge(merged1, df_productos, on='producto_id')
df_final = pd.merge(merged2, df_vendedores, on='vendedor_id')

# Asegurar Convertir la columna de fechas a datetime64[ns]
df_final["fecha_compra"] = pd.to_datetime(df_final["fecha_compra"])

st.write('df_final consolidado')
st.dataframe(df_final)


# Sidebar
st.sidebar.header("Filtros")

estados = st.sidebar.multiselect("Estado", options=df_final["name_state"].unique())
region = st.sidebar.multiselect("Región", options=df_final["name_region"].unique(), help="Sul se refiere al Sur en portugués")

productos = ["Todos"] + list(df_final["tipo_producto"].unique())
producto = st.sidebar.selectbox("Productos", productos)

#--------------------------
años = st.sidebar.checkbox("Todo el periodo", value= True)
if not años:
    año = st.sidebar.slider('Año',df_final["fecha_compra"].dt.year.min(),max_value=df_final["fecha_compra"].dt.year.max())


# Filtrar el dataframe
if estados :
    df_final = df_final[df_final["name_state"].isin(estados)]
if region :
    df_final = df_final[df_final["name_region"].isin(region)]
if producto != 'Todos':
    df_final = df_final[df_final["tipo_producto"] == producto]
if not años:
    df_final = df_final[df_final['fecha_compra'].dt.year==año]
# if años:
#     delta_valor, delta_ventas = calcular_deltas(df_final)
# else:
#     delta_valor, delta_ventas = calcular_deltas(df_final[df_final['fecha_compra'].dt.year.isin('año')])
#     df_final=df_final[df_final['fecha_compra'].dt.year==año]


# Métricas
total_revenue = df_final["total"].sum() / 1e6  # Convertir a millones
total_sales = df_final["cantidad"].sum() / 1e3  # Convertir a miles
previous_total_revenue = 40.0  # Ejemplo
previous_total_sales = 80.0  # Ejemplo

revenue_variation = (total_revenue - previous_total_revenue) / previous_total_revenue * 100
sales_variation = (total_sales - previous_total_sales) / previous_total_sales * 100

##Llamar a los graficos
mapabr =graficobr.crear_grafico(df_final)
fig_bar_estado=grafbarest.crear_grafico_bar_estado(df_final)
fig_bar_vendedor=grafbarvend.crear_grafico_bar_vendedor(df_final)
fig_line = grafline.crear_grafico_linea(df_final)
fig_bar_producto = grafbarprod.crear_grafico_bar_producto(df_final)
fig_pie_vendedor = grafpievend.crear_grafico_pie_vendedor(df_final)

#crear 2 columnas
col1, col2 = st.columns(2)

with col1:
    st.subheader("Total de Revenues")
    st.metric(label="Total Revenue ($)", value=f"{total_revenue:.2f} M", delta=f"{revenue_variation:.2f}%")
 
    # Mapa de Brasil- Ingresos por Estado
    st.subheader("Ingresos por Estado($)")
    st.plotly_chart(mapabr, use_container_width=True)

    # Grafico Barras- Top Ingresos por Estado
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

    # Grafico Top Ingresos por Productos
    st.subheader("Top Ingresos por Producto ($)")
    st.plotly_chart(fig_bar_producto, use_container_width=True)

    # Ventas por vendedores
    st.subheader("Ventas por vendedores")
    st.plotly_chart(fig_pie_vendedor, use_container_width=True)
