import streamlit as st
import datetime
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import gmsh
import meshio
import matplotlib.pyplot as plt
import pyvista as pv
from st_pages import Page, show_pages, add_page_title
from stpyvista import stpyvista

def main():
    # Загрузка файла .msh в pyvista
    mesh = pv.read('gmsh_test6.msh')
    # Визуализация с помощью pyvista
    plotter = pv.Plotter(window_size=[100,100])
    plotter = pv.Plotter()
    plotter.add_mesh(mesh)  # Отображение сетки в белом цвете
    # Вывод графика pyvista в streamlit
    plotter.view_isometric()
    stpyvista(plotter)
    mesh = meshio.read('gmsh_test6.msh')
    # Отображение данных с помощью matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(mesh.points[:, 0], mesh.points[:, 1], mesh.points[:, 2], triangles=mesh.cells[1].data)

    # Загрузка файла .msh в pyvista
    # Вывод matplotlib streamlit
    st.pyplot(fig)
    gmsh.finalize()

if __name__ == "__main__":
    main()
