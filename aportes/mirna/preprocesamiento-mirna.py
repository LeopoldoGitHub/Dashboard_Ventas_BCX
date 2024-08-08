def preprocesamiento():
    global df_itens_pedidos_copy, df_pedidos_copy, df_productos_copy, df_vendedores_copy, df_final
    estados = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}
    #Eliminar datos nulos de los 4 dataframes
    df_itens_pedidos_copy.dropna(inplace=True)
    df_pedidos_copy.dropna(inplace=True)
    df_productos_copy.dropna(inplace=True)
    df_vendedores_copy.dropna(inplace=True)
    #Cambiar tipo de dato de columna 'fecha_compra' en el dataframe df_pedidos_copy
    df_pedidos_copy['fecha_compra'] = pd.to_datetime(df_pedidos_copy['fecha_compra'])
    #Crear una nueva columna 'codigo_estado' en el dataframe df_itens_pedidos_copy donde extraemos los codigos de cada estado
    df_itens_pedidos_copy['codigo_estado'] = df_itens_pedidos_copy['ciudad'].str.split('-').str[1]
    #Crear una nueva columna 'nombre-estado' en el dataframe df_itens_pedidos_copy con el nombre completo de cada estado usando el diccionario 'estados'
    df_itens_pedidos_copy['nombre_estado'] = df_itens_pedidos_copy['codigo_estado'].map(estados)
    #Crear una nueva columna 'tipo_producto' en el dataframe df_productos_copy conteniendo la primera palabra en df_productos.producto
    df_productos_copy['tipo_producto'] = df_productos_copy['producto'].str.split().str[0]

    #Unir todos los dataframes en uno solo df_final
    merged1 = pd.merge(df_itens_pedidos_copy, df_pedidos_copy, on=['producto_id', 'pedido_id'])
    merged2 = pd.merge(merged1, df_productos_copy, on='producto_id')
    df_final = pd.merge(merged2, df_vendedores_copy, on='vendedor_id')

    return df_final

#Llama la funcion preproceso para crear df_final
df_final = preprocesamiento()