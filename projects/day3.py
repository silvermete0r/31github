import streamlit as st
import pandas as pd
import openpyxl

def app():
    st.title('Day #3')
    colx, coly = st.columns([1, 1])
    colx.subheader('Streamlit Toolkit 🧰')
    colx.markdown('''
    - **Streamlit Cheat Sheet** [[streamlit.io](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py)]
    - **Streamlit Apps Gallery** [[streamlit.io](https://streamlit.io/gallery)]
    - **Streamlit Components Gallery** [[streamlit.io](https://www.streamlit.io/components)]
    - **Streamlit 30 Day Challenge** [[streamlit.io](https://www.streamlit.io/30day-challenge)]
    - **Streamlit Community** [[streamlit.io](https://discuss.streamlit.io/)]
    - **Streamlit Documentation** [[streamlit.io](https://docs.streamlit.io/en/stable/)]
    @daniellewisdl 
    ''')

    colx.subheader('Run Streamlit App via Conda')
    colx.code('''
            # Create a new conda environment
            $ conda create --name myenv python=3.9
            
            # Activate the conda environment
            $ conda activate myenv

            # Run Streamlit App
            $ streamlit run app.py              
              ''', language='python')

    coly.subheader('Command Line and Terminal')
    coly.code('''
            $ streamlit --help
            $ streamlit run your_script.py
            $ streamlit hello
            $ streamlit config show
            $ streamlit cache clear
            $ streamlit docs
            $ streamlit --version
            ''', language='python')
    
    coly.subheader('Install & Import Streamlit')
    coly.code('''
            # Install Streamlit via pip
            $ pip install streamlit

            # Import Streamlit in Python
            import streamlit as st
              ''', language='python')
    

    st.subheader('Streamlit Components')

    colA, colB, colC = st.columns([1, 1, 1])
    
    # 1) Display Text
    colA.subheader('1) Display Text')
    colA.code("st.text('It\'s a fixed width text.')", language='python')
    colA.text('It\'s a fixed width text.')
    colA.code("st.markdown(':smile:')", language='python')
    colA.markdown('It\'s a markdown text :smile:')
    colA.code("st.latex('F= G \\frac{m_1 m_2}{r^2}')", language='python')
    colA.latex('F= G \\frac{m_1 m_2}{r^2}')
    colA.code("st.write('Most objects: df, err, func, etc.')", language='python')
    colA.write('Most objects: df, err, func, etc.')
    colA.code("st.title('My Title!')", language='python')
    colA.title('My Title!')
    colA.code("st.header('My Header!')", language='python')
    colA.header('My Header!')
    colA.code("st.subheader('My Subheader!')", language='python')
    colA.subheader('My Subheader!')
    colA.code("st.caption('My Caption!')", language='python')
    colA.caption('My Caption!')
    colA.code("st.code('print(\'Hello, World!\')')", language='python')
    colA.code('print(\'Hello, World!\')')

    # 2) Display Data
    colA.subheader('2) Display Data')
    colA.code("st.dataframe(df[:5])", language='python')

    @st.cache_data
    def load_data(url):
        df = pd.read_excel(url, engine='openpyxl')
        return df
    
    df = load_data('data/tglang_dataset.xlsx')
    colA.dataframe(df[:5])
    colA.code("st.table(df[:5])", language='python')
    colA.table(df[:5])
    colA.code("st.json({'fullname':'Jon Jones', 'status': 'UFC Heavyweight Champion', 'age': 36})", language='python')
    colA.json({'fullname':'Jon Jones', 'status': 'UFC Heavyweight Champion', 'age': 36})
    colA.code("st.metric(label='Temperature', value='-23 °C', delta='-5 °C')", language='python')
    colA.metric(label='Temperature', value='-23 °C', delta='-5 °C')

    # 3) Display Media
    colA.subheader('3) Display Media')
    colA.code("st.image('media/streamlit-logo.png', use_column_width=True)", language='python')
    colA.image('media/streamlit-logo.png', use_column_width=True)
    colA.code("st.audio('media/music.mp3', format='audio/mp3')", language='python')
    colA.audio('media/music.mp3', format='audio/mp3')
    colA.code("st.video('media/video.mp4', format='video/mp4')", language='python')
    colA.video('media/video.mp4', format='video/mp4')

    # 4) Display Columns
    colA.subheader('4) Display Columns')
    colA.code('''
            col1, col2 = st.columns([1, 1])
            with col1:
              st.subheader('Left Title')
              st.code('def left()')
            with col2:
              st.subheader('Right Title')
              st.code('def right()')
              ''', language='python')
    col1, col2 = colA.columns([1, 1])
    with col1:
        st.subheader('Left Title')
        st.code('def left()')
    with col2:
        st.subheader('Right Title')
        st.code('def right()')
    
    # 5) Display Tabs
    colA.subheader('5) Display Tabs')
    colA.code('''
            tab1, tab2, tab3, tab4 = st.tabs(['Fire', 'Water', 'Earth', 'Air'])
            tab1.write('Fire is hot')
            tab2.write('Water is wet')
            tab3.write('Earth is hard')
            tab4.write('Air is fresh')
            ''', language='python')
    tab1, tab2, tab3, tab4 = colA.tabs(['Fire', 'Water', 'Earth', 'Air'])
    tab1.write('Fire is hot')
    tab2.write('Water is wet')
    tab3.write('Earth is hard')
    tab4.write('Air is fresh')


    # 6) Control Flow
    colA.subheader('6) Control Flow')
    colA.code('''
            # Stop execution immediately
            st.stop()

            # Rerun script immediately
            st.experimental_rerun()
            
            # Group Multiple Widgets
            with st.form(key='my_form'):
                username = st.text_input('Username')
                password = st.text_input('Password')
                st.form_submit_button('Login')            
            ''', language='python')
    
    with colA.form(key='my_form'):
        username = st.text_input('Username')
        password = st.text_input('Password')
        st.form_submit_button('Login')  

    # 7) Display interactive widgets
    colB.subheader('7) Display interactive widgets')
    colB.code("st.button('Hit me')", language='python')
    colB.button('Hit me')
    colB.code("st.data_editor(df)", language='python')
    colB.data_editor(df)
    colB.code("st.checkbox('Check me out')", language='python')
    colB.checkbox('Check me out')
    colB.code("st.radio('Pick one:', ['nose','ear'])", language='python')
    colB.radio('Pick one:', ['nose','ear'])
    colB.code("st.selectbox('Select', [1,2,3])", language='python')
    colB.selectbox('Select', [1,2,3])
    colB.code("st.multiselect('Multiselect', [1,2,3])", language='python')
    colB.multiselect('Multiselect', [1,2,3])
    colB.code("st.slider('Slide me', min_value=0, max_value=10)", language='python')
    colB.slider('Slide me', min_value=0, max_value=10)
    colB.code("st.select_slider('Slide to select', options=[1,'2'])", language='python')
    colB.select_slider('Slide to select', options=[1,'2'])
    colB.code("st.text_input('Enter some text')", language='python')
    colB.text_input('Enter some text')
    colB.code("st.number_input('Enter a number')", language='python')
    colB.number_input('Enter a number')
    colB.code("st.text_area('Area for textual entry')", language='python')
    colB.text_area('Area for textual entry')
    colB.code("st.date_input('Date input')", language='python')
    colB.date_input('Date input')
    colB.code("st.time_input('Time entry')", language='python')
    colB.time_input('Time entry')
    colB.code("st.file_uploader('File uploader')", language='python')
    colB.file_uploader('File uploader')
    text_contents = '''
        Foo, Bar
        123, 456
        789, 000
    '''
    colB.code("st.download_button('Download File', text_contents)", language='python')
    colB.download_button('Download File', text_contents)
    colB.code("st.camera_input('I wanna take camera shot, don\'t move:)')", language='python')
    colB.camera_input('I wanna take camera shot, don\'t move:)')
    colB.code("st.color_picker('Pick a color')", language='python')
    colB.color_picker('Pick a color')

    # 8) Display Progress and Status
    colB.subheader('8) Display Progress and Status')
    colB.code("st.progress(0.3)", language='python')
    colB.progress(0.3)
    colB.code('''
                import time
                if st.button('Start'):
                    my_bar = st.progress(0)
                    for percent_complete in range(100):
                        time.sleep(0.1)
                        my_bar.progress(percent_complete + 1)
                    st.success('Done!')
            ''')
    import time
    if colB.button('Start'):
        my_bar = colB.progress(0)
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
        colB.success('Done!')

    # 9) Optimize performance
    colC.subheader('9) Optimize performance')

    colC.image('media/cache.png', use_column_width=True)

    colC.markdown('''**Cache Data Objects**\n 
`st.cache_data` is the recommended way to cache computations that return data: 
loading a DataFrame from CSV, transforming a NumPy array, querying an API, 
or any other function that returns a serializable data object (str, int, float, 
DataFrame, array, list, …). It creates a new copy of the data at each function 
call, making it safe against mutations and race conditions. The behavior of 
`st.cache_data` is what you want in most cases – so if you\'re unsure, start 
with `st.cache_data` and see if it works!''')
    
    colC.code('''
            @st.cache_data  # 👈 Add the caching decorator
            def load_data(url):
                df = pd.read_csv(url)
                return df

            df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
            st.dataframe(df)

            st.button("Rerun")
            ''', language='python')
    
    colC.markdown('''**Cache Global Resources**\n 
`st.cache_resource` is the recommended way to cache global resources like ML models 
or database connections – unserializable objects that you don't want to load multiple 
times. Using it, you can share these resources across all reruns and sessions of an 
app without copying or duplication. Note that any mutations to the cached return value 
directly mutate the object in the cache.''')
    
    colC.code('''
            from transformers import pipeline

            @st.cache_resource  # 👈 Add the caching decorator
            def load_model():
                return pipeline("sentiment-analysis")

            model = load_model()

            query = st.text_input("Your query", value="I love Streamlit! 🎈")
            if query:
                result = model(query)[0]  # 👈 Classify the query text
                st.write(result)
            ''', language='python')


    # 10) Display Animations
    colC.subheader('10) Display Animations')
    colC.code("st.balloons()", language='python')
    if colC.button('Give me balloons!'):
        colC.balloons()
    colC.code("st.snow()", language='python')
    if colC.button('Let it snow!'):
        colC.snow()
    colC.code("st.toast('Here is your toast!')", language='python')
    if colC.button('Give me a toast!'):
        st.toast('Here is your toast!')
    colC.code("st.success('Here is your success!')", language='python')
    if colC.button('Give me a success!'):
        colC.success('Here is your success!')
    colC.code("st.info('Here is your info!')", language='python')
    if colC.button('Give me a info!'):
        colC.info('Here is your info!')
    colC.code("st.warning('Here is your warning!')", language='python')
    if colC.button('Give me a warning!'):
        colC.warning('Here is your warning!')
    colC.code("st.error('Here is your error!')", language='python')
    if colC.button('Give me a error!'):
        colC.error('Here is your error!')
    colC.code("st.exception('Here is your exception!')", language='python')
    if colC.button('Give me a exception!'):
        colC.exception('Here is your exception!')
    colC.code('''
              with st.spinner('Wait for it...')
                time.sleep(5)
                st.success('Done!')
              ''', language='python')
    if colC.button('Give me a spinner!'):
        colC.info('Go down to see the spinner!')
        with st.spinner('Wait for it...'):
            time.sleep(5)
            st.success('Done!')