import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time
import math
from datetime import time
import plotly.express as px
import datetime


st.sidebar.title("MATPLOTLIb")

st.title('Одномерные графики')


st.set_option('deprecation.showPyplotGlobalUse', False)

# Столбчатая диаграмма

def plot_bar():
    st.subheader('Простая столбчатая диаграмма')
    categories = ['Категория 1', 'Категория 2', 'Категория 3']
    values = [3, 7, 2]
    plt.bar(categories, values)
    st.pyplot()
    code = """
    categories = ['Категория 1', 'Категория 2', 'Категория 3']
    values = [3, 7, 2]
    plt.bar(categories, values)
    st.pyplot()
    """
    st.code(code, language='python')
    st.subheader('Добавление h к bar превращает диаграмму в горизонтальную')
    categories = ['Категория 1', 'Категория 2', 'Категория 3']
    values = [3, 7, 2]
    plt.barh(categories, values)
    st.pyplot()
    code = """c
    plt.barh(categories, values)
    """
    st.code(code, language='python')

    st.subheader('Для группировки двух наборов столбцов для каждой категории')
    values = [3, 7, 2]
    values2 = [4, 6, 8]
    categories = ['Категория 1', 'Категория 2', 'Категория 3']
    ind = np.arange(len(categories))  # создание массива индексов
    width = 0.35  # ширина столбцов
    plt.bar(ind - width / 2, values, width, label='Значения 1')
    plt.bar(ind + width / 2, values2, width, label='Значения 2')
    plt.xticks(ind, categories)
    plt.legend()
    st.pyplot()
    code = """
    values = [3, 7, 2]
    values2 = [4, 6, 8]
    categories = ['Категория 1', 'Категория 2', 'Категория 3']
    ind = np.arange(len(categories))  # создание массива индексов
    width = 0.35  # ширина столбцов
    plt.bar(ind - width / 2, values, width, label='Значения 1')
    plt.bar(ind + width / 2, values2, width, label='Значения 2')
    plt.xticks(ind, categories)
    plt.legend()
    st.pyplot()
    """
    st.code(code, language='python')

    st.subheader('Можно добавить код текстовых отметок над столбцами')
    plt.bar(categories, values)
    for i, value in enumerate(values):
        plt.text(i, value + 0.1, str(value), ha='center')
    st.pyplot()

    st.subheader('Настройка цвета, границы и толщины линии')
    plt.bar(categories, values, color='skyblue', edgecolor='black', linewidth=1.2)
    st.pyplot()
    code = """
        plt.bar(categories, values, color='skyblue', edgecolor='black', linewidth=1.2)
    """
    st.code(code, language='python')

    st.subheader('Диаграмма с накоплением второго набора значений поверх первого')
    values2 = [4, 6, 8]
    plt.bar(categories, values, label='Значения 1')
    plt.bar(categories, values2, bottom=values, label='Значения 2')
    plt.legend()
    st.pyplot()
    
    code = """
    plt.bar(categories, values, label='Значения 1')
    plt.bar(categories, values2, bottom=values, label='Значения 2')
    """
    st.code(code, language='python')


# Круговая диаграмма

