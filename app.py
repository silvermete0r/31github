import streamlit as st
import requests
from streamlit_option_menu import option_menu
import pandas as pd
from constants import EMAIL_API
from projects import day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12, day13, day14, day15, day16, day17, day18, day19, day20, day21, day22, day23, day24, day25, day26, day27, day28, day29, day30, day31

# Set Page Config
st.set_page_config(
    page_title = 'DataFlow App',
    page_icon = '📊',
    layout = 'wide',
    initial_sidebar_state = 'auto',
)

# Home Page Content
def main():
    st.title('31 Days DS/ML Challenge')
    st.write('''
            [![Star](https://img.shields.io/github/stars/silvermete0r/31github.svg?logo=github&style=flat-square)](https://github.com/silvermete0r/31github)&nbsp;
            [![Fork](https://img.shields.io/github/forks/silvermete0r/31github.svg?logo=github&style=flat-square)](https://github.com/silvermete0r/31github)&nbsp;
            [![Watch](https://img.shields.io/github/watchers/silvermete0r/31github.svg?logo=github&style=flat-square)](https://github.com/silvermete0r/31github)&nbsp;
            [![Follow](https://img.shields.io/github/followers/silvermete0r.svg?logo=github&style=flat-square)](https://github.com/silvermete0r/31github)&nbsp;
            [![License](https://img.shields.io/github/license/silvermete0r/31github.svg?logo=github&style=flat-square)](https://github.com/silvermete0r/31github)
    ''')
    st.subheader('About Me')
    st.write('👋 My name is Arman, and I have accepted the challenge of 31 days of coding from [GrowthHungry](https://www.growthhungry.life/challenge)')
    st.write('📚 I\'m currently learning `Data Science` and `Machine Learning`.')
    st.write('👨‍💻 All of my projects are available at [my GitHub](https://github.com/silvermete0r)')

    st.subheader('My Projects')
    st.table({
        'Project': {
            'Day_#1': '🏀 NBA Player Stats Explorer',
            'Day_#2': '📈 Stocks Price Web App',
            'Day_#3': '🧰 Streamlit Toolkit',
            'Day_#4': '💎 No-Code ML Web App based on XGBoostRegressor',
            'Day_#5': '🗃️ Excel & CSV Files Multi Merger',
            'Day_#6': '📊 Machine Learning Model Performance Calculator',
            'Day_#7': '🖼️ Image Quality Enhancement Web App',
            'Day_#8': '😺 Github Profile Data Analyzer Web App',
            'Day_#9': '🧑 Face Recognition Web App',
            'Day_#10': '💡 Multi-Object Classifier Web App',
            'Day_#11': '👾 Tensorflow Image Classification DL Model Training Baseline',
            'Day_#12': '🌸 Tensorflow Simple Iris Classification App',
            'Day_#13': '🏠 Tensorflow Regression Model Training Based on Boston Housing Dataset',
            'Day_#14': '📝 Text Summarization using HuggingFace Transformers',
            'Day_#15': '📝 Text Sentiment Analysis using HuggingFace Transformers',
            'Day_#16': '📝 Text Completion using HuggingFace Transformers',
            'Day_#17': '',
        },
        'Description': {
            'Day_#1': 'This app analyze data about NBA Basketball Player Stats in Regular Seasons! Data taken from official resource using web scrapping!',
            'Day_#2': 'This app retrieves the list of the S&P 500 from Wikipedia and Analyze this companies stats using yfinance!',
            'Day_#3': 'This app provides fully-explained useful cheatsheet for Streamlit Framework!',
            'Day_#4': 'This app provides a no-code web interface to use XGBoostRegressor for training & testing Machine Learning Models based on various datasets.',
            'Day_#5': 'This app merges multiple excel & csv files into one file.',
            'Day_#6': 'This app evaluates the performance of machine learning models using various metrics.',
            'Day_#7': 'This app enhances the quality of an image using various techniques.',
            'Day_#8': 'This app analyzes the data of any Github profile using Github API.',
            'Day_#9': 'This app detects faces in uploaded images using Haar Cascades.',
            'Day_#10': 'This app predicts the class of different objects in an image using a pre-trained MobileNetV2 model.',
            'Day_#11': 'This app trains a simple CNN model on the MNIST dataset using Tensorflow.',
            'Day_#12': 'This app demonstrates a simple TensorFlow Iris classification model using the Sklearn Iris dataset.',
            'Day_#13': 'This app demonstrates a simple Tensorflow regression model using the Boston Housing dataset.',
            'Day_#14': 'This app is a simple text summarization app using HuggingFace Transformers.',
            'Day_#15': 'This app is a simple text sentiment analysis app using `BERT` model from HuggingFace Transformers.',
            'Day_#16': 'This app is a simple text completion app using GPT-2 model from HuggingFace Transformers.',
            'Day_#17': '',
        },
        'Reference': {
            'Day_#1': 'Data Professor',
            'Day_#2': 'Data Professor',
            'Day_#3': 'Streamlit Docs',
            'Day_#4': 'Data Professor',
            'Day_#5': 'Data Professor',
            'Day_#6': 'Data Professor',
            'Day_#7': 'OpenCV Docs',
            'Day_#8': 'Github API Docs',
            'Day_#9': 'OpenCV Haar Cascades',
            'Day_#10': 'MobileNetV2',
            'Day_#11': 'Tensorflow Guide',
            'Day_#12': 'Tensorflow Guide',
            'Day_#13': 'Tensorflow Guide',
            'Day_#14': 'HuggingFace Transformers',
            'Day_#15': 'HuggingFace Transformers',
            'Day_#16': 'HuggingFace Transformers',
            'Day_#17': '',
        },
    })

    st.subheader('Contact Me')

    def send_message(user_name, user_email, user_message):
        return requests.post(
        "https://api.mailgun.net/v3/sandboxebd1ff2187ca4bf6a7610daf43c30c0a.mailgun.org/messages",
        auth=("api", EMAIL_API),
        data={"from": "Mailgun Sandbox <postmaster@sandboxebd1ff2187ca4bf6a7610daf43c30c0a.mailgun.org>",
            "to": "Supwithproject <supwithproject@gmail.com>",
            "subject": f"31Days Dataflow User Message from {user_name} <{user_email}>",
            "text": user_message})

    with st.form(key='contact_form', clear_on_submit=True):
        user_name = st.text_input('Name')
        user_email = st.text_input('Email')
        user_message = st.text_area('Message')
        submitted = st.form_submit_button('Submit')
        if submitted:
            try:
                send_message(user_name, user_email, user_message)
                st.success('Thank you for your message! I will get back to you as soon as possible.')
            except Exception as e:
                st.error('Something went wrong... Please try again.')
                st.error(e)

    col1, col2, col3 = st.columns(3)
    col1.write('✈️ Telegram: [@silvermete0r](https://t.me/silvermete0r)')
    col2.write('📷 Instagram: [@grembim](https://www.instagram.com/grembim)')
    col3.write('🔗 Taplink: [@grembim](https://one.link/grembim)')

