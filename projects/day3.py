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
    colA.subheader('1) Display Text', divider=True)
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
    colA.subheader('2) Display Data', divider=True)
    colA.code("st.dataframe(df[:5])", language='python')
    df = pd.read_excel('data/tglang_dataset.xlsx', engine='openpyxl')
    colA.dataframe(df[:5])
    colA.code("st.table(df[:5])", language='python')
    colA.table(df[:5])
    colA.code("st.json({'fullname':'Jon Jones', 'status': 'UFC Heavyweight Champion', 'age': 36})", language='python')
    colA.json({'fullname':'Jon Jones', 'status': 'UFC Heavyweight Champion', 'age': 36})
    colA.code("st.metric(label='Temperature', value='-23 °C', delta='-5 °C')", language='python')
    colA.metric(label='Temperature', value='-23 °C', delta='-5 °C')

    # 3) Display Media
    colA.subheader('3) Display Media', divider=True)
    colA.code("st.image('media/streamlit-logo.png', width=300)", language='python')
    colA.image('media/streamlit-logo.png', width=300)
    colA.code("st.audio('media/music.mp3', format='audio/mp3')", language='python')
    colA.audio('media/music.mp3', format='audio/mp3')
    colA.code("st.video('media/video.mp4', format='video/mp4')", language='python')
    colA.video('media/video.mp4', format='video/mp4')

    # 4) Display Columns
    colA.subheader('4) Display Columns', divider=True)
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
    colA.subheader('5) Display Tabs', divider=True)
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
    colA.subheader('6) Control Flow', divider=True)
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
    colB.subheader('7) Display interactive widgets', divider=True)
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
    colB.subheader('8) Display Progress and Status', divider=True)
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
    colC.subheader('9) Optimize performance', divider=True)
    colC.write('Cache Data Objects')
    colC.code('''
            # E.g. Dataframe computation, storing downloaded data, etc.
            >>> @st.cache_data
            ... def foo(bar):
            ...   # Do something expensive and return data
            ...   return data
            # Executes foo
            >>> d1 = foo(ref1)
            # Does not execute foo
            # Returns cached item by value, d1 == d2
            >>> d2 = foo(ref1)
            # Different arg, so function foo executes
            >>> d3 = foo(ref2)
            # Clear all cached entries for this function
            >>> foo.clear()
            # Clear values from *all* in-memory or on-disk cached functions
            >>> st.cache_data.clear()
            ''', language='python')
    colC.write('Cache Global Resources')
    colC.code('''
            # E.g. TensorFlow session, database connection, etc.
            >>> @st.cache_resource
            ... def foo(bar):
            ...   # Create and return a non-data object
            ...   return session
            # Executes foo
            >>> s1 = foo(ref1)
            # Does not execute foo
            # Returns cached item by reference, s1 == s2
            >>> s2 = foo(ref1)
            # Different arg, so function foo executes
            >>> s3 = foo(ref2)
            # Clear all cached entries for this function
            >>> foo.clear()
            # Clear all global resources from cache
            >>> st.cache_resource.clear()
            ''', language='python')
    colC.write('Deprecated caching')
    colC.code('''
            >>> @st.cache
            ... def foo(bar):
            ...   # Do something expensive in here...
            ...   return data
            >>> # Executes foo
            >>> d1 = foo(ref1)
            >>> # Does not execute foo
            >>> # Returns cached item by reference, d1 == d2
            >>> d2 = foo(ref1)
            >>> # Different arg, so function foo executes
            >>> d3 = foo(ref2)
            ''', language='python')

