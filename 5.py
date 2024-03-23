

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
import matplotlib.animation as animation


st.sidebar.title("MATPLOTLIb")

st.title('Двумерные графики')

st.set_option('deprecation.showPyplotGlobalUse', False)

def plot_linear(x_min, x_max, num_points, show_axis_labels, show_title, show_legend,
                         line_color, text, show_setka, font_size):
    x = np.linspace(x_min, x_max, num_points)
    y = x
    plt.plot(x, y)
    plt.title('Линейный график')


    fig, ax = plt.subplots()
    line, = ax.plot(x, y, color=line_color, label='Линия')
    if show_legend:
        ax.legend()
    if show_title:
        ax.set_title('Линейный график')
    if show_axis_labels:
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
    if show_setka:
        plt.grid()
        plt.show()

    line.set_color(line_color)
    ax.autoscale(enable=True, axis='both', tight=True)
    fig.set_size_inches(10, 6)
    ax.text(x_max * 0.5, 0.8, text, fontsize=font_size, ha='center', va='center')
    st.pyplot(fig)



    code = """
    x = np.linspace(0, 10, 100)
    y = x
    plt.plot(x, y)
    plt.title('Линейный график')
    st.pyplot()
    """
    st.code(code, language='python')


def plot_par(x_min, x_max, num_points, show_axis_labels, show_title, show_legend,
                     line_color, text, show_setka, font_size):
    x = np.linspace(x_min, x_max, num_points)
    y = x**2
    plt.plot(x, y, color='m', label='Парабола y=x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График параболы')

    fig, ax = plt.subplots()
    line, = ax.plot(x, y, color=line_color, label='Парабола')
    if show_legend:
        ax.legend()
    if show_title:
        ax.set_title('График параболы')
    if show_axis_labels:
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
    if show_setka:
        plt.grid()
        plt.show()

    line.set_color(line_color)
    ax.autoscale(enable=True, axis='both', tight=True)
    fig.set_size_inches(10, 6)
    ax.text(x_max * 0.5,  0.8, text, fontsize=font_size, ha='center', va='center')
    st.pyplot(fig)


    code = """
    x = np.linspace(-5, 5, 100)
    y = x**2
    plt.plot(x, y, color='m', label='Парабола y=x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График параболы')
    plt.legend()
    plt.grid(True)
    st.pyplot()
    """
    st.code(code, language='python')

def plot_ellipse(a_min, b_min, num_points, show_axis_labels, show_title, show_legend,
                     line_color, text, show_setka, font_size):

    a = a_min
    b = b_min
    t = np.linspace(0, 2 * np.pi, 100)
    x = a * np.cos(t)
    y = b * np.sin(t)
    plt.plot(x, y, label='Эллипс')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График эллипса')


    fig, ax = plt.subplots()
    line, = ax.plot(x, y, color=line_color, label='Эллипс')
    if show_legend:
        ax.legend()
    if show_title:
        ax.set_title('График эллипса')
    if show_axis_labels:
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
    if show_setka:
        plt.grid()
        plt.show()

    line.set_color(line_color)
    ax.autoscale(enable=True, axis='both', tight=True)
    fig.set_size_inches(10, 6)
    ax.text(0.5, 0.8, text, fontsize=font_size, ha='center', va='center')
    st.pyplot(fig)
    code = """
    a = 3.0
    b = 2.0
    t = np.linspace(0, 2 * np.pi, 100)
    x = a * np.cos(t)
    y = b * np.sin(t)

    plt.plot(x, y, label='Эллипс')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График эллипса')
    plt.axis('equal')
    plt.legend()
    plt.grid(True)
    st.pyplot()
    """
    st.code(code, language='python')


def plot_log(x_min, x_max, num_points, show_axis_labels, show_title, show_legend,
                     line_color, text, show_setka, font_size):
    x = np.linspace(x_min, x_max, num_points)
    y = np.log(x)
    plt.plot(x, y, color='g', label='Логарифмическая функция y=ln(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График логарифмической функции')

    fig, ax = plt.subplots()
    line, = ax.plot(x, y, color=line_color, label='Логарифмическая функция y=ln(x)')
    if show_legend:
        ax.legend()
    if show_title:
        ax.set_title('График логарифмической функции')
    if show_axis_labels:
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
    if show_setka:
        plt.grid()
        plt.show()

    line.set_color(line_color)
    ax.autoscale(enable=True, axis='both', tight=True)
    fig.set_size_inches(10, 6)
    ax.text(0.5, 0.8, text, fontsize=font_size, ha='center', va='center')
    st.pyplot(fig)

    code = """
    x = np.linspace(0.01, 2, 100)
    y = np.log(x)

    plt.plot(x, y, color='g', label='Логарифмическая функция y=ln(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График логарифмической функции')
    plt.legend()
    plt.grid(True)
    st.pyplot()
    """
    st.code(code, language='python')


