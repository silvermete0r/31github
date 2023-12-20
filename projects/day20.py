import streamlit as st
import pandas as pd
import plotly.express as px
import cryptocompare
from datetime import datetime, timedelta

def fetch_crypto_data(coin, currency, limit=30):
    end_time = datetime.now()
    start_time = end_time - timedelta(days=limit)
    historical_data = cryptocompare.get_historical_price_day(coin, currency, start_time, end_time, aggregate=1)
    df = pd.DataFrame(historical_data)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True)
    return df

def calculate_sma(data, window=30):
    # Calculate Simple Moving Average (SMA)
    data['sma'] = data['close'].rolling(window=window).mean()
    return data

def app():
    st.title('Day #20')
    st.subheader('Cryptocurrency Analytics Web App')
    st.markdown('''
        This app is cryptocurrency analytics dashboard that allows you to analyze price, volume, and volatility of different cryptocurrencies.
        
        **Refercence:** [Cryptocompare API](https://min-api.cryptocompare.com/)
    ''')
    st.write('---')

    coin = st.selectbox('Select Crypto', ['BTC', 'ETH', 'XRP', 'LTC'])
    currency = st.selectbox('Select Currency', ['USD', 'EUR', 'GBP', 'JPY'])

    num_days = st.slider('Select Number of Days', 7, 365, 30)

    crypto_data = fetch_crypto_data(coin, currency, num_days)

    window_size = st.slider('Select Window Size', 1, 100, 20)

    crypto_data = calculate_sma(crypto_data, window_size)

    fig = px.candlestick(crypto_data, x=crypto_data.index, open='open', high='high', low='low', close='close')
    fig.add_trace(px.line(crypto_data, x=crypto_data.index, y='SMA', line_shape='linear', line=dict(color='orange')).data[0])

    fig.update_layout(
        title=f'{coin} Historical Prices and SMA ({window_size} days)',
        xaxis_title='Date',
        yaxis_title=f'Price ({currency})',
        xaxis_rangeslider_visible=False,
    )

    st.plotly_chart(fig)

    st.subheader('Additional Information:')
    st.write(f"Current Price: {cryptocompare.get_price(coin, currency)[coin][currency]} {currency}")
    st.write(f"Market Cap: {cryptocompare.get_avg(coin, currency)['MKTCAP'][currency]} {currency}")