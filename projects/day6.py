import streamlit as st
import pandas as pd
import base64
from sklearn.metrics import accuracy_score, balanced_accuracy_score, precision_score, recall_score, f1_score, cohen_kappa_score, confusion_matrix

def app():
    st.title('Day #6')
    st.subheader('Machine Leraning Model Performance Calculator App')
    st.markdown('''
        This app evaluates the performance of machine learning models using various metrics & visualizations.
        
        * **Python libraries:** `streamlit`, `pandas`, `sklearn`, `base64`.
        
        * **Reference:** [Data Professor](https://github.com/dataprofessor)

        ---
    ''')

    # Confusion Matrix
    def calc_confusion_matrix(df):
        y_true = df.iloc[:, 0].values
        y_pred = df.iloc[:, 1].values
        confusion_matrix_array = confusion_matrix(y_true, y_pred)
        confusion_matrix_df = pd.DataFrame(confusion_matrix_array, columns=['Predicted Negative', 'Predicted Positive'], index=['Actual Negative', 'Actual Positive'])
        return confusion_matrix_df
    
    # Performance Metrics
    def calc_metrics(df):
        y_true = df.iloc[:, 0].values
        y_pred = df.iloc[:, 1].values
        metrics_dict = {
            'Accuracy Score': accuracy_score(y_true, y_pred),
            'Balanced Accuracy Score': balanced_accuracy_score(y_true, y_pred),
            'Precision Score': precision_score(y_true, y_pred, average='weighted'),
            'Recall Score': recall_score(y_true, y_pred, average='weighted'),
            'F1 Score': f1_score(y_true, y_pred, average='weighted'),
            'Cohen Kappa Score': cohen_kappa_score(y_true, y_pred)
        }
        metrics_df = pd.DataFrame.from_dict(metrics_dict, orient='index', columns=['Value'])
        return metrics_df
    
    # Load Example Data
    @st.cache_data
    def load_example_data():
        df = pd.read_csv('data/day6_example.csv')
        return df
    
    # Download Performance Metrics
    def filedownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode() # strings <-> bytes conversions
        href = f'<a href="data::file/csv;base64,{b64}" download="performance_metrics.csv">Download as CSV File</a>'
        return href

    # Main Panel
    # Upload CSV data
    uploaded_file = st.file_uploader("Upload your input CSV file (Submission)", type=["csv"])

    # Performance metrics
    performance_metrics = ['Accuracy Score', 'Balanced Accuracy Score', 'Precision Score', 'Recall Score', 'F1 Score', 'Cohen Kappa Score']
    selected_metrics = st.multiselect("Select performance metrics", performance_metrics, performance_metrics)
    with st.expander('Performance Metrics Description & Formulas'):
        st.markdown('''
            * **Accuracy Score:** It is the number of correct predictions divided by the total number of predictions. It is suitable when the target class is well balanced.
        ''')
        st.latex(r'''Accuracy Score = \frac{TP + TN}{TP + TN + FP + FN}''')
        st.markdown('''
            ---
            * **Balanced Accuracy Score:** It is the average recall obtained on each class. It is suitable when the target class is imbalanced.
        ''')
        st.latex(r'''Balanced Accuracy Score = \frac{TPR + TNR}{2} = \frac{TP}{TP + FN} + \frac{TN}{TN + FP}''')
        st.markdown('''
            ---
            * **Precision Score:** It is the number of true positives divided by the number of true positives and false positives. It is suitable when the cost of false positives is high.
        ''')
        st.latex(r'''Precision Score = \frac{TP}{TP + FP}''')
        st.markdown('''
            ---
            * **Recall Score:** It is the number of true positives divided by the number of true positives and false negatives. It is suitable when the cost of false negatives is high.
        ''')
        st.latex(r'''Recall Score = \frac{TP}{TP + FN}''')
        st.markdown('''
            ---
            * **F1 Score:** It is the harmonic mean of precision and recall. It is suitable when you want to seek a balance between precision and recall.
        ''')
        st.latex(r'''F1 Score = 2 \times \frac{Precision Score \times Recall Score}{Precision Score + Recall Score}''')
        st.markdown('''
            ---
            * **Cohen Kappa Score:** It is the classification accuracy normalized by the imbalance of the classes in the data. It is suitable when there is a large class imbalance.
        ''')
        st.latex(r'''Cohen Kappa Score = \frac{Accuracy Score - Expected Accuracy Score}{1 - Expected Accuracy Score}''')

    if uploaded_file is not None:        
        df = pd.read_csv(uploaded_file)
        cf = calc_confusion_matrix(df)
        metrics_df = calc_metrics(df)
        selected_metrics_df = metrics_df.loc[selected_metrics]
        st.header('Input Data')
        st.dataframe(df)
        st.header('Confusion Matrix')
        st.dataframe(cf)
        st.header('Performance Metrics')
        st.dataframe(selected_metrics_df)
        st.markdown(filedownload(selected_metrics_df), unsafe_allow_html=True)
    else:
        st.info('Awaiting for CSV file to be uploaded.')
        if st.button('Use Example Dataset'):
            df = load_example_data()
            cf = calc_confusion_matrix(df)
            metrics_df = calc_metrics(df)
            selected_metrics_df = metrics_df.loc[selected_metrics]
            st.header('Input Data')
            st.dataframe(df)
            st.header('Confusion Matrix')
            st.dataframe(cf.style.highlight_max(axis=0, color='purple'))
            st.header('Performance Metrics')
            st.dataframe(selected_metrics_df.style.highlight_max(axis=0, color='purple'))
            st.markdown(filedownload(selected_metrics_df), unsafe_allow_html=True)