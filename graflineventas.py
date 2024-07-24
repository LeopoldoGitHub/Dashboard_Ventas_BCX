import streamlit as st
import pandas as pd
import plotly.express as px

##Funcion crear grafico de lineas de ingresos totales
def crear_grafico_linea(df):

    ingreso_mensual = df.set_index('fecha_compra').groupby(pd.Grouper(freq='ME'))["total"].sum().reset_index()
    ingreso_mensual['Año'] = ingreso_mensual['fecha_compra'].dt.year
    ingreso_mensual['Mes'] = ingreso_mensual['fecha_compra'].dt.month_name()
    
    fig_line = px.line(ingreso_mensual,
                       x="Mes",
                       y="total",
                       markers=True,
                       range_y=(0, ingreso_mensual.max()),
                       color = 'Año',
                       line_dash = 'Año',
                       )
    
    return fig_line