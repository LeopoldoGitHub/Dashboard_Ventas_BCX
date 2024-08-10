import streamlit as st
import pandas as pd
import plotly.express as px

def merge_dataframes(df_itens_pedidos, df_pedidos, df_productos, df_vendedores, coordenadas_brasil):
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

    # Realizar el merge con df_merged
    df_merged = df_merged.merge(coordenadas_brasil, on='abbrev_state', how='left')
    
    # Eliminar la columna 'ciudad'
    df_merged.drop(columns=['ciudad'], inplace=True)

# Renombrar la columna 'valor_total' a 'valor_total_itens'
    df_merged.rename(columns={'valor_total': 'valor_total_itens'}, inplace=True)

    return df_merged
