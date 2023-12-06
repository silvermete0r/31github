import streamlit as st
import pandas as pd
import zipfile
import base64
import uuid
import os

def app():
    st.title('Day #5')
    st.subheader('Excel & CSV Files Multi Merger')
    st.markdown('''
    This app merges multiple excel & csv files into one file.
                
    **Libraries:** `streamlit`, `pandas`, `numpy`, `zipfile`, `base64`, `uuid`, `os`
                
    **Reference:** [Data Professor](https://github.com/dataprofessor)
    
    ---
    ''')

    st.info('Excel & CSV files must have the same number of columns & column names!')

    # Excel & CSV files merge function
    def excel_and_csv_file_merge(uploaded_file):
        try:
            unique_dirname = str(uuid.uuid4())
            with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
                zip_ref.extractall(f'data/{unique_dirname}')
                file_list = zip_ref.namelist()

            merged_df = pd.DataFrame()
            for file in file_list:
                file_path = f'data/{unique_dirname}/{file}'
                if file.endswith('.csv'):
                    df = pd.read_csv(file_path)
                else:
                    df = pd.read_excel(file_path)
                merged_df = pd.concat([merged_df, df], ignore_index=True)
                os.remove(file_path)

            os.rmdir(f'data/{unique_dirname}')
            return merged_df
        except Exception as e:
            st.error(e)
            return None

    # Upload ZIP file
    st.subheader('1. Upload your ZIP file')
    uploaded_file = st.file_uploader("Upload your input ZIP file", type=["zip"])
    st.markdown("""
    [What ZIP files are?](https://en.wikipedia.org/wiki/Zip_(file_format))
    """)

    # File Download
    # as CSV
    def csvdownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="merged_file.csv">Download CSV File</a>'
        return href
    
    # as Excel
    def xldownload(df):
        df.to_excel('data/merged_file.xlsx', index=False)
        data = open('data/merged_file.xlsx', 'rb').read()
        b64 = base64.b64encode(data).decode('UTF-8')
        href = f'<a href="data:file/xls;base64,{b64}" download="merged_file.xlsx">Download Excel File</a>'
        return href

    # Main Panel
    if st.button('Submit'):
        if uploaded_file is not None:
            with st.spinner('Merging files...'):
                df = excel_and_csv_file_merge(uploaded_file)
                st.dataframe(df)
            colA, colB, _ = st.columns([1, 1, 3])
            with st.spinner('Making CSV file...'):
                colA.markdown(csvdownload(df), unsafe_allow_html=True)
            with st.spinner('Making Excel file...'):
                colB.markdown(xldownload(df), unsafe_allow_html=True)
        else:
            st.info('Awaiting for ZIP file to be uploaded.')



