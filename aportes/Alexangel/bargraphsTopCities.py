import pandas as pd
import plotly.express as px

def create_graph(df):

    fig = px.bar(df.tail(10),
                 x = 'state_name',
                 y='sales_per_state',
                 text= 'sales_per_state',
                 title= 'Top incomes per states ($)'
                 )
    
    fig.update_layout(yaxis_title = 'Incomes per states ($)', xaxis_title = 'States', showlegend = False)
    fig.update_traces(texttemplate = '%{text:.3s}')
    return fig
