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
    Se va a obtener el total de datos, cuántos datos se tiene y cuantos no, esto mediante un filtrado de todos los datos (data) 
    mediante las columnas de la categoria y del tema en donde se indicará cuál es la categoria y el tema para hacer el filtrado. 
    Una vez hecho esa filtración sólo se va a obtener la columna indicada en 'name_column_values' para determinar el tamaño de los datos
    y de estos datos cuántos tienen Sí y cuántos No.
    """
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
    for i in range(len(array)):
        if(word == array[i]):
            return i
    return -1
