



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

st.set_option('deprecation.showPyplotGlobalUse', False)


st.sidebar.title("MATPLOTLIb")

st.title('3D Графики')
def plot_point(num_points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.random.standard_normal(num_points)
    y = np.random.standard_normal(num_points)
    z = np.random.standard_normal(num_points)

    ax.scatter(x, y, z, c='r', marker='o')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.title('Пример 3D-графика')
    st.pyplot()

    code = """
            fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.random.standard_normal(num_points)
    y = np.random.standard_normal(num_points)
    z = np.random.standard_normal(num_points)

    ax.scatter(x, y, z, c='r', marker='o')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.title('Пример 3D-графика')
    st.pyplot()
        """
    st.code(code, language='python')

def plot_tor():
    u, v = np.mgrid[0:2 * np.pi:30j, 0:2 * np.pi:30j]
    x = (2 + np.sin(v)) * np.cos(u)
    y = (2 + np.sin(v)) * np.sin(u)
    z = np.cos(v)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_zlim(-2, 2)
    ax.plot_surface(x, y, z, cmap='inferno')
    st.pyplot()

    code = """
            u, v = np.mgrid[0:2 * np.pi:30j, 0:2 * np.pi:30j]
    x = (2 + np.sin(v)) * np.cos(u)
    y = (2 + np.sin(v)) * np.sin(u)
    z = np.cos(v)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_zlim(-2, 2)
    ax.plot_surface(x, y, z, cmap='inferno')
    st.pyplot()
        """
    st.code(code, language='python')

def plot_graph(x_min, x_max, num_points):


    fig = plt.figure()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(x_min, x_max, num_points)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    st.pyplot()

    code = """
            fig = plt.figure()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(x_min, x_max, num_points)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    st.pyplot()
        """
    st.code(code, language='python')

def plot_graph_z():
    fig = plt.figure()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    st.pyplot()

    code = """
            fig = plt.figure()
    fig, ax = plt.subplots(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    st.pyplot()
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

    code = """
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
        """
    st.code(code, language='python')

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

    code = """
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
        """
    st.code(code, language='python')

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
    ax.set_title('Сетка')
    st.pyplot()

    code = """
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
    ax.set_title('Сетка')
    st.pyplot()
        """
    st.code(code, language='python')



def main():


    # Выбор типа графика
    chart_type = st.selectbox('Выберите тип графика', ['Точки','Тор','График', 'Спираль','Сетка'])

    # Отображение соответствующего графика

    if chart_type == 'Точки':

        num_points = st.sidebar.slider('Количество точек', min_value=10, max_value=100, value=50)
        plot_point(num_points)
    elif chart_type == 'Тор':
        plot_tor()
    elif chart_type == 'График':


        x_min = st.sidebar.slider('Минимальное значение x', min_value=-20, max_value=0, value=-10)
        x_max = st.sidebar.slider('Максимальное значение x', min_value=0, max_value=20, value=10)
        num_points = st.sidebar.slider('Количество точек', min_value=100, max_value=1000, value=500)

        plot_graph(x_min, x_max, num_points)
    elif chart_type == 'Спираль':
        plot_spiral()
    elif chart_type == 'Сетка':
        plot_grid()

if __name__ == '__main__':
    main()