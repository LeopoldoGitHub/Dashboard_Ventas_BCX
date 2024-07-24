import streamlit as st
import pandas as pd
import plotly.express as px

def crear_grafico_pie_vendedor(df):
    ventas_vendedor = df["nombre_vendedor"].value_counts().reset_index()
    ventas_vendedor.columns = ["nombre_vendedor", "ventas"]
    # Definir la paleta de colores azul
    blue_palette = px.colors.sequential.Blues_r #Blues_r, Ice, Teal, Tealgrn

    fig_pie_vendedor = px.pie(ventas_vendedor, values="ventas", names="nombre_vendedor", labels={"ventas": "Ventas", "nombre_vendedor": "Vendedor"}, color_discrete_sequence=blue_palette)
    fig_pie_vendedor.update_traces(textinfo="label+percent", showlegend=False, textfont=dict(size=11, color="white", family="Arial"))
    
    return fig_pie_vendedor