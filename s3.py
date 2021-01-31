import pandas as pd
import streamlit as st
from PIL import Image


#@st.cache
#def load_data(year):
#     df = pd.read_csv("stocksdata.csv")
#     company_stat = df
#     return  company_stat
#company_stat = load_data(select_year)


image = Image.open('download.jpg')
st.image(image, use_column_width=True)

st.write("""
#  Stock Analysis
""")

st.sidebar.header('User Input Features')



df = pd.read_csv("stocksdata.csv")
df.drop('Unnamed: 0', inplace=True, axis=1)
df.drop('Unnamed: 0.1', inplace=True, axis=1)
df.fillna(0)

sorted_unique_company = df.Company.unique()
selected_company = st.sidebar.selectbox('Company', sorted_unique_company)

df_final = df.loc[df.Company == selected_company]



st.dataframe(df_final)