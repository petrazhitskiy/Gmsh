import streamlit as st
import datetime
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import gmsh
import meshio
import pyvista as pv
from st_pages import Page, show_pages, add_page_title
from stpyvista import stpyvista
import subprocess
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def plot_mesh(mesh_file):
    # Визуализация с помощью pyvista
    mesh = pv.read(mesh_file)
    plotter = pv.Plotter()
    plotter.add_mesh(mesh, show_edges=True, color=True)  # Отображение сетки в белом цвете
    # Вывод графика pyvista в streamlit
    plotter.view_isometric()
    stpyvista(plotter)

def union():

    st.subheader('___')
    width = st.slider("Ширина ", 0.01, 5.0, 2.0, key='sl01')
    height = st.slider("Высота", 0.01, 5.0, 2.0, key='sl02')
    mesh_size = st.slider("Размер сетки", 0.01, 0.5, 0.01, key='sl03')

    # Пример использования для визуализации круглой и треугольной сеток
    b1 = st.button("Сгенерировать", key='bt1')
    if b1:
        mesh_file = "union_mesh6.msh"
        subprocess.run(["python3", "generate_mesh6.py", str(1), str(1), str(1), mesh_file])
        plot_mesh(mesh_file)


def diff():
    st.subheader('___')
    st.subheader('___')
    width = st.slider("Ширина ", 0.01, 5.0, 2.0, key='sl21')
    height = st.slider("Высота", 0.01, 5.0, 2.0, key='sl22')
    mesh_size = st.slider("Размер сетки", 0.01, 0.5, 0.01, key='sl23')

    # Пример использования для визуализации круглой и треугольной сеток
    b2 =st.button("Сгенерировать", key = 'bt2')
    if b2:
        mesh_file = "diff_mesh6.msh"
        subprocess.run(["python3", "generate_mesh6.py", str(1), str(1), str(1), mesh_file])
        plot_mesh(mesh_file)

def inter():
    st.subheader('___')
    width = st.slider("Ширина ", 0.01, 5.0, 2.0, key='sl31')
    height = st.slider("Высота", 0.01, 5.0, 2.0, key='sl32')
    mesh_size = st.slider("Размер сетки", 0.01, 0.5, 0.01, key='sl33')

    # Пример использования для визуализации круглой и треугольной сеток
    b3 = st.button("Сгенерировать", key='bt3')
    if b3:
        mesh_file = " intersec_mesh.msh"
        subprocess.run(["python3", "generate_mesh6.py", str(1), str(1), str(1), mesh_file])
        plot_mesh(mesh_file)

def main():
    st.title("Составные области")

    st.title('')
    r'''В GMSH вы можете создавать различные составные области, 
    объединяя более простые геометрические фигуры
    Некоторые из типов составных областей, которые вы можете создать в GMSH, включают:'''

    st.subheader('1. Объединение (Union): ')

    r''' Объединение нескольких геометрических фигур 
    (например, прямоугольника и круга), чтобы создать одну область
    '''

    st.subheader('2. Вычитание (Subtraction): ')

    r'''Создание составной области путем вычитания одной геометрической фигуры из другой 
    (например, вырезание круглого отверстия из прямоугольной пластины)'''

    st.subheader('3. Пересечение (Intersection): ')

    r'''Создание области, образованной общей частью нескольких геометрических фигур.'''

    st.subheader('4. Объединение с дыркой (Union with Hole): ')

    r'''Создание области с отверстием, путем объединения двух фигур и вырезания отверстия из одной из них.'''


    union()
    diff()
    inter()


if __name__ == '__main__':
    main()



# def visual():
#     st.header("Заголовок 1 уровня")  # Заголовок
#     st.subheader("Заголовок 2 уровня")  # Заголовок поменьше
#     # Загрузка файла .msh в pyvista
#     mesh = pv.read('gmsh_test6.msh')
#     # Визуализация с помощью pyvista
#     plotter = pv.Plotter()
#     plotter.add_mesh(mesh,show_edges=True, color=True)  # Отображение сетки в белом цвете
#     # Вывод графика pyvista в streamlit
#     plotter.view_isometric()
#     stpyvista(plotter)
#     mesh = meshio.read('gmsh_test6.msh')
#     # Отображение данных с помощью matplotlib
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.plot_trisurf(mesh.points[:, 0], mesh.points[:, 1], mesh.points[:, 2], triangles=mesh.cells[1].data)
#
#     # Загрузка файла .msh в pyvista
#     # Вывод matplotlib streamlit
#     st.pyplot(fig)
#     gmsh.finalize()

