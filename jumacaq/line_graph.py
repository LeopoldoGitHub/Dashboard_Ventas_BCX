import pandas as pd
import plotly.express as px

def line_graph(df):
  revenues_monthly = df.set_index('fecha_compra').groupby(pd.Grouper(freq = 'ME'))['total'].sum().reset_index()
  revenues_monthly['Year'] = revenues_monthly['fecha_compra'].dt.year
  revenues_monthly['Month'] = revenues_monthly['fecha_compra'].dt.month_name()
  fig = px.line(revenues_monthly,
    x = 'Month',
    y = 'total',
    markers = True,
    range_y = (0, revenues_monthly.max()),
    color = 'Year',
    title= 'Ingresos Mensuales')
  fig.update_layout(yaxis_title='Ingresos ($)',xaxis_title='Mes')
  return fig
 