# Streamlit Framework
import streamlit as st

# Data Processing
import pandas as pd
import numpy as np

# Data Visulization
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style='whitegrid', palette='viridis')

# Machine Learning
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.datasets import load_wine, load_diabetes, load_breast_cancer, load_iris
import joblib

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

def data_summary_info(df):
    summary_df = pd.DataFrame(df.dtypes, columns=['dtypes'])
    summary_df['missing#'] = df.isna().sum()
    summary_df['missing%'] = df.isna().sum() / len(df)
    summary_df['unique'] = df.nunique().values
    summary_df['count'] = df.count().values
    return summary_df

def draw_heatmap(df):
    plt.figure(figsize=(12,10), dpi=300)
    corr_matrix = df.corr(method='pearson')
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='coolwarm')
    st.pyplot()

def draw_numeric_distplot(df, plots_per_line = 3):
    num_cols = df.select_dtypes(include=np.number).columns.tolist()
    if len(num_cols) == 0:
        st.info('No Numeric Columns in the Dataset.')
        return
    for i in range(0, len(num_cols), plots_per_line):
        fig, axes = plt.subplots(1, plots_per_line, figsize=(15, 5))
        for j in range(plots_per_line):
            if i + j < len(num_cols):
                sns.distplot(df[num_cols[i + j]], ax=axes[j])
                axes[j].set_title(num_cols[i + j])
        st.pyplot(fig)

def draw_categorical_distplot(df, plots_per_line = 3):
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    if len(cat_cols) == 0:
        st.info('No Categorical Columns in the Dataset.')
        return
    for i in range(0, len(cat_cols), plots_per_line):
        fig, axes = plt.subplots(1, plots_per_line, figsize=(15, 5))
        for j in range(plots_per_line):
            if i + j < len(cat_cols):
                sns.countplot(x=cat_cols[i + j], data=df, ax=axes[j])
                axes[j].set_title(cat_cols[i + j])
                axes[j].tick_params(axis='x', rotation=45)
        st.pyplot(fig)

def save_model(model, filename='xgboost_model.joblib'):
    joblib.dump(model, filename)

def build_model(df, params, target, features, split_size):
    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_size / 100.0, random_state=params['random_state'])

    model = XGBRegressor(
        max_depth=params['max_depth'],
        n_estimators=params['n_estimators'],
        learning_rate=params['learning_rate'],
        min_child_weight=params['min_child_weight'],
        subsample=params['subsample'],
        colsample_bytree=params['colsample_bytree'],
        gamma=params['gamma'],
        reg_alpha=params['reg_alpha'],
        reg_lambda=params['reg_lambda'],
        random_state=params['random_state']
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.subheader('5. Model Performance Metrics')
    st.markdown(f'* Mean Squared Error: `{mse}`')
    st.markdown(f'* R-squared Score: `{r2}`')
    st.markdown(f'* Mean Absolute Error: `{mae}`')

def app():
    st.title('Day #4')
    st.subheader('No Code Machine Learning Web App based on XGBoostRegressor')
    
    # Load data caching
    @st.cache_data
    def load_data(file):
        df = pd.read_csv(file)
        return df

    # Load CSV data
    st.subheader('1. Upload your CSV data')
    uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
    st.markdown("""
    [What CSV files are?](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html)
    """)

    # Main Panel - Displays the Dataset and Metrics
    st.subheader('2. Dataset and Metrics')
    st.markdown('**2.1. Dataset Overview**')
    df = None
    if uploaded_file is not None:
        df = load_data(uploaded_file)
    else:
        st.info('Awaiting for CSV file to be uploaded.')
        selected_df = st.selectbox('Select Dataset', ['Iris', 'Wine', 'Breast Cancer', 'Diabetes'])
        if selected_df == 'Iris':
            df = load_iris(as_frame=True).frame
        elif selected_df == 'Wine':
            df = load_wine(as_frame=True).frame
        elif selected_df == 'Breast Cancer':
            df = load_breast_cancer(as_frame=True).frame
        else:
            df = load_diabetes(as_frame=True).frame
    st.dataframe(df.head())

    # Data Understading
    if df is not None:
        st.markdown('**2.2. Dataset Dimension**')
        st.info(f'{df.shape[0]} rows and {df.shape[1]} columns.')
        st.markdown('**2.3. Dataset Description**')
        st.dataframe(df.describe().T)
        st.markdown('**2.4. Dataset Overview Information**')
        st.dataframe(data_summary_info(df))
        st.markdown('**2.5. Dataset Correlation**')
        try:
            st.dataframe(df.corr())
        except Exception as e:
            st.info('Dataset Corr not available.')
            st.info(e)

    # Exploratory Data Analysis
    if df is not None:
        st.subheader('3. Exploratory Data Analysis')
        st.markdown('**2.6. Correlation Matrix Heatmap**')
        draw_heatmap(df)
        st.markdown('**2.7. Distribution of Numerical Columns**')
        draw_numeric_distplot(df)
        st.markdown('**2.8. Distribution of Categorical Columns**')
        draw_categorical_distplot(df)
        
    # Setting Up Parameters
    st.subheader('4. Set up Parameters')
    target = st.selectbox('Select the Target Column', df.columns.tolist())
    features = st.multiselect('Select the Features', df.columns.tolist(), df.columns.tolist())
    split_size = st.slider('Data split ratio (% for Training Set)', 10, 90, 80, 5)

    # Set up parameters for xgboost regressor
    params = dict()
    params['max_depth'] = st.number_input('max_depth', 1, 100, 5, 1)
    params['n_estimators'] = st.number_input('n_estimators', 1, 1000, 100, 1)
    params['learning_rate'] = st.number_input('learning_rate', 0.01, 1.0, 0.1, 0.01)
    params['min_child_weight'] = st.number_input('min_child_weight', 1, 10, 1, 1)
    params['subsample'] = st.number_input('subsample', 0.01, 1.0, 0.8, 0.05)
    params['colsample_bytree'] = st.number_input('colsample_bytree', 0.01, 1.0, 0.8, 0.05)
    params['gamma'] = st.number_input('gamma', 0.0, 10.0, 0.0, 0.05)
    params['reg_alpha'] = st.number_input('reg_alpha', 0.0, 10.0, 0.0, 0.05)
    params['reg_lambda'] = st.number_input('reg_lambda', 1.0, 10.0, 1.0, 0.05)
    params['random_state'] = st.number_input('random_state', 0, 1000, 42, 1)

    # Model Building
    if st.button('Press to Build the Model'):
        with st.spinner('Model is being built...'):
            best_model = build_model(df, params, target, features, split_size)
        st.snow()
        st.success('Model has been built successfully!')
        st.subheader('6. Download Model as Pickle File')
        if st.button('Download Model'):
            save_model(best_model, 'xgboost_model.joblib')
            st.info('Model has been saved as `xgboost_model.joblib`')



    