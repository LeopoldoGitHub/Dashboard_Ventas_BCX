import pandas as pd
import streamlit as st
import pandas as pd
# import geobr
import plotly.express as px
st.title('Dashboard G2')
st.sidebar.title('Filtros')
###Cargar datos
df_itens_pedidos=pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_itens_pedidos.csv')
df_pedidos=pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_pedidos.csv')
df_productos=pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_productos.csv')
df_vendedores=pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_vendedores.csv')
st.write('Tabla Items pedidos')
st.dataframe(df_itens_pedidos)
st.write('Tabla pedidos')
st.dataframe(df_pedidos)
st.write('Tabla productos')
st.dataframe(df_productos)
st.write('Tabla vendedores')
st.dataframe(df_vendedores)

##Tratamiento de los datos.
##Crear función de preprocesamiento

def preprocesamiento(df_itens_pedidos, df_pedidos, df_productos, df_vendedores):
    """
    Realiza tareas de preprocesamiento en los DataFrames.

    Args:
        df_itens_pedidos, df_pedidos, df_productos, df_vendedores: DataFrames de entrada.

    Returns:
        Tupla de DataFrames .
    """
    dataframes = [df_itens_pedidos, df_pedidos, df_productos, df_vendedores]

    # Convertir la columna 'fecha_compra' a datetime
    df_pedidos['fecha_compra'] = pd.to_datetime(df_pedidos['fecha_compra'])

    for df in dataframes:
        if df is None:
            raise ValueError("Todos los DataFrames deben ser no nulos.")

        # Eliminar registros duplicados
        df.drop_duplicates(inplace=True)

        # Convertir columnas numéricas a tipos adecuados
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

        # Convertir columnas de tipo 'object' a 'str'
        object_columns = df.select_dtypes(include=['object']).columns
        df[object_columns] = df[object_columns].astype(str)



    return df_itens_pedidos, df_pedidos, df_productos, df_vendedores

##Procesamiento de los dataframe con la función creada.

df_itens_pedidos, df_pedidos, df_productos, df_vendedores = preprocesamiento(
    df_itens_pedidos, df_pedidos, df_productos, df_vendedores
)

##Realizar limpieza final:

# Eliminar filas con valores NaN en la columna "sku" del dataframe productos
df_productos.dropna(subset=['sku'], inplace=True)

# Eliminar vendedor "unknown" del dataframe vendedores
df_vendedores = df_vendedores[df_vendedores["vendedor_id"] != 6]

# # Eliminar filas con valores de pedido_id = 341 en df_itens_pedidos , asociado a una venta del vendedor 6, quien ya fue eliminado

# Filtrar las filas donde el pedido_id es diferente a 341 y generar un nuevo dataframe
df_itens_pedidos = df_itens_pedidos[df_itens_pedidos['pedido_id'] != 341]


# # Eliminar filas con valores de vendedor_id =6 en la columna vendedor_id" del dataframe df_pedidos
df_pedidos = df_pedidos[df_pedidos['vendedor_id'] != 6]

# Reindexar el DataFrame después de eliminar las filas
df_itens_pedidos .reset_index(drop=True, inplace=True)


##--------------##

#### 3. **Feature Engineering**
##Ciudades y Geobr
# Eliminar 'BR-' de la columna ciudad y guardar el resultado en abbrev_state

df_itens_pedidos['abbrev_state'] = df_itens_pedidos['ciudad'].str.replace('BR-', '')

# Leer los datos de los estados de Brasil.La función read_state() descarga datos geoespaciales de los estados brasileños.
df_brasil_coordenadas=pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/brasil_coordenas.csv')


# Fusionar los datos de los estados de Brasil con el DataFrame df_itens_pedidos
df_itens_pedidos = df_itens_pedidos.merge(df_brasil_coordenadas, left_on='abbrev_state', right_on='abbrev_state', how='inner')


##*PRODUCTOS.*
##---
###Crear nombre simple de los productos para facilitar los filtros##
df_productos['tipo_producto'] = df_productos['producto'].str.split().str[0]

##*PEDIDOS.*
#---
#Separar la fecha en año y mes para facilitar los filtros

df_pedidos['año'] = df_pedidos['fecha_compra'].dt.year
df_pedidos['mes'] = df_pedidos['fecha_compra'].dt.month

##*DataFrame FINAL*
# ---
# Realizar la concatenación de los dataframe utilizados para generar uno con la informaicón consolidada

merged1 = pd.merge(df_itens_pedidos, df_pedidos, on=['producto_id', 'pedido_id'])
merged2 = pd.merge(merged1, df_productos, on='producto_id')
df_final = pd.merge(merged2, df_vendedores, on='vendedor_id')
st.dataframe(df_final)
# estados = sorted(list(df_final['state_name'].unique()))
# ciudades = st.sidebar.multiselect('Estados', estados)

