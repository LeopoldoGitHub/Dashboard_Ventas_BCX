import pandas as pd
import plotly.express as px

def create_map(df):
    df_mapa = df.groupby('name_state').agg({
		'total' : 'sum',
		'geolocation_lat': 'mean',
		'geolocation_lng': 'mean'
	}).reset_index().sort_values(by='total', ascending=False)
    graf_mapa = px.scatter_geo(df_mapa,
		lat = 'geolocation_lat',
		lon = 'geolocation_lng',
		scope = 'south america',
		template = 'seaborn',
		size = 'total',
		hover_name = 'name_state',
		hover_data = {'geolocation_lat':False, 'geolocation_lng':False},
		title = 'Ingresos por estado')
    return graf_mapa