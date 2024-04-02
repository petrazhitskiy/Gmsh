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
    plotter.add_mesh(mesh, show_edges=True, color=True)
    # Вывод графика pyvista в streamlit
    plotter.view_isometric()
    stpyvista(plotter)

def union():

    st.subheader('___')
    # width_u1 = st.slider("Ширина ", 0.5, 5.0, 2.0, key='sl01')
    col1, col2 = st.columns(2)
    with col1:
        st.header("Основная фигура")
        figure_type_1 = st.selectbox("Выбирите тип фигуры:", ["Окружность", "Прямоугольник"], key = 'sel01')
        width_u1 = st.slider("Ширина ", 0.5, 5.0, 2.0, key='sl01')
        height_u1 = st.slider("Высота", 0.5, 5.0, 2.0, key='sl02')
        st.write(figure_type_1)
    with col2:
        st.header("Что добавляем")
        figure_type_2 = st.selectbox("Выбирите тип фигуры:", ["Окружность", "Прямоугольник"], key = 'sel02')
        width_u2 = st.slider("Ширина ", 0.5, 5.0, 2.0, key='sl11')
        height_u2 = st.slider("Высота", 0.5, 5.0, 2.0, key='sl12')

    # mesh_size_u = st.slider("Размер сетки", 0.01, 0.5, 0.01, key='sl03')
    b1 = st.button("Сгенерировать", key='bt1')
    if b1:
        mesh_file = "union_mesh6.msh"
        subprocess.run(["python3", "generate_mesh6.py",mesh_file,  str(width_u1),str(height_u1), str(width_u2),str(height_u2), figure_type_1, figure_type_2])# str(height_u1), str(width_u2), str(height_u2)
        plot_mesh(mesh_file)


def diff():
    st.subheader('___')
    width_d = st.slider("Ширина ", 0.01, 5.0, 2.0, key='sl21')
    # height_d = st.slider("Высота", 0.01, 5.0, 2.0, key='sl22')
    # mesh_size_d = st.slider("Размер сетки", 0.01, 0.5, 0.01, key='sl23')

    b2 =st.button("Сгенерировать", key = 'bt2')
    if b2:
        mesh_file = "diff_mesh6.msh"
        subprocess.run(["python3", "generate_mesh6.py", mesh_file, width_d])
        plot_mesh(mesh_file)


def inter():
    st.subheader('___')
    width_i = st.slider("Ширина ", 0.01, 5.0, 2.0, key='sl31')
    # height_i = st.slider("Высота", 0.01, 5.0, 2.0, key='sl32')
    # mesh_size_i = st.slider("Размер сетки", 0.01, 0.5, 0.01, key='sl33')

    b3 = st.button("Сгенерировать", key='bt3')
    if b3:
        mesh_file = " intersec_mesh.msh"
        subprocess.run(["python3", "generate_mesh6.py",mesh_file, width_i])
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
    union()
    st.subheader('2. Вычитание (Subtraction): ')

    r'''Создание составной области путем вычитания одной геометрической фигуры из другой 
    (например, вырезание круглого отверстия из прямоугольной пластины)'''
    diff()
    st.subheader('3. Пересечение (Intersection): ')

    r'''Создание области, образованной общей частью нескольких геометрических фигур.'''
    inter()
    # st.subheader('4. Объединение с дыркой (Union with Hole): ')
    #
    # r'''Создание области с отверстием, путем объединения двух фигур и вырезания отверстия из одной из них.'''
    #



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