def plot_animation():
    fig, ax = plt.subplots()
    x = np.arange(0, 2 * np.pi, 0.1)
    y = np.sin(x)

    sc = ax.scatter(x, y, c=x, cmap='hsv', s=100)

    def update(frame):
        sc.set_offsets(np.c_[x, np.sin(x + frame / 10.0)])
        sc.set_array(x + frame / 10.0)
        return sc,

    ani = animation.FuncAnimation(fig, update, frames=100, blit=True)
    plt.title('Пример диаграммы рассеяния с анимацией')
    st.pyplot()
    code = """
    fig, ax = plt.subplots()
    x = np.arange(0, 2 * np.pi, 0.1)
    y = np.sin(x)

    sc = ax.scatter(x, y, c=x, cmap='hsv', s=100)

    def update(frame):
        sc.set_offsets(np.c_[x, np.sin(x + frame / 10.0)])
        sc.set_array(x + frame / 10.0)
        return sc,

    ani = animation.FuncAnimation(fig, update, frames=100, blit=True)
    plt.title('Пример диаграммы рассеяния с анимацией')
    st.pyplot()
    """
    st.code(code, language='python')


def main():


    # Выбор типа графика
    chart_type = st.selectbox('Выберите тип графика', ['Линейный', 'Парабола', 'Эллипс', 'Логарифм', 'Рассеивание'])



    # Отображение соответствующего графика



    if chart_type == 'Линейный':


        x_min = st.sidebar.slider('Минимальное значение x', min_value=0, max_value=10, value=0)
        x_max = st.sidebar.slider('Максимальное значение x', min_value=10, max_value=20, value=10)
        num_points = st.sidebar.slider('Количество точек', min_value=100, max_value=1000, value=500)
        show_axis_labels = st.sidebar.checkbox('Показать подписи осей', value=True)
        show_title = st.sidebar.checkbox('Показать заголовок графика', value=True)
        show_legend = st.sidebar.checkbox('Показать леганду', value=True)
        show_setka = st.sidebar.checkbox('Показать сетку', value=True)
        line_color = st.sidebar.color_picker('Выберите цвет линии', '#ff5733')
        font_size = st.sidebar.slider('Размер шрифта', min_value=8, max_value=20, value=12)
        text = st.sidebar.text_input('Введите текст для добавления на график')

        plot_linear(x_min, x_max, num_points, show_axis_labels, show_title, show_legend,
                         line_color, text, show_setka, font_size)

    elif chart_type == 'Парабола':

        x_min = st.sidebar.slider('Минимальное значение x', min_value=-20, max_value=0, value=-10)
        x_max = st.sidebar.slider('Максимальное значение x', min_value=0, max_value=20, value=10)
        num_points = st.sidebar.slider('Количество точек', min_value=100, max_value=1000, value=500)

        show_axis_labels = st.sidebar.checkbox('Показать подписи осей', value=True)
        show_title = st.sidebar.checkbox('Показать заголовок графика', value=True)
        show_legend = st.sidebar.checkbox('Показать леганду', value=True)
        show_setka = st.sidebar.checkbox('Показать сетку', value=True)
        line_color = st.sidebar.color_picker('Выберите цвет линии', '#ff5733')
        font_size = st.sidebar.slider('Размер шрифта', min_value=8, max_value=20, value=12)
        text = st.sidebar.text_input('Введите текст для добавления на график')

        plot_par(x_min, x_max, num_points, show_axis_labels, show_title, show_legend,
                         line_color, text, show_setka, font_size)
    elif chart_type == 'Эллипс':

        a_min = st.sidebar.slider('Значение а', min_value=-10, max_value=10, value=3)

        b_min = st.sidebar.slider('Значение b', min_value=-10, max_value=10, value=2)

        num_points = st.sidebar.slider('Количество точек', min_value=100, max_value=1000, value=500)
        show_axis_labels = st.sidebar.checkbox('Показать подписи осей', value=True)
        show_title = st.sidebar.checkbox('Показать заголовок графика', value=True)
        show_legend = st.sidebar.checkbox('Показать леганду', value=True)
        show_setka = st.sidebar.checkbox('Показать сетку', value=True)
        line_color = st.sidebar.color_picker('Выберите цвет линии', '#ff5733')
        font_size = st.sidebar.slider('Размер шрифта', min_value=8, max_value=20, value=12)
        text = st.sidebar.text_input('Введите текст для добавления на график')

        plot_ellipse(a_min, b_min, num_points, show_axis_labels, show_title, show_legend,
                 line_color, text, show_setka, font_size)


    elif chart_type == 'Логарифм':

        x_min = st.sidebar.slider('Минимальное значение x', min_value=-20, max_value=0, value=-10)
        x_max = st.sidebar.slider('Максимальное значение x', min_value=0, max_value=20, value=10)
        num_points = st.sidebar.slider('Количество точек', min_value=100, max_value=1000, value=500)

        show_axis_labels = st.sidebar.checkbox('Показать подписи осей', value=True)
        show_title = st.sidebar.checkbox('Показать заголовок графика', value=True)
        show_legend = st.sidebar.checkbox('Показать леганду', value=True)
        show_setka = st.sidebar.checkbox('Показать сетку', value=True)
        line_color = st.sidebar.color_picker('Выберите цвет линии', '#ff5733')
        font_size = st.sidebar.slider('Размер шрифта', min_value=8, max_value=20, value=12)
        text = st.sidebar.text_input('Введите текст для добавления на график')

        plot_log(x_min, x_max, num_points, show_axis_labels, show_title, show_legend,
                 line_color, text, show_setka, font_size)
    elif chart_type == 'Рассеивание':
        plot_animation()




if __name__ == '__main__':
    main()