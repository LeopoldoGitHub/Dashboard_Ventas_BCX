import pandas as pd
import plotly.express as px

def pie_graph(df):
#    vendedores = df.groupby('nombre_vendedor')['cantidad'].sum().sort_values('cantidad', ascending = True).reset_index()
    vendedores = df.groupby('nombre_vendedor').agg(
		cantidad = ('cantidad', 'sum')
	).reset_index()
    colors = ['#0077b6', '#1A4D83', '#063970', '#2f567D', '#4B6A92']
    fig = px.pie(vendedores.head(5),
    values = 'cantidad',
    names = 'nombre_vendedor',
    title = 'Ventas por vendedor',
    color_discrete_sequence = colors
    )
    fig.update_layout(yaxis_title = 'Vendedor', xaxis_title='Cantidad de Productos Vendidos', showlegend=False)
    fig.update_traces(textposition = 'inside', textinfo='percent+label', insidetextfont=dict(size=16))
    return fig
	
	