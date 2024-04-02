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
import streamlit as st
import datetime
from st_pages import Page, show_pages, add_page_title


st.sidebar.title("    ")

st.title('    ')


# Пример использования
def plot_mesh(mesh_file):
    # Визуализация с помощью pyvista
    mesh = pv.read(mesh_file)
    plotter = pv.Plotter()
    plotter.add_mesh(mesh, show_edges=True, color=True)
    # Вывод графика pyvista в streamlit
    plotter.view_isometric()
    stpyvista(plotter)

def main():
    mark_subdomains_and_boundaries()


if __name__ == '__main__':
    main()







