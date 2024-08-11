import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.info('thi sis a machine learning app, built by machie learning model')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
