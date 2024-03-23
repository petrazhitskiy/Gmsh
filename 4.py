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
from st_pages import Page, show_pages, add_page_title

st.sidebar.title("MATPLOTLIb")

st.title('Чтение расчетный данных')









st.subheader('Matplotlib может работать с данными, представленными в виде различных структур и форматов. Некоторые из поддерживаемых носителей информации включают:')

st.subheader('Numpy Arrays')

code =""" 
    import numpy as np
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
"""

st.code(code, language='python')


st.subheader('Списки Python')

code =""" 
    x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
"""

st.code(code, language='python')


st.subheader('Pandas DataFrames')

code =""" 
   import pandas as pd
df = pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [2, 4, 6, 8, 10]})
"""

st.code(code, language='python')


st.subheader('Текстовые файлы')

code =""" 
   # Загрузка данных из текстового файла
data = np.loadtxt('данные.txt')
"""

st.code(code, language='python')


st.subheader('CSV файлы')

code =""" 
    # Используется pandas для загрузки данных из CSV файла
df = pd.read_csv('данные.csv')
"""

st.code(code, language='python')


st.subheader('Excel файлы:')

code =""" 
    # Используется pandas для загрузки данных из Excel файла
df = pd.read_excel('данные.xlsx')
"""

st.code(code, language='python')


st.subheader('SQLite базы данных')

code =""" 
    import sqlite3
conn = sqlite3.connect('база_данных.db')
query = "SELECT * FROM таблица"
df = pd.read_sql(query, conn)
"""

st.code(code, language='python')



st.subheader('Серверы API')

code =""" 
    import requests
response = requests.get('https://api.example.com/data')
data = response.json()
"""

st.code(code, language='python')

st.subheader('Генерация случайных данных:')

code =""" 
    # Используется numpy для генерации случайных данных
x = np.random.rand(100)
y = np.random.rand(100)
"""

st.code(code, language='python')
