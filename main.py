import modulo_information as m_info

if __name__ == "__main__":
    import pandas as pd
    import numpy as np
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
    # Le doy formato a los campos que tienen Si para que sean Sí
    df_data.loc[df_data['¿Se tiene?'] == 'Si' , '¿Se tiene?'] = 'Sí'
    df_data.loc[df_data['Campo agregado'] == 'Si' , 'Campo agregado'] = 'Sí'

        #Todas las Categorias
    categories = df_data['CATEGORIA'].unique()
    print(categories)

    category = categories[1]
    arr_datos, arr_without_data, arr_with_data = 0,0,0

    #GET CATEGORIA
    dashboard['Categoria'] = category
    
    #GET TEMA
    theme = m_info.filter_column(df_data,'CATEGORIA', category, 'TEMA')
    dashboard['Tema'] = theme
    
    arr_total_datos = []
    arr_sin_datos = []
    arr_con_datos = []
    for j in range(theme.size):
        arr_total_datos.append(m_info.every_data(df_data, 'CATEGORIA', category, 'TEMA', theme[j], '¿Se tiene?' )[0])

        i = m_info.get_i('Sí', m_info.every_data(df_data, 'CATEGORIA', category, 'TEMA', theme[j], '¿Se tiene?' )[1])
        # Operación ternaria donde si nos devuelve un True es porque no existe esa palabra por ende el valor es 0, 
        # en caso de que devuelva la iteral esa la usamos para el array de m_info.every_data

        value = 0 if i == -1 else m_info.every_data(df_data, 'CATEGORIA', category, 'TEMA', theme[j], '¿Se tiene?' )[2][i]
        arr_con_datos.append(value)

        i = m_info.get_i('No', m_info.every_data(df_data, 'CATEGORIA', category, 'TEMA', theme[j], '¿Se tiene?' )[1])
        value = 0 if i == -1 else m_info.every_data(df_data, 'CATEGORIA', category, 'TEMA', theme[j], '¿Se tiene?' )[2][i]
        arr_sin_datos.append(value)
        print()
    dashboard['Datos'] = arr_total_datos
    dashboard['Datos_con_informacion'] = arr_con_datos
    dashboard['Datos_sin_informacion'] = arr_sin_datos


    #GET FUENTE DE INFORMACIÓN
    dashboard['Source_information'] = m_info.filter_column(df_data,'CATEGORIA', category, 'ORIGEN')

    print(dashboard)

    

