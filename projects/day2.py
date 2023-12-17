import streamlit as st
import pandas as pd
import numpy as np
import base64
import matplotlib.pyplot as plt
import yfinance as yf

def app():
    st.title('Day #2')
    st.subheader('Stocks Price Web App 📈')

    st.markdown("""
    This app retrieves the list of the **S&P 500** from Wikipedia and Analyze this companies stats using **yfinance**!
    * **Python modules:** base64, pandas, streamlit.
    * **Data source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)
    * **Reference:** [Data Professor](https://github.com/dataprofessor)
    """)

    with st.expander('About S&P 500'):
        st.markdown("""
        The S&P 500 stock market index is maintained by S&P Dow Jones Indices. It comprises 503 common stocks which are issued by 500 large-cap companies traded on American stock exchanges.
        """)

    st.subheader('User Input Features')
    
    # Web scraping of S&P 500 data
    @st.cache_data
    def load_data():
        url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
        html = pd.read_html(url, header=0)
        df = html[0]
        return df
    
    df = load_data()

    # Sector Selection
    sorted_sector_unique = sorted(df['GICS Sector'].unique())
    selected_sector = st.multiselect('Sector', sorted_sector_unique, sorted_sector_unique[0])
    df_selected_sector = df[(df['GICS Sector'].isin(selected_sector))]

    # Sub-Industry Selection
    sorted_subindustry_unique = sorted(df_selected_sector['GICS Sub-Industry'].unique())
    selected_subindustry = st.multiselect('Sub-Industry', sorted_subindustry_unique, sorted_subindustry_unique)
    df_final_selected = df_selected_sector[df_selected_sector['GICS Sub-Industry'].isin(selected_subindustry)]

    # Filtering data
    st.subheader('Display Companies in Selected Sector')
    st.dataframe(df_final_selected)
    
    # Download S&P500 data
    def filedownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode() # strigns <-> bytes conversions
        href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download as CSV File</a>'
        return href
    
    st.markdown(filedownload(df_final_selected), unsafe_allow_html=True)

    # Plot Closing Price of Query Symbol
    if len(df_final_selected)!=0:
        data = yf.download(
            tickers = list(df_final_selected.Symbol),
            period = "ytd",
            interval = "1d",
            group_by = "ticker",
            auto_adjust = True,
            prepost = True,
            threads = True,
            proxy = None
        )

        def price_plot(symbol):
            df = pd.DataFrame(data[symbol].Close)
            df['Date'] = df.index
            plt.fill_between(df.Date, df.Close, color='lime', alpha=0.3)
            plt.plot(df.Date, df.Close, color='lime', alpha=0.8)
            plt.xticks(rotation=90)
            plt.title(symbol, fontweight='bold')
            plt.xlabel('Date', fontweight='bold')
            plt.ylabel('Closing Price', fontweight='bold')
            return st.pyplot()
        
        num_company = st.slider('Number of Companies', 1, len(df_final_selected))
        
        if st.button('Show Plots'):
            st.subheader('Stock Closing Price')
            for i in list(df_final_selected.Symbol)[:num_company]:
                price_plot(i)