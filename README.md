# **Dashboard de Ventas**
Bootcamp Xperience

<img src="img/LogoSales.jpeg" alt="SalesPro" width="200"/>

## Información
Aplicación en línea que muestra información consolidadada por regiones, ciudades, vendedores y productos de la evolución de compras en una tienda ubicada en el territorio brasilero. 
Dashboard interactivo de una empresa de e-commerce desplegado en la plataforma Streamlit.

## Paso a Paso
Detalle del tratamiento de los datos. Obtención, estandarización y consolidación de los datos.

1) El Negocio. El Cliente.

Una tienda en línea, de artículos de moda, con presencia en todo Brasil, necesita impulsar su rendimiento utilizando sus datos de manera estratégica.
Como científicos de datos, hemos sido convocados para analizar datos de transacciones de tres períodos calendario y ofrecer una vison interna profunda sobre los consumidores que guíen sus decisiones respondiendo a preguntas clave:
                    
                    ¿Cuál es el Top 5 productos más vendidos históricamente?

                    ¿Cuál es la evolución histórica de las ingresos netos?

                    ¿Cuáles son los ingresos netos por vendedor por año?

                    ¿Cuáles son las ciudades que proporcionan mayores ingresos netos?

                    Otro insight. 
 
2) Obtención, Tratamiento y Análisis Exploratório (EDA)

Proceso de investigación en el que, usando estadísticas de resumen y herramientas gráficas, se llega a conocer los datos y comprender lo que se puede averiguar de ellos.

Diagnóstico:
Se identificaron inconsistencias en cuanto al producto_id -únicos (205)- y producto -únicos (201)- determinando lo siguiente:

a) Calca Alfaiataria Preta 2--->2 marcas (Mixed y Lelis Blanc): Justificado

b) Saia Pregas Preta       2--->1 marca (Zara) precios distintos: Injustificado

c) Vestido Recortes Cores  2--->2 marcas (Alix Shop y Bcbgmaxzria): Justificado

d) Calca Jeans Costuras    2--->2 marcas (Seven y Diesel): Justificado

Consideramos justificada la diferencia en el mismo producto cuando son de marcas diferentes, lo que genera SKU y producto_id diferentes, también precio. Sin embargo, el producto Saia Pregas Preta, es la misma marca, el mismo nombre, pero con precios y id distintos. Se decide dejar esos datos considerando que pueden ser de tallas distintas y de precio mayor o que tienen un diferente calidad.

### Gráficos explicativos
  Histogramas
  
![Histogramas](img/Histogramas-items_pedidos.jpg)

  Distribución de Pedidos por Ciudad

![Pedidos por Ciudad](img/DistribucionPedidosCiudad.jpg)

  Distribuciones con Diagramas de Caja (Bloxplot) Exploratorios

![Boxplots](img/Plots-Distribuciones.jpg)

  Distribución con Densidad de Montos de los Pedidos

![Densidad Montos Pedidos](img/Distribucion-MontosPedidosDensidad.jpg)

  Cantidad de Pedidos Por Vendedor
![Pedidos por Vendedor](img/CantidadPedidosVendedor.jpg)

  Evolución Total de Pedidos en el Tiempo
![Evolución de los Pedidos](img/EvolucionTotalPedidosFecha.jpg)

  Productos por su Condición
  
![Cantidad de Productos por Condición](img/CantidadProducosCondicion.jpg)

  Distribución de Precios por Condición
![Precios por Condición Producto](img/DistribucionPreciosCondicionProducto.jpg)

  Ventas por Mes por Año
![Ventas Mes Año](img/LineasVentasMesAnio.jpg)

## Tablero de Ventas 

Funcionalidades:   Cuadros -   Filtros  - Gráficos

  Página Principal
  
![Home SalesPro](img/SalesProDashboardBX.jpg)

  Filtros Habilitados para Selecciones

![Filtros Selección](img/SalesProDashboardGraficos.png)

  Ejemplo Filtro por Estado

![Filtro por Estado](img/SalesProDashEstado.png)

  Selección de Ventas de un producto por Vendedores
  
  ![Ventas de Un producto por Vendedor](img/SalesProDashVendeoresProd.png)
  
## <h3 align="center">🛠️ Miembros del Equipo</h3>
<br>
<div align="center"> 

|Participantes|Roles|Redes|
|:---:|:---:|:---:|
|**Mirna**|![](https://img.shields.io/badge/DATA%20SCIENTIST-blue?style=for-the-badge)| <a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/mirna-prieto-990356242/">![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)
|**Edwin Garcia**|![](https://img.shields.io/badge/DATA%20SCIENTIST-blue?style=for-the-badge) | <a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/edd-garcia/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a> |
|**Juan Campos**|![](https://img.shields.io/badge/DATA%20SCIENTIST-blue?style=for-the-badge)| <a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/jumacaq/">[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jumacaq/)</a> |
|**Leopoldo Flores**|![](https://img.shields.io/badge/DATA%20SCIENTIST-blue?style=for-the-badge)| <a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/leopoldofloresc/">[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/leopoldofloresc/)</a> |
|**Alexangel Bracho**|![](https://img.shields.io/badge/DATA%20SCIENTIST-blue?style=for-the-badge)| <a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/alexangel-bracho-m-sc-in-physics-510675239/">[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alexangel-bracho-m-sc-in-physics-510675239/)</a> |



</div>
<br>




## <h2>🚧 Stack de Tecnologías </h2>

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Colab](https://img.shields.io/badge/Colab-F9AB00?style=flat&logo=google-colab&logoColor=white)](https://colab.research.google.com/)

[![Trello](https://img.shields.io/badge/Trello-0052CC?style=flat&logo=trello&logoColor=white)](https://trello.com/)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=flat&logo=discord&logoColor=white)](https://discord.com/)
