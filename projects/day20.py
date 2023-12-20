import streamlit as st
import pandas as pd
import cryptocompare
from datetime import datetime

def fetch_crypto_data(coin, currency, limit=30):
    historical_data = cryptocompare.get_historical_price_day(coin, currency, limit=limit, exchange='CCCAGG', toTs=datetime.now())
    df = pd.DataFrame(historical_data)
    df['time'] = pd.to_datetime(df['time'], unit='s').dt.date
    df.set_index('time', inplace=True)
    df.drop(columns=['conversionType', 'conversionSymbol'], inplace=True)
    df['change%'] = df['close'] / df['open'] * 100 - 100
    return df

def app():
    st.title('Day #20')
    st.subheader('Cryptocurrency Analytics Web App')
    st.markdown('''
        This app is cryptocurrency analytics dashboard that allows you to analyze price, volume, and volatility of different cryptocurrencies.
        
        **Refercence:** [Cryptocompare API](https://min-api.cryptocompare.com/)
    ''')
    st.write('---')

    coin = st.selectbox('Select Crypto', ['BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'BNB', 'EOS', 'XLM', 'TRX', 'ADA'])
    currency = st.selectbox('Select Currency', ['USD', 'KZT', 'EUR', 'GBP', 'JPY', 'KRW', 'CNY', 'RUB', 'INR', 'TRY', 'BRL'])

    num_days = st.slider('Select Number of Days', 7, 365, 30)

    crypto_data = fetch_crypto_data(coin, currency, int(num_days))

    # Visual Metrics Data
    st.subheader('Today\'s State Information')
    colA, colB, colC = st.columns(3)
    colA.metric(label='Price', value=round(crypto_data['close'][-1], 2), delta=round(crypto_data['change%'][-1], 2))
    colB.metric(label='Volume', value=round(crypto_data['volumefrom'][-1], 2), delta=round(crypto_data['volumeto'][-1], 2))
    colC.metric(label='Volatility', value=round(crypto_data['high'][-1] - crypto_data['low'][-1], 2), delta=round(crypto_data['high'][-1] - crypto_data['low'][-1], 2))

    st.markdown('### Data from the last {} days'.format(num_days))

    st.dataframe(crypto_data.style.highlight_max(axis=0, color='green').highlight_min(axis=0, color='purple'))   

    # Data Visualization
    st.subheader('Opening and Closing Price')
    st.line_chart(crypto_data[['open', 'close']])

    st.subheader('Volume')
    st.line_chart(crypto_data['volumefrom'])

    st.subheader('Volatility')
    st.line_chart(crypto_data['high'] - crypto_data['low'])