import streamlit as st
import pandas as pd
import psycopg2 as post
import mapgraphs as mapgraph
import linegraphs as linesgraph
import bargraphs as bargraph
import pizzagraph as pizzagraph

## settings of the layoout
st.set_page_config(layout='wide')
st.title("Sales  Dashboard  🛒 \n 2019 - 2021")
st.sidebar.image('fashionShop.jpeg')

## dataframes
df_final = pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_final.csv')
df_map = pd.read_csv('df_map.csv')
df_bar = pd.read_csv('df_bar.csv')
df_lines = pd.read_csv('df_lines.csv')
df_pizza = pd.read_csv('df_pizza.csv')
#st.dataframe(df_map)
 

## filters

st.sidebar.title('Filters')

# states: multiselect
states = ['Bahia', 'Rio de Janeiro','Paraíba','Distrito Federal','Minas Gerais','Paraná','Mato Grosso del Sur',
          'San Pablo','Goiás','Amazonas','Ceará','Río Grande del Sur','Acre','Rondonia','Mato Grosso',
          'Roraima','Pernambuco','Maranhao','Pará','Santa Catarina','Sergipe','Tocantins','Amapá','Piauí',
          'Espírito Santo','Alagoas','Río Grande del Norte']

states_multiselect = st.sidebar.multiselect('States',states)

# products: selectbox
products = sorted(list(df_final['product_type'].dropna().unique()))
products.insert(0,'All')
product = st.sidebar.selectbox('Products',products)

if product!='All':
    df_bar = df_bar[df_bar['product_type']==product]

# ages: checkbox
ages = st.sidebar.checkbox('All the period',value=True)


# we use df_lines because instead of df_final because it has the column 'year'.
if not ages:
    age = st.sidebar.slider('Age',df_lines['year'].min(),df_lines['year'].max())
if not ages:
    df_lines = df_lines[df_lines['year']==age]


# filtering the data
if states_multiselect:
    df_final = df_final[df_final['state_name'].isin(states_multiselect)]
else:
    df_final = df_final



## graphics
graph_map = mapgraph.create_graph(df_map)
graph_bar = bargraph.create_graph(df_bar)
graph_lines = linesgraph.create_graph(df_lines)
graph_pizza = pizzagraph.create_graph(df_pizza)

## setting of the columns
col1,col2 = st.columns(2)
with col1:
     if states_multiselect:
        st.metric(f'**Total revenue {states_multiselect}**',df_final['valor_total'].sum())
        st.plotly_chart(graph_map,use_container_width=True)
        st.plotly_chart(graph_bar,use_container_width=True)
     else:
        st.metric(f'**Total revenue**',df_final['valor_total'].sum(),'$')
        st.plotly_chart(graph_map,use_container_width=True)
        st.plotly_chart(graph_bar,use_container_width=True)
         
with col2:
    if states_multiselect:
        st.metric(f'**Total items sold {states_multiselect}**',df_final['cantidad'].sum())
        st.plotly_chart(graph_lines,use_container_width=True)
        st.plotly_chart(graph_pizza,use_container_width=True)
    else:
        st.metric(f'**Total items sold**',df_final['cantidad'].sum())
        st.plotly_chart(graph_lines,use_container_width=True)
        st.plotly_chart(graph_pizza,use_container_width=True)









## may be this function works
#def format_number(value,prefix = ''):
#    for unit in ['','k']:
#        if value < 1000 :
#            return f'{prefix}{value:.2f} {unit}'
#        value /= 1000
#    return f'{prefix}{value:.2f} M'







