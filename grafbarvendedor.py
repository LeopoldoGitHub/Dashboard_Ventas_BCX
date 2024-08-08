import streamlit as st
import pandas as pd
import plotly.express as px

def crear_grafico_bar_vendedor(df):
    vendedor_ingresos = df.groupby("nombre_vendedor")["total"].sum().reset_index()
    vendedor_ingresos['total'] = vendedor_ingresos['total'] / 1e6  # Convertir a millones
    vendedor_ingresos = vendedor_ingresos.sort_values(by="total", ascending=False)  # Ordenar de mayor a menor
    fig_bar_vendedor = px.bar(vendedor_ingresos, x="total", y="nombre_vendedor", orientation='h', labels={"total": "Ingresos ($)", "nombre_vendedor": "Vendedor"})
    fig_bar_vendedor.update_traces(texttemplate='<b>%{x:.2f} M</b>', textposition='inside', textfont_size=12)
    fig_bar_vendedor.update_layout(xaxis=dict(ticksuffix=' M'))  # Agregar la letra "M" a la escala de valores
    return fig_bar_vendedor
