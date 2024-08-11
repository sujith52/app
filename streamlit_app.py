import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.info('thi sis a machine learning app, built by machie learning model')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
