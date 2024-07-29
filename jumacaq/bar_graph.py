import pandas as pd
import plotly.express as px

def bar_graph(df):
	revenue_productos = df.groupby('tipo_producto')[['total']].sum().sort_values('total', ascending = True).reset_index()

	fig = px.bar(revenue_productos.tail(10),
		x = 'total',
		y = 'tipo_producto',
		text = 'total',
		title = 'Top Ingresos por Producto ($)'
	)
	fig.update_layout(yaxis_title = 'Productos', xaxis_title='Ingresos ($)', showlegend=False)
	fig.update_traces(texttemplate = '%{text:.3s}')

	return fig