import streamlit as st

def app():
    st.title('Day #27')
    st.subheader('Time Series Forecasting with NeuralProphet')
    st.markdown('''
        This app is a demo of Time Series Forecasting with NeuralProphet.
                
        Reference: [NeuralProphet](https://neuralprophet.com/)
    ''')
    st.write('---')

    st.subheader('Install NeuralProphet')
    st.code('!pip install neuralprophet')

    st.subheader('Import Libraries')
    st.code('''
        from neuralprophet import NeuralProphet
        import pandas as pd
    ''')

    st.subheader('Load Data')
    st.code('''
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/timeseries.csv')
        df.columns = ['ds', 'y']
        df.head()
    ''')

    st.subheader('Train Model')
    st.code('''
        m = NeuralProphet()
        metrics = m.fit(df, freq='D')
    ''')

    st.subheader('Predict Future')
    st.code('''
        future = m.make_future_dataframe(df, periods=365)
        forecast = m.predict(future)
        forecast.head()
    ''')

    st.subheader('Plot Forecast')
    st.code('''
        # Plot Forecast
        fig = m.plot(forecast)
        
        # Plot Components
        fig_comp = m.plot_components(forecast)
            
        # Plot Parameters
        fig_param = m.plot_parameters()        
    ''')

    st.subheader('Save Model')
    st.code('''            
        m.save('model.pkl')
    ''')