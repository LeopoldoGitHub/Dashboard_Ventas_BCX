import streamlit as st
import pandas as pd
import plotly.express as px

def preprocesamiento(df_itens_pedidos, df_pedidos, df_productos, df_vendedores):
    """
    Realiza tareas de preprocesamiento en los DataFrames.

    Args:
        df_itens_pedidos, df_pedidos, df_productos, df_vendedores: DataFrames de entrada.

    Returns:
        Tupla de DataFrames.
    """
    
    dataframes = [df_itens_pedidos, df_pedidos, df_productos, df_vendedores]

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

    # Eliminar filas con valores NaN en la columna "sku" del dataframe productos
    df_productos.dropna(subset=['sku'], inplace=True)
    
    # Crear nombre simple de los productos para facilitar los filtros
    df_productos['tipo_producto'] = df_productos['producto'].str.split().str[0]
    
    # Convertir la columna 'fecha_compra' a datetime
    df_pedidos['fecha_compra'] = pd.to_datetime(df_pedidos['fecha_compra'])

    # Eliminar filas con valores de vendedor_id = 6 en la columna vendedor_id del dataframe df_pedidos
    df_pedidos = df_pedidos[df_pedidos['vendedor_id'] != 6]
    
    # Separar fecha de año y mes en df_pedidos para mejorar los filtros
    df_pedidos['año'] = df_pedidos['fecha_compra'].dt.year
    df_pedidos['mes'] = df_pedidos['fecha_compra'].dt.month
       
    # Eliminar vendedor "unknown" del dataframe vendedores
    df_vendedores = df_vendedores[df_vendedores["vendedor_id"] != 6]
    
    # Eliminar filas con valores de pedido_id = 341 en df_itens_pedidos, asociado a una venta del vendedor 6, quien ya fue eliminado
    df_itens_pedidos = df_itens_pedidos[df_itens_pedidos['pedido_id'] != 341]

    # Reindexar el DataFrame después de eliminar las filas
    df_itens_pedidos.reset_index(drop=True, inplace=True)
    
    # Crear columna con sólo las siglas de los estados
    #df_itens_pedidos['abbrev_state'] = df_itens_pedidos['ciudad'].str.replace('BR-', '')
    df_itens_pedidos = df_itens_pedidos.copy()  # hice este cambio porque me daba un error, si gustan comenten la linea 60 y 61 y luego descomenten la 59 que es el codigo original
    df_itens_pedidos.loc[:, 'abbrev_state'] = df_itens_pedidos['ciudad'].str.replace('BR-', '')


    
    return df_itens_pedidos, df_pedidos, df_productos, df_vendedores



