import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import json
from urllib.request import urlopen

# Cargar el archivo GeoJSON con la geometría de Brasil
with urlopen('https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson') as response:
    gdf_brazil = json.load(response)
    

##Funcion crear mapa
def crear_grafico(df):
    df_resumido = (
        df.groupby(['abbrev_state', 'name_state'])['total']
        .sum()
        .reset_index()
        .sort_values(by='total', ascending=False)
    )
        
    data = dict(type ='choropleth',
            locationmode ='geojson-id',
            geojson = gdf_brazil,
            locations = df_resumido['abbrev_state'],
            featureidkey = 'properties.sigla',
            colorscale ='blues',
            text = df_resumido['name_state'],
            z = df_resumido['total'],
            customdata = df_resumido[['name_state','total']],
            colorbar = {'title':'Ingresos ($)','tickformat': '.3s'}        
            )
    layout = dict(
                title='',
                geo =dict(
                     scope='south america',
                     resolution=50,
                     lonaxis=dict(range=[-85, -30]), # Ampliar el rango de longitud)
                     lataxis=dict(range=[-40, 10]), # Ampliar el rango de latitud)
                     showframe=False, #desactiva el marco del mapa
                     showcoastlines=False, #desactiva las lineas de costa
                     showland=False, #desactiva la visualización de la tierra
                     landcolor='rgba(0,0,0,0)', #Colorea la tierra con transparencia
                     showcountries=False, #desactiva las lineas del pais
                     showlakes=False, #desactiva la visualización de los lagos
                     showrivers=False, #desactiva la visualización de los ríos
                     showocean=False, #desactiva la visualización del oceano
                     fitbounds='locations', #ajusta el mapa a los datos
               ),
               title_x=0,
               width=800, #Ajustar al ancho del grafico
               height=500, #Ajustar la altura del gráfico
          )
    fig = go.Figure([data], layout=layout)
    fig.update_layout(geo=dict(bgcolor='rgba(00,0,0,0)'))
    fig.update_traces(hovertemplate="<b>%{customdata[0]}</b><br> Ingresos Totales ($): %{customdata[1]:,.0f} <extra></extra>", marker_line_width=0
    )
    return fig

