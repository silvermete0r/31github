import streamlit as st
from ipyvizzu import Chart, Data, Config, DisplayTarget
import pandas as pd
import json

def app():
    st.title('Day #30')
    st.subheader('Storytelling with Data Visualization using `ipyvizzu`')
    st.markdown('''
        This app is a simple example of how to use `ipyvizzu` to create interactive data visualization.
                
        Reference: [Data Professor](https://github.com/dataprofessor)
    ''')
    st.write('---')

    tabA, tabB = st.tabs(['Demo', 'Tutorial'])

    with tabA:
        # Load the dataset
        df = pd.read_csv(
            "https://ipyvizzu.vizzuhq.com/0.17/showcases/titanic/titanic.csv"
        )
        data = Data()
        data.add_df(df)

        # Create the Vizzu chart
        chart = Chart(width="640px", height="360px", display=DisplayTarget.MANUAL)

        chart.animate(data)

        chart.animate(
            Config(
                {
                    "x": "Count",
                    "y": "Sex",
                    "label": "Count",
                    "title": "Passengers of the Titanic",
                }
            )
        )
        chart.animate(
            Config(
                {
                    "x": ["Count", "Survived"],
                    "label": ["Count", "Survived"],
                    "color": "Survived",
                }
            )
        )
        chart.animate(Config({"x": "Count", "y": ["Sex", "Survived"]}))
        
        st.components.v1.html(chart._repr_html_(), height=360)

    with tabB:
        st.subheader('Install ipyvizzu')
        st.code('!pip install ipyvizzu')

        st.subheader('Import Libraries')
        st.code('''
            from ipyvizzu import Chart
            import pandas as pd
        ''')

        st.subheader('Load Data')
        st.code('''
            df = pd.read_csv(
                "https://ipyvizzu.vizzuhq.com/0.17/showcases/titanic/titanic.csv"
            )
            data = Data()
            data.add_df(df)
        ''')

        st.subheader('Create Chart')
        st.code('''
            chart = Chart(width="640px", height="360px", display=DisplayTarget.MANUAL)
            chart.animate(data)
        ''')

        st.subheader('Customize Chart')
        st.code('''
            chart.animate(
                Config(
                    {
                        "x": "Count",
                        "y": "Sex",
                        "label": "Count",
                        "title": "Passengers of the Titanic",
                    }
                )
            )
            chart.animate(
                Config(
                    {
                        "x": ["Count", "Survived"],
                        "label": ["Count", "Survived"],
                        "color": "Survived",
                    }
                )
            )
            chart.animate(Config({"x": "Count", "y": ["Sex", "Survived"]}))
        ''')

        st.subheader('Display Chart')
        st.code('''
            st.components.v1.html(chart._repr_html_(), height=360)
        ''')