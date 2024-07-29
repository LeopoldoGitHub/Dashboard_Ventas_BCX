import streamlit as st
import pandas as pd
import map_graph as g1
import line_graph as g2
import bar_graph as g3
import pie_graph as g4


#Set the layout to wide mode to allow full-width content
st.set_page_config(layout='wide')

#Title of the page  and introduction message
st.title('Dashboard de ventas :shopping_trolley:')
st.write('HOLA')

def formata_numero(valor, prefijo = ''):
	for unidad in ['', 'k']:
		if valor<1000:
			return f'{prefijo} {valor:.2f} {unidad}'
		valor /= 1000
	return f'{prefijo} {valor:.2f} M'
df_items = pd.read_csv('df_itens_pedidos.csv')

#Obtaining CSV file from a github's public repository 
df_final_raw= pd.read_csv('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/BBDD/df_final.csv')
df_final_raw['fecha_compra'] = pd.to_datetime(df_final_raw['fecha_compra'])
st.dataframe(df_final_raw)


# Create sidebar for filtering
st.sidebar.image('https://raw.githubusercontent.com/LeopoldoGitHub/Dashboard_Ventas_BCX/main/img/Logo.jpeg')
st.sidebar.title('Filtros')
estados = sorted(list(df_final_raw['name_state'].unique()))
#estados = ['Acre','Alagoas','Amapá','Amazonas','Bahia','Ceará','Distrito Federal','Espírito Santo','Goiás','Maranhão','Mato Grosso','Mato Grosso do Sul','Minas Gerais','Pará','Paraíba','Paraná','Pernambuco','Piauí','Rio de Janeiro','Rio Grande do Norte','Rio Grande do Sul','Rondônia','Roraima','Santa Catarina','São Paulo','Sergipe','Tocantins']
ciudades = st.sidebar.multiselect('Estados', estados)
#producto = ["Todos"] + list(df_final_raw["tipo_producto"].unique())
producto = sorted(list(df_final_raw['tipo_producto'].unique()))
producto.insert(0, 'Todos')
productos = st.sidebar.selectbox('Productos', producto)
años = st.sidebar.checkbox('Todos los años', value=True)
if not años:
    años_filtrados = st.sidebar.slider('Años', df_final_raw['fecha_compra'].dt.year.min(), df_final_raw['fecha_compra'].dt.year.max() )

#Filtering datasets
if ciudades:
    df_final_raw = df_final_raw[df_final_raw['name_state'].isin(ciudades)] 
    
if productos!= 'Todos':
    df_final_raw = df_final_raw[df_final_raw['tipo_producto']== productos]
    
if not años:
    df_final_raw = df_final_raw[df_final_raw['fecha_compra'].dt.year == años_filtrados]
    
# Calling graphs
graf_mapa = g1.create_map(df_final_raw)
graf_linea = g2.line_graph(df_final_raw)
graf_bar = g3.bar_graph(df_final_raw)
graf_torta = g4.pie_graph(df_final_raw)

#Creating columns and metrics
col1,col2 = st.columns(2)
with col1:
    st.metric('**Ingresos Totales**',formata_numero(df_final_raw['total'].sum(),'$'))
    st.plotly_chart(graf_mapa,use_container_width=True)
    st.plotly_chart(graf_bar,use_container_width=True)    
with col2:
    st.metric('**Cantidad de productos vendidos**',formata_numero(df_final_raw['cantidad'].sum()))
    st.plotly_chart(graf_linea,use_container_width=True)
    st.plotly_chart(graf_torta,use_container_width=True)
    


    

