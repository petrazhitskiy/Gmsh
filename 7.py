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
from st_pages import Page, show_pages, add_page_title

st.sidebar.title("MATPLOTLIb")


st.title('Комбинирование графиков')

st.subheader('Размещение нескольких графиков на одной области (на одном рисунке).'
                 '\nВ Matplotlib мы можем нарисовать несколько графиков на одном графике двумя способами.'
                 'Один из них заключается в использовании функции subplot()'
                 ', а другой - в наложении второго графика на первый, т.е. все графики будут отображаться на одном графике.'
                 'Мы рассмотрим оба способа один за другим')


def plot_point():
    st.subheader('\nФункция subplot() - это функция, которая позволяет программисту построить более одного графика на одном рисунке.')

    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # Создание фигуры и осей с помощью subplot()
    fig, (ax1, ax2) = plt.subplots(2, 1)

    # Построение первого графика на первых осях
    ax1.plot(x, y1)
    ax1.set_title('График синуса')

    # Построение второго графика на вторых осях
    ax2.plot(x, y2)
    ax2.set_title('График косинуса')

    # Отображение графиков
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)

    code = """
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # Создание фигуры и осей с помощью subplot()
    fig, (ax1, ax2) = plt.subplots(2, 1)

    # Построение первого графика на первых осях
    ax1.plot(x, y1)
    ax1.set_title('График синуса')

    # Построение второго графика на вторых осях
    ax2.plot(x, y2)
    ax2.set_title('График косинуса')

    # Отображение графиков
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)
               """
    st.code(code, language='python')

def plot_point1():
    st.subheader('\nВ Matplotlib есть еще одна функция, очень похожая на subplot, которая называется subplot2grid ().'
                 'Это то же самое, что и функция subplot, но обеспечивает большую гибкость при расположении объектов графика в соответствии с потребностями программиста.')

    # Создание данных для графиков
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)


    fig = plt.figure()

    # Определение размеров и расположения графиков в сетке
    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
    ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
    ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
    ax4 = plt.subplot2grid((3, 3), (2, 0))
    ax5 = plt.subplot2grid((3, 3), (2, 1))

    # Построение графиков на каждой оси
    ax1.plot(x, y1)
    ax1.set_title('График 1')

    ax2.plot(x, y2)
    ax2.set_title('График 2')

    ax3.plot(x, y3)
    ax3.set_title('График 3')

    ax4.plot(x, y1 + y2)
    ax4.set_title('График 4')

    ax5.plot(x, y1 * y3)
    ax5.set_title('График 5')

    # Отображение графиков
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)


    code = """
           def plot_point1():
    # Создание данных для графиков
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)


    fig = plt.figure()

    # Определение размеров и расположения графиков в сетке
    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
    ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
    ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
    ax4 = plt.subplot2grid((3, 3), (2, 0))
    ax5 = plt.subplot2grid((3, 3), (2, 1))

    # Построение графиков на каждой оси
    ax1.plot(x, y1)
    ax1.set_title('График 1')

    ax2.plot(x, y2)
    ax2.set_title('График 2')

    ax3.plot(x, y3)
    ax3.set_title('График 3')

    ax4.plot(x, y1 + y2)
    ax4.set_title('График 4')

    ax5.plot(x, y1 * y3)
    ax5.set_title('График 5')

    # Отображение графиков
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)
    """
    st.code(code, language='python')

def plot_tor():
    st.subheader('\nВ этом методе мы не используем никаких специальных функций, вместо этого мы непосредственно строим кривые одна над другой на одном графике.')

    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)

    # Создание графика
    fig = plt.figure()

    # Построение кривых на одном графике
    plt.plot(x, y1, label='График 1')
    plt.plot(x, y2, label='График 2')
    plt.plot(x, y3, label='График 3')

    # Настройка осей и заголовка
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Несколько кривых на одном графике')

    # Добавление легенды
    plt.legend()

    # Отображение графика
    plt.show()
    st.pyplot(fig)

    code = """
    def plot_tor():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)

    # Создание графика
    fig = plt.figure()

    # Построение кривых на одном графике
    plt.plot(x, y1, label='График 1')
    plt.plot(x, y2, label='График 2')
    plt.plot(x, y3, label='График 3')

    # Настройка осей и заголовка
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Несколько кривых на одном графике')

    # Добавление легенды
    plt.legend()

    # Отображение графика
    plt.show()
    st.pyplot(fig)

               """
    st.code(code, language='python')
def main():


    # Выбор типа графика
    chart_type = st.sidebar.selectbox('Выберите тип графика', ['Функция subplots', 'Функция subplot2grid', 'Строим кривые одна над другой'])

    # Отображение соответствующего графика

    if chart_type == 'Функция subplots':
        plot_point()
    if chart_type == 'Функция subplot2grid':

        plot_point1()
    elif chart_type == 'Строим кривые одна над другой':
        plot_tor()





if __name__ == '__main__':
    main()







