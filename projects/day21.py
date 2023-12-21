import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid", palette="rocket")

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

    st.markdown('### Data Overview')
    st.info(f'Number of rows: {data.shape[0]} and Number of columns: {data.shape[1]}')
    st.caption('Columns:')
    st.json(data.columns.to_list())
    st.caption('Data:')
    st.dataframe(data.style.highlight_max(axis=0, color='green').highlight_min(axis=0, color='purple'))
    st.caption('Data Types:')
    st.json(data.dtypes.to_dict())
    st.caption('Numeric Data Description:')
    st.dataframe(data.describe().T.style.highlight_max(axis=0, color='green').highlight_min(axis=0, color='purple'))
    
    st.markdown('### Data Visualization')

    st.markdown('#### Salary Distribution')
    plt.figure(figsize=(12, 6), dpi=300)
    sns.histplot(data['salary_in_usd'], kde=True, bins=30)
    plt.xlabel('Salary in USD')
    st.pyplot()

    st.markdown('#### Distribution of experience levels')
    st.bar_chart(data['experience_level'].value_counts())

    st.markdown('#### Distribution of employment types')
    st.bar_chart(data['employment_type'].value_counts())

    st.markdown('#### Top 10 Job Titles')
    st.bar_chart(data['job_title'].value_counts().head(10))

    st.markdown('#### Top 10 Locations for Data Scientists')
    st.bar_chart(data['company_location'].value_counts().head(10))

    st.markdown('#### Salary vs Experience Level')
    plt.figure(figsize=(12, 6), dpi=300)
    sns.boxplot(x='experience_level', y='salary_in_usd', data=data, order=data['experience_level'].value_counts().index)
    plt.xlabel('Experience Level')
    plt.ylabel('Salary in USD')
    st.pyplot()

    st.markdown('#### Salary vs Employment Type')
    plt.figure(figsize=(12, 6), dpi=300)
    sns.boxplot(x='employment_type', y='salary_in_usd', data=data, order=data['employment_type'].value_counts().index)
    plt.xlabel('Employment Type')
    plt.ylabel('Salary in USD')
    st.pyplot()

    def data_prepare(data):
        le = LabelEncoder()
        for col in ['experience_level', 'employment_type', 'salary_currency', 'job_title', 'employee_residence', 'company_location', 'company_size']:
            data[col] = le.fit_transform(data[col])
        return data
    
    st.markdown('#### Correlation Matrix')
    with st.spinner('Preparing data...'):
        data = data_prepare(data)
    plt.figure(figsize=(12, 6), dpi=300)
    sns.heatmap(data.corr(), annot=True, cmap='rocket', fmt='.2f')
    st.pyplot()