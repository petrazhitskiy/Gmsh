import streamlit as st
import subprocess
import meshio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_mesh(mesh_file):
    mesh = meshio.read(mesh_file)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(mesh.points[:, 0], mesh.points[:, 1], mesh.points[:, 2], triangles=mesh.cells_dict["triangle"])
    st.pyplot(fig)

st.title("Gmsh Mesh Visualization in Streamlit")

if st.button("Generate and Show Mesh"):
    mesh_file = "gmsh_test4.msh"
    subprocess.run(["python3", "generate_mesh4.py", mesh_file])
    plot_mesh(mesh_file)
