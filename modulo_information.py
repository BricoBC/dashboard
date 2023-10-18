# import pandas as pd
# import numpy as np

#Creo una función que me regresa todos los tema de una categoria
def filter_column(data, column_of_value, value, column_filter):
    """
    Se va a filtar todos los datos con respecto al valor de una columna proporcionada, 
    pero únicamente se va a mostrar los valores de la columna filtrada.
    ES NECESARIO QUE EN DATA SEA TODA LA TABLA DE LOS DATOS.
    COLUMN_OF_VALUE es únicamente el nombre la columna.
    COLUMN_FILTER es únicamente el nombre la columna.
    """
    arr_tema = data[ data[column_of_value] == value][column_filter].unique()
    return arr_tema

def every_data(data, name_column_category , category, name_column_tema, tema, name_column_values):
    """
    Se va a obtener el valor de TOTAL DE DATOS, DATOS CON INFORMACIÓN, DATOS SIN INFORMACIÓN, en este orden.
    """
    # Por medio del filtrado por dos columnas y los dos valores de éstas columnas, se va a contar el total de datos que se tuvo
    # después de éste total se va a evaluar cuántos no tienen datos y al final se restará con el total
    data_total = data[name_column_values].loc[(data[name_column_category] == category) & (data[name_column_tema] == tema)].size
    data_without_information = data_without_information = data[name_column_values].loc[(data[name_column_category] == category) & 
                                                                                  (data[name_column_tema] == tema) & 
                                                                                  (data[name_column_values] == 'No') ].count()
    data_information = data_total - data_without_information
    return data_total, data_without_information, data_information

def get_i(word, array):
    """
    Con base a un arreglo se buscará una paralabra y retornará la iteral de esa ubicación.
    """
    for i in range(array.size):
        if(word == array[i]):
            return i
    return -1
