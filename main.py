
def temas(category):
    """
    Está función es para obtener todos los temas en forma de un arreglo que contenga la categoria enviada en el parametro.
    """
    df_data[df_data['CATEGORIA'] == category]
    arr_tema = df_data[df_data['CATEGORIA'] == category]['TEMA'].unique()
    return arr_tema

def data(category, tema):
    """
    Esta función es para obtener los datos totales, los datos con información y los datos sin información.
    Se necesita enviar como parametro la categoria y el tema.
    """
    data_total = df_data['¿Se tiene?'].loc[(df_data['CATEGORIA'] == category) & (df_data['TEMA'] == tema)].size
    data_without_information = df_data['Campo agregado'].loc[(df_data['CATEGORIA'] == category) & (df_data['TEMA'] == tema) & (df_data['¿Se tiene?'] == 'No')].count()
    data_information = data_total - data_without_information
    return data_total, data_without_information, data_information

def source_information(category):
    """
    Esta función es para obtener la fuente de información de todos los temas que tiene la categoria.
    """
    source_information = df_data['ORIGEN'].loc[(df_data['CATEGORIA'] == category)].unique()
    return source_information


if __name__ == "__main__":
    import pandas as pd
    dashboard = {
        "Categoria": "",
        "Tema": [],
        "Datos": [],
        "Datos_con_informacion": [],
        "Datos_sin_informacion": [],
        "Source_information": ""
    }
    df_data_all = pd.read_csv("./KPIs.csv")
        # Elimino las últimas tres columnas
    df_data = df_data_all.iloc[ : , :-3]
        #Todas las Categorias
    categories = df_data['CATEGORIA'].unique()
    print(categories)

    category = categories[1]
    arr_datos, arr_without_data, arr_with_data = 0,0,0

    dashboard['Categoria'] = category
    theme = temas(category)

    dashboard['Tema'] = theme
    for j in range(theme.size):
        dashboard['Datos'].append(data(category, theme[j])[0])
        dashboard['Datos_sin_informacion'].append(data(category, theme[j])[1])
        dashboard['Datos_con_informacion'].append(data(category, theme[j])[2])
    dashboard['Source_information'] = source_information(category)

    print(dashboard)

    
