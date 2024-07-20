import pandas as pd
import plotly.express as px

def create_graph(df):

    fig = px.bar(df.tail(10),
                 x = 'product_type',
                 y='total_per_product',
                 text= 'total_per_product',
                 title= 'Top incomes per product ($)'
                 )
    
    fig.update_layout(yaxis_title = 'Products', xaxis_title = 'Incomes ($)', showlegend = False)
    fig.update_traces(texttemplate = '%{text:.3s}')
    return fig