def plot_pie():
    st.subheader('В этом коде sizes представляет собой значения для каждой категории, и autopct добавляет процентные значения.')
    labels = ['Категория 1', 'Категория 2', 'Категория 3']
    sizes = [30, 45, 25]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot()
    code = """
    labels = ['Категория 1', 'Категория 2', 'Категория 3']
    sizes = [30, 45, 25]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot()
    """
    st.code(code, language='python')

    st.subheader('Для выделения одного сектора')

    explode = (0, 0.1, 0)  # выделение второй категории
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode)
    st.pyplot()
    code = """
    labels = ['Категория 1', 'Категория 2', 'Категория 3']
    sizes = [30, 45, 25]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot()
    """
    st.code(code, language='python')
    st.subheader('Настройка цвета выполняется следующим образом')


    colors = ['gold', 'lightskyblue', 'lightcoral']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
    st.pyplot()
    code = """
    labels = ['Категория 1', 'Категория 2', 'Категория 3']
    colors = ['gold', 'lightskyblue', 'lightcoral']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
    st.pyplot()
    """
    st.code(code, language='python')
    st.subheader('Для выбора начала откладываемого угла ')

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    st.pyplot()
    code = """
     plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
     st.pyplot()
     """
    st.code(code, language='python')
    st.subheader('Код для построения диаграммы с отсечением ')

    explode = (0, 0.1, 0)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, wedgeprops=dict(width=0.3))
    st.pyplot()
    code = """
         explode = (0, 0.1, 0)
         plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, wedgeprops=dict(width=0.3))
         st.pyplot()
         """
    st.code(code, language='python')
    st.subheader('На график можно добавить тень ')

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
    st.pyplot()
    code = """
         plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
         st.pyplot()
         """
    st.code(code, language='python')
    st.subheader('Добавлять легенду можно при помощи следующего кода ')

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.legend(subheader='Категории', loc='upper right', bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot()
    code = """
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.legend(subheader='Категории', loc='upper right', bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot()
         """
    st.code(code, language='python')

# Точечный график
def plot_scatter():
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 5, 8, 2]
    plt.scatter(x, y)
    st.pyplot()
    code = """
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 5, 8, 2]
    plt.scatter(x, y)
    st.pyplot()
     """
    st.code(code, language='python')

    st.subheader('Настройка размера и цвета точек')

    sizes = [30, 80, 120, 200, 10]
    colors = ['red', 'green', 'blue', 'yellow', 'purple']
    plt.scatter(x, y, s=sizes, c=colors)
    st.pyplot()
    code = """
    sizes = [30, 80, 120, 200, 10]
    colors = ['red', 'green', 'blue', 'yellow', 'purple']
    plt.scatter(x, y, s=sizes, c=colors)
    st.pyplot()
     """
    st.code(code, language='python')

    st.subheader('Можно использовать цветовую карту')

    sizes = np.random.randint(10, 100, len(x))
    colors = np.random.rand(len(x), 3)
    plt.scatter(x, y, s=sizes, c=colors, cmap='viridis')
    plt.colorbar()
    st.pyplot()
    code = """
    sizes = np.random.randint(10, 100, len(x))
    colors = np.random.rand(len(x), 3)  
    plt.scatter(x, y, s=sizes, c=colors, cmap='viridis')
    plt.colorbar()
    st.pyplot()
     """
    st.code(code, language='python')

    st.subheader('Добавление подписей осуществляется следующим образом')

    labels = ['A', 'B', 'C', 'D', 'E']
    plt.scatter(x, y)
    for i, label in enumerate(labels):
     plt.annotate(label, (x[i], y[i]))
    st.pyplot()
    code = """
    labels = ['A', 'B', 'C', 'D', 'E']
    plt.scatter(x, y)
    for i, label in enumerate(labels):
    plt.annotate(label, (x[i], y[i]))
    st.pyplot()
     """
    st.code(code, language='python')

    st.subheader('Также на точечный график можно добавлять линии. Это осуществляется следующим образом')

    plt.scatter(x, y)
    plt.plot(x, y, linestyle='dashed', color='gray')
    st.pyplot()
    code = """
    plt.scatter(x, y)
    plt.plot(x, y, linestyle='dashed', color='gray')
    st.pyplot()
     """
    st.code(code, language='python')

    st.subheader('На точечном графике можно сразу работать с несколькими наборами данных')


    x2 = [1.5, 2.5, 3.5, 4.5, 5.5]
    y2 = [8, 3, 2, 7, 1]
    plt.scatter(x, y, label='Группа 1')
    plt.scatter(x2, y2, label='Группа 2', marker='^')
    plt.legend()
    st.pyplot()
    code = """
    x2 = [1.5, 2.5, 3.5, 4.5, 5.5]
    y2 = [8, 3, 2, 7, 1]
    plt.scatter(x, y, label='Группа 1')
    plt.scatter(x2, y2, label='Группа 2', marker='^')
    plt.legend()
    st.pyplot()
     """
    st.code(code, language='python')

def main():
    st.text('Двумерные графики бывают следующих видов: Столбчатые, Точечные, Круговые и т.д')
    st.text('Рассмотрим наиболее популярные из них:')

    # Выбор типа графика
    chart_type = st.sidebar.selectbox('Выберите тип графика', ['Столбчатый', 'Круговой', 'Точечный', ])

    # Отображение соответствующего графика

    if chart_type == 'Столбчатый':
        st.subheader('Библиотека matplotlib предоставляет множество возможностей для создания столбчатых диаграмм.')
        plot_bar()
    elif chart_type == 'Круговой':
        st.subheader('Круговые диаграммы в matplotlib можно создавать с использованием функции pie. Вот несколько примеров:')
        plot_pie()
    elif chart_type == 'Точечный':
        st.subheader('Точечные графики (scatter plots) в matplotlib могут быть созданы с использованием функции scatter. Вот несколько примеров:')
        plot_scatter()


st.set_option('deprecation.showPyplotGlobalUse', False)


