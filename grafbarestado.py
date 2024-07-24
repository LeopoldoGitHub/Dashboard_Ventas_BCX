import streamlit as st
import pandas as pd
import plotly.express as px

##Funcion crear grafico de barras top ingresos por estados
def crear_grafico_bar_estado(df):

    top_ventas_estado = df.groupby("name_state")["total"].sum().reset_index().nlargest(10, 'total')
    fig_bar_estado = px.bar(top_ventas_estado, x="name_state", y="total", orientation='v', labels={"total": "Ingresos ($)", "name_state": "Estados"})
    fig_bar_estado.update_traces(texttemplate='<b>%{y:.3s}</b>', textposition='inside', textfont=dict(size=12))  # Ajustar el texto
    
    return fig_bar_estado