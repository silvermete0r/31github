import streamlit as st
import pandas as pd 
import numpy as np

def app():
    st.title('Day #26')
    st.subheader('Streamlit Maps Web App')
    st.markdown('''
        This app is a demo of the Streamlit Maps functionality.
                
        Reference: [Streamlit Docs](https://docs.streamlit.io/)
    ''')
    st.write('---')

    st.info('CSV file must have `latitude` and `longitude` columns.')

    data = st.file_uploader('Upload a CSV file', type=['csv'])

    color = st.color_picker('Pick a Color', '#00f900')

    size = st.slider('Pick a Size', 0, 100, 30)

    zoom = st.slider('Pick a Zoom Level', 0, 20, 2)

    use_container_width = st.checkbox('Use Container Width')
    
    if data is not None:
        with st.spinner('Loading Map...'):
            df = pd.read_csv(data)
            if 'latitude' not in df.columns or 'longitude' not in df.columns:
                st.error('Please make sure your CSV file has `latitude` and `longitude` columns.')
                st.stop()
            st.map(df, color=color, size=size, zoom=zoom, use_container_width=use_container_width)
    