# Заголовок презентации
st.subheader('Демонстрация библиотеки Matplotlib с помощью Streamlit')

# Столбчатая диаграмма

def plot_bar():
    st.subheader('Простая столбчатая диаграмма')
    categories = ['Категория 1', 'Категория 2', 'Категория 3']
    values = [3, 7, 2]
    plt.bar(categories, values)
    st.pyplot()
    code = """
    categories = ['Категория 1', 'Категория 2', 'Категория 3']
    values = [3, 7, 2]
    plt.bar(categories, values)
    st.pyplot()
    """
    st.code(code, language='python')
    st.subheader('Добавление h к bar превращает диаграмму в горизонтальную')
    categories = ['Категория 1', 'Категория 2', 'Категория 3']
    values = [3, 7, 2]
    plt.barh(categories, values)
    st.pyplot()
    code = """
    plt.barh(categories, values)
    """
    st.code(code, language='python')

    st.subheader('Для группировки двух наборов столбцов для каждой категории')
    values = [3, 7, 2]
    values2 = [4, 6, 8]
    categories = ['Категория 1', 'Категория 2', 'Категория 3']
    ind = np.arange(len(categories))  # создание массива индексов
    width = 0.35  # ширина столбцов
    plt.bar(ind - width / 2, values, width, label='Значения 1')
    plt.bar(ind + width / 2, values2, width, label='Значения 2')
    plt.xticks(ind, categories)
    plt.legend()
    st.pyplot()
    code = """
    values = [3, 7, 2]
    values2 = [4, 6, 8]
    categories = ['Категория 1', 'Категория 2', 'Категория 3']
    ind = np.arange(len(categories))  # создание массива индексов
    width = 0.35  # ширина столбцов
    plt.bar(ind - width / 2, values, width, label='Значения 1')
    plt.bar(ind + width / 2, values2, width, label='Значения 2')
    plt.xticks(ind, categories)
    plt.legend()
    st.pyplot()
    """
    st.code(code, language='python')

    st.subheader('Можно добавить код текстовых отметок над столбцами')
    plt.bar(categories, values)
    for i, value in enumerate(values):
        plt.text(i, value + 0.1, str(value), ha='center')
    st.pyplot()
    code = """
        for i, value in enumerate(values):
            plt.text(i, value + 0.1, str(value), ha='center')
        """
    st.code(code, language='python')

    st.subheader('Настройка цвета, границы и толщины линии')
    plt.bar(categories, values, color='skyblue', edgecolor='black', linewidth=1.2)
    st.pyplot()
    code = """
        plt.bar(categories, values, color='skyblue', edgecolor='black', linewidth=1.2)
    """
    st.code(code, language='python')

    st.subheader('Диаграмма с накоплением второго набора значений поверх первого')
    values2 = [4, 6, 8]
    plt.bar(categories, values, label='Значения 1')
    plt.bar(categories, values2, bottom=values, label='Значения 2')
    plt.legend()
    st.pyplot()
    code = """
    plt.bar(categories, values, label='Значения 1')
    plt.bar(categories, values2, bottom=values, label='Значения 2')
    """
    st.code(code, language='python')
# Круговая диаграмма

