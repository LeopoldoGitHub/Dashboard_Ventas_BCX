import pandas as pd
import plotly.express as px

def create_graph(df):
    #df_review = df.groupby('review_score').agg(
    #    total_sales = ('cantidad_itens','sum')
    #).reset_index()

    colors = ['#0077b6','#1A4D83','#063970','#2f567D','#4B6A92']
    fig = px.pie(df,
                 values='total_per_seller',
                 names = 'name_seller',
                 title = 'Sales per seller',
                 color_discrete_sequence=colors
    )

    fig.update_layout(yaxis_title = 'Score',xaxis_title = 'Sales',showlegend = False)
    fig.update_traces(textposition = 'inside',textinfo = 'percent + label', insidetextfont=dict(size=16))
    return fig