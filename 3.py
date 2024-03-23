
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


st.title('Элементы оформления')

# Подписи осей


def plot_sinus_graph(x_min, x_max, num_points, amplitude, frequency, show_axis_labels, show_title, show_legend,
                     line_color, text, show_setka, font_size):
    x = np.linspace(x_min, x_max, num_points)
    y = amplitude * np.sin(frequency * x)

    fig, ax = plt.subplots()
    line, = ax.plot(x, y, color=line_color, label='Синусоида sin(x)')
    if show_legend:
        ax.legend()
    if show_title:
        ax.set_title('График синусоиды')
    if show_axis_labels:
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
    if show_setka:
        plt.grid()
        plt.show()

    line.set_color(line_color)
    ax.autoscale(enable=True, axis='both', tight=True)
    fig.set_size_inches(10, 6)
    ax.text(x_max * 0.5, amplitude * 0.8, text, fontsize=font_size, ha='center', va='center')
    st.pyplot(fig)

    st.subheader("Данная строчка кода являестя пользовательской фунцией, которая получает значения из checkbox-ов, представленных слева, и строит график с заданными параметрами")
    code = """
        plot_sinus_graph(x_min, x_max, num_points, amplitude, frequency, show_axis_labels,
         show_title, show_legend, line_color, text, show_setka, font_size)
        """
    st.code(code, language='python')

    st.subheader("Код данной функции")
    code = """
            def plot_sinus_graph(x_min, x_max, num_points, amplitude, frequency, show_axis_labels, show_title, show_legend,
                     line_color, text, show_setka, font_size):
    x = np.linspace(x_min, x_max, num_points)
    y = amplitude * np.sin(frequency * x)

    fig, ax = plt.subplots()
    line, = ax.plot(x, y, color=line_color, label='Синусоида')
    if show_legend:
        ax.legend()
    if show_title:
        ax.set_title('График синусоиды')
    if show_axis_labels:
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
    if show_setka:
        plt.grid()
        plt.show()

    line.set_color(line_color)
    ax.autoscale(enable=True, axis='both', tight=True)
    fig.set_size_inches(7, 10)
    ax.text(x_max * 0.5, amplitude * 0.8, text, fontsize=font_size, ha='center', va='center')
    st.pyplot(fig)
            """
    st.code(code, language='python')



def main():
    x_min = st.sidebar.slider('Минимальное значение x', min_value=0, max_value=10, value=0)
    x_max = st.sidebar.slider('Максимальное значение x', min_value=10, max_value=20, value=10)
    num_points = st.sidebar.slider('Количество точек', min_value=100, max_value=1000, value=500)
    amplitude = st.sidebar.slider('Амплитуда', min_value=1, max_value=10, value=1)
    frequency = st.sidebar.slider('Частота', min_value=1, max_value=10, value=1)
    show_axis_labels = st.sidebar.checkbox('Показать подписи осей', value=True)
    show_title = st.sidebar.checkbox('Показать заголовок графика', value=True)
    show_legend = st.sidebar.checkbox('Показать легенду', value=True)
    show_setka = st.sidebar.checkbox('Показать сетку', value=True)
    line_color = st.sidebar.color_picker('Выберите цвет линии', '#ff5733')
    font_size = st.sidebar.slider('Размер шрифта', min_value=8, max_value=20, value=12)
    text = st.sidebar.text_input('Введите текст для добавления на график')



    plot_sinus_graph(x_min, x_max, num_points, amplitude, frequency, show_axis_labels, show_title, show_legend,
                     line_color, text, show_setka, font_size)


if __name__ == '__main__':
    main()





