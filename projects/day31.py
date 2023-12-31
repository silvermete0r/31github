import streamlit as st
import random

new_year_messages = [
    'Happy New Year! Hope you have a year filled with positivity.',
    'Wishing you and your family endless blessings this year. Happy New Year 2024!',
    'I hope your life is filled with surprises this year. Happy New Year!',
    'Wishing you a year filled with laughter. Happy New Year!',
    'Wishing you and your family a year filled with happiness. May this year bring lots of prosperity. Happy New Year!',
    'As you say goodbye to 2023, and welcome the year 2024, may happiness follow you always. Happy New Year!',
    'Wishing you a year of fulfillment and happiness. Happy New Year!',
    'May the new bring countless blessings to you and your family. Happy New Year!',
    'Wishing you a year of happiness and good luck. Happy New Year!',
    'May the new year bring lots of love and light to your family. Happy New Year!'
]

def app():
    st.title('Day #31 ')
    st.subheader('Happy New Year 2024 Streamlit App!')
    st.markdown('''
        This app is a last app for 2023 Github 31 Days of Streamlit Challenge.
                
        Reference: [Streamlit Community](https://streamlit.io/community)
    ''')
    st.write('---')

    st.markdown('### Happy New Year 2024')
    st.success(random.choice(new_year_messages))
    st.markdown('''
        #### Goals for 2024
        - Learn more about Data Science and Machine Learning;
        - Drive `Dataflow` organization to success in the field of research and development [DS/ML];
        - Learn more about `Tensorflow` and `PyTorch`;
        - Learn more about CI/CD and DevOps [`Docker` & `Github Actions`];
        - Get 10+ certifications in the field of Data Science and Machine Learning;
        - Become Kaggle Master & Full-Stack Expert;
        - Become a better person and a better professional;
    ''')
    st.image('media/happy-new-year-2024-dragon.png')
    stA, stB, _ = st.columns([2, 2, 5])
    if stA.button('Some ballons for you!'):
        st.balloons()
    if stB.button('Some snow for you!'):
        st.snow()