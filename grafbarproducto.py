import streamlit as st
import pandas as pd
import plotly.express as px

def crear_grafico_bar_producto(df):
    top_ventas_producto = df.groupby("tipo_producto")["total"].sum().reset_index().nlargest(10, 'total')
    fig_bar_producto = px.bar(top_ventas_producto, x="tipo_producto", y="total", orientation='v', labels={"total": "Ingresos ($)", "tipo_producto": "Tipo de Producto"})
    fig_bar_producto.update_traces(texttemplate='<b>%{y:.3s}</b>', textposition='inside', textfont_size=12, textangle=90)
    
    return fig_bar_producto