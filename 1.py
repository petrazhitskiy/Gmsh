import streamlit as st
from st_pages import Page, show_pages, add_page_title
import numpy as np

st.title("Общая характеристика ПО")
r"""

Gmsh - это автоматический трехмерный генератор конечно-элементной сетки со встроенными средствами предварительной и последующей обработки.

"""

r"""

Установка библиотеки через консоль:

"""

code1 = '''
        $ pip install gmsh
    '''
st.code(code1, language='python')

r"""

Импорт библиотеки:

"""

code2 = '''
        import pygmsh
    '''
st.code(code2, language='python')