# Multipage WebApp Design
class MultiApp:
    def __init__(self):
        self.apps = []
    
    def add_app(self, title, function):
        self.apps.append({
            'title': title,
            'function': function
        })
    
    def run():
        with st.sidebar:
            # Set Sidebar Content
            st.sidebar.image('media/logo.png', use_column_width=True)
            app = option_menu(
                menu_title = None,
                options = ['Main', 'Day #1', 'Day #2', 'Day #3', 'Day #4', 'Day #5', 'Day #6', 'Day #7', 'Day #8', 'Day #9', 'Day #10', 'Day #11', 'Day #12', 'Day #13', 'Day #14', 'Day #15', 'Day #16', 'Day #17', 'Day #18', 'Day #19', 'Day #20', 'Day #21', 'Day #22', 'Day #23', 'Day #24', 'Day #25', 'Day #26', 'Day #27', 'Day #28', 'Day #29', 'Day #30', 'Day #31'],
                icons = ['menu-up'],
                menu_icon = 'chat-text-fill',
                default_index = 0
            )
            st.info('31 Days Educational Challenge for Data Science / Machine Learning for the program [GrowthHungry](https://www.growthhungry.life/challenge) Challenge.')
            st.caption('Made with ❤️ by [DataFlow](https://dataflow.kz) team.')

        # Set Main Content
        if app == 'Main':
            main()
        if app == 'Day #1':
            day1.app()
        if app == 'Day #2':
            day2.app()
        if app == 'Day #3':
            day3.app()
        if app == 'Day #4':
            day4.app()
        if app == 'Day #5':
            day5.app()
        if app == 'Day #6':
            day6.app()
        if app == 'Day #7':
            day7.app()
        if app == 'Day #8':
            day8.app()
        if app == 'Day #9':
            day9.app()
        if app == 'Day #10':
            day10.app()
        if app == 'Day #11':
            day11.app()
        if app == 'Day #12':
            day12.app()
        if app == 'Day #13':
            day13.app()
        if app == 'Day #14':
            day14.app()
        if app == 'Day #15':
            day15.app()
        if app == 'Day #16':
            day16.app()
        if app == 'Day #17':
            day17.app()
        if app == 'Day #18':
            day18.app()
        if app == 'Day #19':
            day19.app()
        if app == 'Day #20':
            day20.app()
        if app == 'Day #21':
            day21.app()
        if app == 'Day #22':
            day22.app()
        if app == 'Day #23':
            day23.app()
        if app == 'Day #24':
            day24.app()
        if app == 'Day #25':
            day25.app()
        if app == 'Day #26':
            day26.app()
        if app == 'Day #27':
            day27.app()
        if app == 'Day #28':
            day28.app()
        if app == 'Day #29':
            day29.app()
        if app == 'Day #30':
            day30.app()
        if app == 'Day #31':
            day31.app()
    run()