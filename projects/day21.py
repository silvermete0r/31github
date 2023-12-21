import streamlit as st
import pandas as pd

@st.cache_data()
def load_data():
    data = pd.read_csv('data/ds_salaries.csv')
    return data

def app():
    st.title('Day #21')
    st.subheader('Data Scientists Salary Analysis')
    st.markdown('''
        This app shows how to use Streamlit to create charts and plots for data visualization on the example of Data Scientists Salary Analysis.

        **Data Source:** [Kaggle](https://www.kaggle.com/datasets/henryshan/2023-data-scientists-salary)
                      
        **Reference:** [Streamlit Docs](https://docs.streamlit.io/)
    ''')
    st.write('---')

    data = load_data()

    st.markdown('### Line Chart')