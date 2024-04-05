import streamlit as st
from st_pages import Page, show_pages, add_page_title
import numpy as np

st.title("Геометрия")
st.subheader("Многоугольник (Polygon) ")
col1, col2 = st.columns(2)
with col1:
    code1 = '''
                import pygmsh
                with pygmsh.geo.Geometry() as geom:

                    geom.add_polygon(
                    [
                        [0.0, 0.0],
                        [1.0, -0.2],
                        [1.1, 1.2],
                        [0.1, 0.7],
                    ],

                    mesh_size=0.1,
                    ) 

                mesh = geom.generate_mesh()
            '''
    st.code(code1, language='python')

with col2:
    st.image('polygon.png')



st.subheader("Круг (Circle) ")
col3, col4 = st.columns(2)
with col3:
    code2 = '''
            import pygmsh
 
            with pygmsh.geo.Geometry() as geom:


                geom.add_circle([0.0, 0.0], 1.0, 
                         
                mesh_size=0.2)

                mesh = geom.generate_mesh()
        
        '''
    st.code(code2, language='python')

with col4:
    st.image('circle.png')


st.subheader("Сплайны (Splines) ")
col5, col6 = st.columns(2)
with col5:
    code3 = '''
            import pygmsh
            with pygmsh.geo.Geometry() as geom:
                lcar = 0.1
                p1 = geom.add_point([0.0, 0.0], lcar)
                p2 = geom.add_point([1.0, 0.0], lcar)
                p3 = geom.add_point([1.0, 0.5], lcar)
                p4 = geom.add_point([1.0, 1.0], lcar)
                s1 = geom.add_bspline([p1, p2, p3, p4])

                p2 = geom.add_point([0.0, 1.0], lcar)
                p3 = geom.add_point([0.5, 1.0], lcar)
                s2 = geom.add_spline([p4, p3, p2, p1])
                ll = geom.add_curve_loop([s1, s2])
                pl = geom.add_plane_surface(ll)

                mesh = geom.generate_mesh()
        '''
    st.code(code3, language='python')

with col6:
    st.image('splines.png')
