import streamlit as st
import pandas as pd
import streamlit.web.cli as stcli
import plotly.express as px

def create_graph(df):
    #df_maps = df.groupby('geolocation_state').agg({
    #'total_amount':'sum',
    #'geolocation_lat':'mean',
    #'geolocation_lng':'mean'
    #}).reset_index().sort_values(by='total_amount',ascending=False)

    graph_map = px.scatter_geo(df,
                           lat = 'avg_latitude',
                           lon='avg_longitude',
                           scope='south america',
                           template='seaborn',
                           size='valor_total',
                           hover_name='initials_state',
                           hover_data={'avg_latitude': False, 'avg_longitude': False},
                           title='Incomes per state'
                           )
    
    return graph_map





