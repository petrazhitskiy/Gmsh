


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
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go

st.set_option('deprecation.showPyplotGlobalUse', False)


st.sidebar.title("MATPLOTLIb")

st.title('Сложные визуализации')

def plot_rgbf():
    def function(x, y):
        return np.sin(np.sqrt(x**2 + y**2))

    x = np.linspace(-10, 10, 40)
    y = np.linspace(-10, 10, 40)

    X, Y = np.meshgrid(x, y)
    Z = function(X, Y)

    fig = plt.figure(figsize=(10, 8))
    ax = plt.axes(projection='3d')

    ax.plot_surface(X, Y, Z, cmap='cool', alpha=0.8)

    ax.set_title('График функции f(x, y) =\
                    sin(sqrt(x^2 + y^2))', fontsize=14)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_zlabel('z', fontsize=12)
    st.pyplot()

    code = """
            def plot_rgbf():
    def function(x, y):
        return np.sin(np.sqrt(x**2 + y**2))

    x = np.linspace(-10, 10, 40)
    y = np.linspace(-10, 10, 40)

    X, Y = np.meshgrid(x, y)
    Z = function(X, Y)

    fig = plt.figure(figsize=(10, 8))
    ax = plt.axes(projection='3d')

    ax.plot_surface(X, Y, Z, cmap='cool', alpha=0.8)

    ax.set_title('График функции f(x, y) =\
                    sin(sqrt(x^2 + y^2))', fontsize=14)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_zlabel('z', fontsize=12)
    st.pyplot()
           """
    st.code(code, language='python')

def plot_mebius():
    R = 2

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(-1, 1, 100)
    u, v = np.meshgrid(u, v)
    x = (R + v * np.cos(u / 2)) * np.cos(u)
    y = (R + v * np.cos(u / 2)) * np.sin(u)
    z = v * np.sin(u / 2)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    ax.plot_surface(x, y, z, alpha=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Лента Мебиуса')

    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])
    st.pyplot()

    code = """
       def plot_mebius():
    R = 2

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(-1, 1, 100)
    u, v = np.meshgrid(u, v)
    x = (R + v * np.cos(u / 2)) * np.cos(u)
    y = (R + v * np.cos(u / 2)) * np.sin(u)
    z = v * np.sin(u / 2)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    ax.plot_surface(x, y, z, alpha=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Лента Мебиуса')

    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])
    st.pyplot()
       """
    st.code(code, language='python')

def plot_plt_dynamic():

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    surf = ax.plot_surface(x, y, z, cmap='viridis')

    for angle in range(0, 20, 10):
        ax.view_init(30, angle)
        st.pyplot(fig)  # отображение графика внутри окна приложения
        st.write("Angle:", angle)

    code = """
        def plot_plt_dynamic():
    def dynamic_3d_plot():
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        x, y = np.meshgrid(x, y)
        z = np.sin(np.sqrt(x**2 + y**2))

        surf = ax.plot_surface(x, y, z, cmap='viridis')

        for angle in range(0, 20, 10):
            ax.view_init(30, angle)
            st.pyplot(fig)  # отображение графика внутри окна приложения
            st.write("Angle:", angle)
           """
    st.code(code, language='python')

def plot_graph():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
    fig.update_layout(scene=dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z'),
                    width=800, height=700,
                    margin=dict(l=65, r=50, b=65, t=90))

    st.plotly_chart(fig)

    code = """
def plot_graph():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
    fig.update_layout(scene=dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z'),
                    width=800, height=700,
                    margin=dict(l=65, r=50, b=65, t=90))

    st.plotly_chart(fig)           """
    st.code(code, language='python')

def plot_tor_dynamic():
    # Параметры тора
    R = 1
    r = 0.3
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    u, v = np.meshgrid(u, v)
    x = (R + r * np.cos(v)) * np.cos(u)
    y = (R + r * np.cos(v)) * np.sin(u)
    z = r * np.sin(v)

    # Создаем 3D-график тора
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])
    fig.update_layout(scene=dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z'),
                    width=800, height=700,
                    margin=dict(l=65, r=50, b=65, t=90))

    # Отображаем график в приложении Streamlit
    st.plotly_chart(fig)

    code = """
        def plot_tor_dynamic():
    # Параметры тора
    R = 1
    r = 0.3
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    u, v = np.meshgrid(u, v)
    x = (R + r * np.cos(v)) * np.cos(u)
    y = (R + r * np.cos(v)) * np.sin(u)
    z = r * np.sin(v)

    # Создаем 3D-график тора
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])
    fig.update_layout(scene=dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z'),
                    width=800, height=700,
                    margin=dict(l=65, r=50, b=65, t=90))

    # Отображаем график в приложении Streamlit
    st.plotly_chart(fig)
           """
    st.code(code, language='python')

def plot_spiral():
    fig = plt.figure()

    # syntax for 3-D projection
    ax = plt.axes(projection='3d')

    # defining all 3 axis
    z = np.linspace(0, 1, 100)
    x = z * np.sin(25 * z)
    y = z * np.cos(25 * z)

    # plotting
    ax.plot3D(x, y, z, 'green')
    st.pyplot()

    fig = plt.figure()

    # syntax for 3-D projection
    ax = plt.axes(projection='3d')
    # defining axes
    z = np.linspace(0, 1, 100)
    x = z * np.sin(25 * z)
    y = z * np.cos(25 * z)
    c = x + y
    ax.scatter(x, y, z, c=c)

    # syntax for plotting
    st.pyplot()

def plot_grid():
    # function for z axis
    def f(x, y):
        return np.sin(np.sqrt(x**2 + y**2))

    # x and y axis
    x = np.linspace(-1, 5, 10)
    y = np.linspace(-1, 5, 10)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)


    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_wireframe(X, Y, Z, color='green')
    ax.set_title('wireframe geeks for geeks')
    st.pyplot()



def main():


    # Выбор типа графика
    chart_type = st.selectbox('Выберите тип графика', ['График','Лента Мебиуса','Динамика Matplotlib','Динамика', 'Тор'])

    # Отображение соответствующего графика

    if chart_type == 'График':
        plot_rgbf()
    elif chart_type == 'Лента Мебиуса':
        plot_mebius()
    elif chart_type == 'Динамика Matplotlib':
        plot_plt_dynamic()
    elif chart_type == 'Динамика':
        plot_graph()
    elif chart_type == 'Тор':
        plot_tor_dynamic()

if __name__ == '__main__':
    main()