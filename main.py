import modulo_information as m_info
import graphics as fig

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

    #GET CATEGORIA
    dashboard['Categoria'] = category
    
    #GET TEMA
    theme = m_info.filter_column(df_data,'CATEGORIA', category, 'TEMA')
    dashboard['Tema'] = theme
    
    arr_total_datos = []
    arr_sin_datos = []
    arr_con_datos = []
    for j in range(theme.size):
            # Cómo se tiene el tema de una categoria se empieza a coleccionar en un arreglo los
            # datos totales, datos con información y datos sin información de cada tema.
            # Tiene su propio array cada dato obtenido.
            all_data = m_info.every_data(df_data, 'CATEGORIA', category, 'TEMA', theme[j], '¿Se tiene?' )

            arr_total_datos.append(all_data[0])
            arr_con_datos.append(all_data[2])
            arr_sin_datos.append(all_data[1])
        
    dashboard['Datos'] = arr_total_datos
    dashboard['Datos_con_informacion'] = arr_con_datos
    dashboard['Datos_sin_informacion'] = arr_sin_datos


    #GET FUENTE DE INFORMACIÓN
    dashboard['Source_information'] = m_info.filter_column(df_data,'CATEGORIA', category, 'ORIGEN')

    print(dashboard)

    print("Creando las imagenes")
    fig.bar_pie(dashboard)
    print(f"Se termino de crear las imagenes de {dashboard['Categoria']}")


    

