
import streamlit as st
import datetime
from st_pages import Page, show_pages, add_page_title
import numpy as np
import streamlit as st
# import gmsh

st.title("Объемная геометрия")
st.subheader("Выдавливание (Extrude) ")
col1, col2 = st.columns(2)
with col1:
    code1 = '''
            import pygmsh
            with pygmsh.geo.Geometry() as geom:
                poly = geom.add_polygon(
                    [
                        [0.0, 0.0],
                        [1.0, -0.2],
                        [1.1, 1.2],
                        [0.1, 0.7],
                    ],
                    mesh_size=0.1,
                )
                geom.extrude(poly, [0.0, 0.3, 1.0],
                num_layers=5)

                mesh = geom.generate_mesh()
        '''
    st.code(code1, language='python')

with col2:
    st.image('extrude.png')

st.subheader("Вращение (Revolve) ")
col3, col4 = st.columns(2)
with col3:
    code2 = '''
            from math import pi
            import pygmsh

            with pygmsh.geo.Geometry() as geom:
                poly = geom.add_polygon(
                    [
                        [0.0, 0.2, 0.0],
                        [0.0, 1.2, 0.0],
                        [0.0, 1.2, 1.0],
                    ],
                    mesh_size=0.1,
                )
                geom.revolve(poly, [0.0, 0.0, 1.0], [0.0, 0.0, 0.0], 0.8 * pi)
                mesh = geom.generate_mesh()
        '''
    st.code(code2, language='python')

with col4:
    st.image('revolve.png')

st.subheader("Скручивание (twist) ")
col5, col6 = st.columns(2)
with col5:
    code3 = '''
            from math import pi
            import pygmsh

            with pygmsh.geo.Geometry() as geom:
                poly = geom.add_polygon(
                    [
                        [+0.0, +0.5],
                        [-0.1, +0.1],
                        [-0.5, +0.0],
                        [-0.1, -0.1],
                        [+0.0, -0.5],
                        [+0.1, -0.1],
                        [+0.5, +0.0],
                        [+0.1, +0.1],
                    ],
                    mesh_size=0.05,
                )

                geom.twist(
                    poly,
                    translation_axis=[0, 0, 1],
                    rotation_axis=[0, 0, 1],
                    point_on_axis=[0, 0, 0],
                    angle=pi / 3,
                )

                mesh = geom.generate_mesh()
        '''
    st.code(code3, language='python')

with col6:
    st.image('twist.png')






