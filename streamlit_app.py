import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.info('thi sis a machine learning app, built by machie learning model')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  x= df.drop('species',axis=1)
  x

  st.write('**Y**')
  y=df.species
  y
#"bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

#data preparations
with st.sidebar:
  st.header('Input Features')
  #,"bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g",
  island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
  gender = st.selectbox('Gender',('Male','Female'))
  bill_length_mm = st.slider('Bill Length (mm)',32.1,59.6,43.9)


  
