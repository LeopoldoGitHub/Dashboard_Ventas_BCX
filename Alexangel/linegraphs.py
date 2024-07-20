import pandas as pd
import plotly.express as px

def create_graph(df):
    #revenue_monthly = df.set_index('order_purchase_timestamp').groupby(pd.Grouper(freq='ME'))['total_amount'].sum().reset_index()
    #revenue_monthly['Year'] = revenue_monthly['order_purchase_timestamp'].dt.year
    #revenue_monthly['Month'] = revenue_monthly['order_purchase_timestamp'].dt.month_name()
    #revenue_monthly = revenue_monthly[revenue_monthly['Year'] > 2016]

    fig = px.line(df,
                  x = 'month',
                  y= 'total_per_month',
                  markers=True,
                  range_y=(0,df.max()),
                  color= 'year',
                  line_dash='year',
                  title='Incomes per month'
                  )
    
    fig.update_layout(yaxis_title = 'Monthly incomes over the years ($)')

    return fig










