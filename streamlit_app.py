import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.info('This is a machine learning app, built by a machine learning model')

# Load the penguins dataset
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

# Display raw data
st.write('**Raw Data**')
st.write(df)

# Data preparation
with st.expander('Data Visualization'):
    st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

# Sidebar input features
with st.sidebar:
    st.header('Input Features')
    island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
    gender = st.selectbox('Gender', ('Male', 'Female'))
    bill_length_mm = st.slider('Bill Length (mm)', 32.1, 59.6, 43.9)
    bill_depth_mm = st.slider('Bill Depth (mm)', 13.1, 21.5, 17.2)
    flipper_length_mm = st.slider('Flipper Length (mm)', 172.0, 231.0, 201.0)  # Corrected variable name
    body_mass_g = st.slider('Body Mass (g)', 2700.0, 6300.0, 4207.0)

    # Create the input DataFrame
    data = {
        'island': island,
        'bill_length_mm': bill_length_mm,
        'bill_depth_mm': bill_depth_mm,
        'flipper_length_mm': flipper_length_mm,
        'body_mass_g': body_mass_g,
        'gender': gender
    }
    input_df = pd.DataFrame(data, index=[0])

# Concatenate input features with existing data
input_penguins = pd.concat([input_df, df.drop('species', axis=1)], axis=0)

# Display input features DataFrame
with st.expander('Input Features'):
    st.write(input_df)

# Display combined penguins data
st.write('**Combined Penguins Data**')
st.write(input_penguins)
