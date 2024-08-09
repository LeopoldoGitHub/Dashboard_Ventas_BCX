import streamlit as st
import pandas as pd
import plotly.express as px
import geobr
import geopandas as gpd

def merge_dataframes(df_itens_pedidos, df_pedidos, df_productos, df_vendedores):
    """
    Realiza el merge entre los DataFrames de items de pedidos, pedidos, productos y vendedores,
    y añade la información geográfica de los estados brasileños.

    Args:
        df_itens_pedidos, df_pedidos, df_productos, df_vendedores: DataFrames de entrada.

    Returns:
        DataFrame combinado con la información geográfica de los estados brasileños.
    """
    
    # Hacer el merge entre df_itens_pedidos y df_pedidos
    df_merged = pd.merge(df_itens_pedidos, df_pedidos, on="pedido_id", how="left")
    df_merged['producto_id'] = df_merged['producto_id_x']  # Renombrar 'producto_id_x' a 'producto_id'
    df_merged.drop(columns=['producto_id_x', 'producto_id_y'], inplace=True)  # Eliminar las columnas innecesarias

    # Unir df_merged con df_productos
    df_productos = df_productos.rename(columns={'producto_id': 'producto_id_prod'})  # Renombrar columnas en df_productos
    df_merged = pd.merge(df_merged, df_productos, left_on='producto_id', right_on='producto_id_prod', how='left')
    df_merged.drop(columns=['producto_id_prod'], inplace=True)  # Eliminar columna duplicada

    # Renombrar columnas en df_vendedores para evitar conflictos
    df_vendedores = df_vendedores.rename(columns={'vendedor_id': 'vendedor_id_vend'}) 
    df_merged = pd.merge(df_merged, df_vendedores, left_on='vendedor_id', right_on='vendedor_id_vend', how='left')
    df_merged.drop(columns=['vendedor_id_vend'], inplace=True)

    # Cargar los datos de estados brasileños usando geobr
    estados_brasil = geobr.read_state()

    # Reproyectar las geometrías a un CRS geográfico (EPSG:4326)
    estados_brasil = estados_brasil.to_crs(epsg=4326)

    # Extraer latitud y longitud de la columna 'geometry'
    estados_brasil['geolocation_lat'] = estados_brasil['geometry'].centroid.y
    estados_brasil['geolocation_lng'] = estados_brasil['geometry'].centroid.x

    # Filtrar la información de geobr para obtener las columnas necesarias
    estados_brasil = estados_brasil[['abbrev_state', 'name_state', 'name_region', 'geolocation_lat', 'geolocation_lng']]

    # Realizar el merge con df_merged
    df_merged = df_merged.merge(estados_brasil, on='abbrev_state', how='left')

    return df_merged
