import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch

def percentage(dashboard):
    """
    Función que regresa dos arrays, el porcentaje de los datos con información y sin información de un tema.
    """
    arr_percentage_without_information = []
    arr_percentage_with_information = []
    for i in range(len(dashboard['Datos'])):
        porcentaje_con_informacion = ((dashboard['Datos_con_informacion'][i]*100)/dashboard['Datos'][i])/100
        porcentaje_sin_informacion = (1-porcentaje_con_informacion)
        #print(porcentaje_con_informacion, porcentaje_sin_informacion) 
        arr_percentage_without_information.append(porcentaje_sin_informacion)
        arr_percentage_with_information.append(porcentaje_con_informacion)
    return arr_percentage_with_information, arr_percentage_without_information

def rotate_figure(i, arr):
    sum = 0
    if i<0:
        return sum    
    for j in range(len(arr)):
        if(i <= j):
            sum = sum + arr[j]*10
            return sum
        else:
            sum = sum + arr[j]*10
    return False

# make figure and assign axis objects
def bar_pie(dashboard):
    title = dashboard['Categoria']
    etiquetas = dashboard['Tema']
    valores = dashboard['Datos']
        # make figure and assign axis objects
    overall_ratios = valores
    labels = etiquetas
    explode = np.zeros(len(overall_ratios))

    for i in range(len(labels)):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        fig.subplots_adjust(wspace=.1)

        # pie chart parameters
        explode[i] = .1
        # rotate so that first wedge is split by the x-axis
        angle = - (3.6*rotate_figure(i-1,overall_ratios)/2) -(3.6*rotate_figure(i,overall_ratios) )/2 
        wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                            labels=labels, explode=explode)
        color_rebanada = wedges[i].get_facecolor()

        # bar chart parameters
        age_ratios = [percentage(dashboard)[0][i], percentage(dashboard)[1][i]]
        age_labels = ['Con información', 'Sin información']
        bottom = 1
        width = .1

        # Adding from the top matches the legend.
        for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
            bottom -= height
            bc = ax2.bar(0, height, width, bottom=bottom, color=color_rebanada, label=label,
                        alpha=0.25 + 0.50 * j)
            ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')

        source_info = ', '.join(map(str, dashboard['Source_information']))
        ax2.set_title(f"Fuente de información: {source_info}")
        ax2.legend()
        ax2.axis('off')
        ax2.set_xlim(- 2.5 * width, 2.5 * width)

        # use ConnectionPatch to draw lines between the two plots
        theta1, theta2 = wedges[i].theta1, wedges[i].theta2
        center, r = wedges[i].center, wedges[i].r
        bar_height = sum(age_ratios)

        # draw top connecting line
        x = r * np.cos(np.pi / 180 * theta2) + center[0]
        y = r * np.sin(np.pi / 180 * theta2) + center[1]
        con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                            xyB=(x, y), coordsB=ax1.transData)
        con.set_color([0, 0, 0])
        con.set_linewidth(4)
        ax2.add_artist(con)

        # draw bottom connecting line
        x = r * np.cos(np.pi / 180 * theta1) + center[0]
        y = r * np.sin(np.pi / 180 * theta1) + center[1]
        con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                            xyB=(x, y), coordsB=ax1.transData)
        con.set_color([0, 0, 0])
        ax2.add_artist(con)
        con.set_linewidth(4)


        plt.savefig(f'./images/Pastel-barras-{title}_{labels[i]}.png')
