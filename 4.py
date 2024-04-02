import streamlit as st
import subprocess
import meshio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_mesh(mesh_file):
    mesh = meshio.read(mesh_file)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(mesh.points[:, 0], mesh.points[:, 1], mesh.points[:, 2], triangles=mesh.cells_dict["triangle"])
    st.pyplot(fig)

st.title("Построение плоскости с помощью сетки")

st.title('Создание областей в Gmsh')
r'''Создание областей в Gmsh включает в себя несколько ключевых этапов.
 Вот краткий обзор основных шагов'''
st.subheader('1. Инициализация Gmsh')
r'''Это подготавливает библиотеку к работе с вашей моделью.'''
st.code('''
import gmsh
gmsh.initialize()
''')

st.subheader('2. Создание новой модели')
r'''Создайте новую модель, в которой будете работать. Это ваш "рабочий холст".'''
st.code('''
gmsh.model.add("Название модели")
''')

st.subheader('3. Определение геометрических элементов')
r'''Определите геометрические элементы (точки, линии, кривые и т.д.), которые будут использоваться для создания области.'''
st.code('''
p1 = gmsh.model.geo.addPoint(x1, y1, z1, meshSize)
p2 = gmsh.model.geo.addPoint(x2, y2, z2, meshSize)
l1 = gmsh.model.geo.addLine(p1, p2)
''')

st.subheader('4. Формирование области')
r'''Используйте созданные геометрические элементы для формирования области, определив контуры и поверхности.'''
st.code('''
loop = gmsh.model.geo.addCurveLoop([l1, l2, l3, l4])
surface = gmsh.model.geo.addPlaneSurface([loop])
''')

st.subheader('5. Синхронизация геометрии')
r'''Синхронизируйте определённую вами геометрию с внутренней структурой Gmsh, чтобы подготовить её к мешингу.'''
st.code('''
gmsh.model.geo.synchronize()
''')

st.subheader('6. Генерация сетки')
r'''Сгенерируйте сетку для вашей области. Этот шаг преобразует вашу геометрию в сетку элементов, которая может быть использована для численных расчётов.'''
st.code('''
gmsh.model.mesh.generate(2)  # Для 2D сетки
''')

st.subheader('7. Экспорт сетки')
r'''Экспортируйте сгенерированную сетку в файл, чтобы использовать её в других приложениях или для анализа.'''
st.code('''
gmsh.write("output.msh")
''')

st.subheader('8. Завершение работы с Gmsh')
r'''По завершении работы с Gmsh корректно завершите сессию, чтобы освободить ресурсы.'''
st.code('''
gmsh.finalize()
''')

st.subheader('Построение квадрата')
width = st.slider("Ширина ", 0.01, 5.0, 2.0, key='sl01')
height = st.slider("Высота", 0.01, 5.0, 2.0, key='sl02')
mesh_size = st.slider("Размер сетки", 0.01, 0.5, 0.01, key='sl03')

if st.button("Сгенерировать" ,key='button1'):
    mesh_file = "gmsh_test4.msh"
    subprocess.run(["python3", "generate_mesh4.py", mesh_file, str(width), str(height), str(mesh_size), ])
    plot_mesh(mesh_file)


def plot_mesh_from_file(mesh_file):
    # Чтение сетки
    mesh = meshio.read(mesh_file)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(mesh.points[:, 0], mesh.points[:, 1], mesh.points[:, 2], triangles=mesh.cells_dict["triangle"])
    st.pyplot(fig)

    # Получение координат узлов и элементов
    points = mesh.points[:, :2]  # Используем только X и Y координаты
    cells = mesh.cells_dict["triangle"]  # Для треугольной сетки

    # Создание графика
    plt.figure(figsize=(8, 8))
    plt.gca().set_aspect('equal')

    # Отрисовка каждого треугольника
    for tri in cells:
        t_coords = np.append(tri, tri[0])  # Замыкание треугольника
        plt.plot(points[t_coords, 0], points[t_coords, 1], 'b-')

    # Отрисовка узлов
    plt.plot(points[:, 0], points[:, 1], 'ro')

    plt.title(f"Mesh Visualization: {mesh_file}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()
    
# Пример использования для визуализации круглой и треугольной сеток
figure_type = st.selectbox("Выбирите тип фигуры:", ["Окружность", "Многоугольник"])
if figure_type == "Окружность":
        mesh_file = "circle_mesh.msh"
else: mesh_file = "triangle_mesh.msh"
if figure_type == 'Многоугольник': sides = st.slider("Количество углов" , 1, 30, 0)
else: sides = 0
radius = st.slider("Радиус" , 1.00, 10.0, 5.0)
mesh_size = st.slider("Размер сетки", 0.1, 1.00, 0.5)
if st.button("Сгенерировать"):
    
    subprocess.run(["python3", "generate_circle4.py", str(sides),str(radius), str(mesh_size), mesh_file ])
    plot_mesh_from_file(mesh_file)

def plot_mesh_from_file(mesh_file):
    # Чтение сетки
    mesh = meshio.read(mesh_file)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(mesh.points[:, 0], mesh.points[:, 1], mesh.points[:, 2], triangles=mesh.cells_dict["triangle"])
    st.pyplot(fig)

    # Получение координат узлов и элементов
    points = mesh.points[:, :2]  # Используем только X и Y координаты
    cells = mesh.cells_dict["triangle"]  # Для треугольной сетки

    punct4
    # Создание графика
    plt.figure(figsize=(8, 8))
    plt.gca().set_aspect('equal')

    # Отрисовка каждого треугольника
    for tri in cells:
        t_coords = np.append(tri, tri[0])  # Замыкание треугольника
        plt.plot(points[t_coords, 0], points[t_coords, 1], 'b-')


    # Отрисовка узлов
    plt.plot(points[:, 0], points[:, 1], 'ro')

    plt.title(f"Mesh Visualization: {mesh_file}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()


# Пример использования для визуализации круглой и треугольной сеток
figure_type = st.selectbox( "Выбирите тип фигуры:",  ["Окружность", "Многоугольник"])
if figure_type == "Окружность":
        mesh_file = "circle_mesh.msh"
else: mesh_file = "triangle_mesh.msh"
if figure_type == 'Многоугольник': sides = st.slider("Количество углов" , 1, 30, 3,  key='sl1')
else: sides = 0
radius = st.slider("Радиус" , 1.00, 10.0, 5.0, key='sl2')
mesh_size = st.slider("Размер сетки", 0.1, 1.00, 0.5 ,  key='sl3' )
if st.button("Сгенерировать", key='button2'):
    
    subprocess.run(["python3", "generate_circle4.py", str(sides),str(radius), str(mesh_size), mesh_file ])
    plot_mesh_from_file(mesh_file)