def plot_pie():
    st.subheader('В этом коде sizes представляет собой значения для каждой категории, и autopct добавляет процентные значения.')
    labels = ['Категория 1', 'Категория 2', 'Категория 3']
    sizes = [30, 45, 25]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot()
    code = """
    labels = ['Категория 1', 'Категория 2', 'Категория 3']
    sizes = [30, 45, 25]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot()
    """
    st.code(code, language='python')

    st.subheader('Для выделения одного сектора')

    explode = (0, 0.1, 0)  # выделение второй категории
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode)
    st.pyplot()
    code = """
    labels = ['Категория 1', 'Категория 2', 'Категория 3']
    sizes = [30, 45, 25]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot()
    """
    st.code(code, language='python')
    st.subheader('Настройка цвета выполняется следующим образом')


    colors = ['gold', 'lightskyblue', 'lightcoral']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
    st.pyplot()
    code = """
    labels = ['Категория 1', 'Категория 2', 'Категория 3']
    colors = ['gold', 'lightskyblue', 'lightcoral']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
    st.pyplot()
    """
    st.code(code, language='python')
    st.subheader('Для выбора начала откладываемого угла ')

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    st.pyplot()
    code = """
     plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
     st.pyplot()
     """
    st.code(code, language='python')
    st.subheader('Код для построения диаграммы с отсечением ')

    explode = (0, 0.1, 0)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, wedgeprops=dict(width=0.3))
    st.pyplot()
    code = """
         explode = (0, 0.1, 0)
         plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, wedgeprops=dict(width=0.3))
         st.pyplot()
         """
    st.code(code, language='python')
    st.subheader('На график можно добавить тень ')

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
    st.pyplot()
    code = """
         plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
         st.pyplot()
         """
    st.code(code, language='python')
    st.subheader('Добавлять легенду можно при помощи следующего кода ')

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.legend(title='Категории', loc='upper right', bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot()
    code = """
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.legend(title='Категории', loc='upper right', bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot()
         """
    st.code(code, language='python')

# Точечный график
def plot_scatter():
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 5, 8, 2]
    plt.scatter(x, y)
    st.pyplot()
    code = """
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 5, 8, 2]
    plt.scatter(x, y)
    st.pyplot()
     """
    st.code(code, language='python')

    st.subheader('Настройка размера и цвета точек')

    sizes = [30, 80, 120, 200, 10]
    colors = ['red', 'green', 'blue', 'yellow', 'purple']
    plt.scatter(x, y, s=sizes, c=colors)
    st.pyplot()
    code = """
    sizes = [30, 80, 120, 200, 10]
    colors = ['red', 'green', 'blue', 'yellow', 'purple']
    plt.scatter(x, y, s=sizes, c=colors)
    st.pyplot()
     """
    st.code(code, language='python')

    st.subheader('Можно использовать цветовую карту')

    sizes = np.random.randint(10, 100, len(x))
    colors = np.random.rand(len(x), 3)
    plt.scatter(x, y, s=sizes, c=colors, cmap='viridis')
    plt.colorbar()
    st.pyplot()
    code = """
    sizes = np.random.randint(10, 100, len(x))
    colors = np.random.rand(len(x), 3)  
    plt.scatter(x, y, s=sizes, c=colors, cmap='viridis')
    plt.colorbar()
    st.pyplot()
     """
    st.code(code, language='python')

    st.subheader('Добавление подписей осуществляется следующим образом')

    labels = ['A', 'B', 'C', 'D', 'E']
    plt.scatter(x, y)
    for i, label in enumerate(labels):
     plt.annotate(label, (x[i], y[i]))
    st.pyplot()
    code = """
    labels = ['A', 'B', 'C', 'D', 'E']
    plt.scatter(x, y)
    for i, label in enumerate(labels):
    plt.annotate(label, (x[i], y[i]))
    st.pyplot()
     """
    st.code(code, language='python')

    st.subheader('Также на точечный график можно добавлять линии. Это осуществляется следующим образом')

    plt.scatter(x, y)
    plt.plot(x, y, linestyle='dashed', color='gray')
    st.pyplot()
    code = """
    plt.scatter(x, y)
    plt.plot(x, y, linestyle='dashed', color='gray')
    st.pyplot()
     """
    st.code(code, language='python')

    st.subheader('На точечном графике можно сразу работать с несколькими наборами данных')


    x2 = [1.5, 2.5, 3.5, 4.5, 5.5]
    y2 = [8, 3, 2, 7, 1]
    plt.scatter(x, y, label='Группа 1')
    plt.scatter(x2, y2, label='Группа 2', marker='^')
    plt.legend()
    st.pyplot()
    code = """
    x2 = [1.5, 2.5, 3.5, 4.5, 5.5]
    y2 = [8, 3, 2, 7, 1]
    plt.scatter(x, y, label='Группа 1')
    plt.scatter(x2, y2, label='Группа 2', marker='^')
    plt.legend()
    st.pyplot()
     """
    st.code(code, language='python')

def main():


    st.subheader('Одномерные графики бывают следующих видов: Столбчатые, Точечные, Круговые и т.д')
    st.subheader('Рассмотрим наиболее популярные из них:')

    # Выбор типа графика
    chart_type = st.sidebar.selectbox('Выберите тип графика', ['Столбчатый', 'Круговой', 'Точечный', ])

    # Отображение соответствующего графика

    if chart_type == 'Столбчатый':
        st.subheader('Библиотека matplotlib предоставляет множество возможностей для создания столбчатых диаграмм.')
        plot_bar()
    elif chart_type == 'Круговой':
        st.subheader('Круговые диаграммы в matplotlib можно создавать с использованием функции pie. Вот несколько примеров:')
        plot_pie()
    elif chart_type == 'Точечный':
        st.subheader('Точечные графики (scatter plots) в matplotlib могут быть созданы с использованием функции scatter. Вот несколько примеров:')
        plot_scatter()


if __name__ == '__main__':
    main()