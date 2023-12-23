import streamlit as st
from qaznltk import qaznltk as qnltk

qn = qnltk.QazNLTK()

def app():
    st.title('Day #23')
    st.subheader('QazNLTK - kazakh language processing library based Web App')
    st.markdown('''
        This app show the basic usage of `QazNLTK` library.
                
        Reference: [QazNLTK](https://github.com/silvermete0r/QazNLTK)
    ''')
    st.write('---')

    st.image('media/qaznltk-logo.jpg', width=500)

    tabA, tabB, tabC, tabD = st.tabs(['About', 'Installation', 'Guideline', 'Try it out'])

    with tabA:
        st.markdown('### About')
        st.markdown('''
            QazNLTK provides developers with a fast and convenient tool for processing text in the Kazakh language. 
            Tailored for the unique linguistic characteristics of Kazakh, this library offers a comprehensive set of tools for natural language processing, like: 
             - tokenization;
             - sentence segmentation;
             - evaluation similarity score;
             - tranliteration of kazakh language cyrillic-latin;
             - sentiment analysis (in progress);
             - number to text;
        ''')

    with tabB:
        st.markdown('### Installation')
        st.code('pip install qaznltk')

        st.markdown('### Usage')
        st.code('''
            from qaznltk import QazNLTK as qnltk
            qn = qnltk.QazNLTK()
        ''', language='python')

    with tabC:
        st.markdown('### Guideline')
        with st.expander('Tokenization'):
            st.markdown('''
                #### Tokenization
                Tokenization is the process of breaking a stream of text up into words, phrases, symbols, or other meaningful elements called tokens.
            ''')
            st.caption('Code:')
            st.code('''
                text = input("Enter text: ")
                tokens = qn.tokenize(text)
                print(tokens)
            ''', language='python')
            st.caption('Input:')
            st.write('Біздің өміріміз үлкен өзен іспетті. Сіздің қайығыңыздың қиындықтардан жеңіл өтіп, махаббат иірімінде басқаруын жоғалтпай, бақыт сарқырамасына жетуін тілеймін!')
            st.caption('Output:')
            st.write([('өміріміз', 1), ('үлкен', 1), ('өзен', 1), ('іспетті', 1), ('сіздің', 1), ('қайығыңыздың', 1), ('қиындықтардан', 1), ('жеңіл', 1), ('өтіп', 1), ('махаббат', 1), ('иірімінде', 1), ('басқаруын', 1), ('жоғалтпай', 1), ('бақыт', 1), ('сарқырамасына', 1), ('жетуін', 1), ('тілеймін', 1)])
        
        with st.expander('Text Segmentation'):
            st.markdown('''
                #### Text Segmentation
                Text segmentation is the process of dividing written text into meaningful units, such as words, sentences, or topics.
            ''')
            st.caption('Code:')
            st.code('''
                text = input("Enter text: ")
                sent_tokens = qn.sent_tokenize(text)
                print(sent_tokens)
            ''', language='python')
            st.caption('Input:')
            st.write('Біздің өміріміз үлкен өзен іспетті. Сіздің қайығыңыздың қиындықтардан жеңіл өтіп, махаббат иірімінде басқаруын жоғалтпай, бақыт сарқырамасына жетуін тілеймін!')
            st.caption('Output:')
            st.write(['Біздің өміріміз үлкен өзен іспетті.', 'Сіздің қайығыңыздың қиындықтардан жеңіл өтіп, махаббат иірімінде басқаруын жоғалтпай, бақыт сарқырамасына жетуін тілеймін!'])
        
        with st.expander('Difference score'):
            st.markdown('''
                #### Difference score
                Difference score is the process of comparing two texts and calculating the difference score.            
            ''')
            st.caption('Code:')
            st.code('''
                textA = input("Enter text A: ")
                textB = input("Enter text B: ")
                similarity_score = qn.calc_similarity(textA, textB)
                print(similarity_score)
            ''', language='python')
            st.caption('Input:')
            st.write('Text A: Еңбегіне қарай — құрмет, Жасына қарай — ізет.')
            st.write('Text B: Еңбегіне қарай табысы, Ерлігіне қарай дабысы.')
            st.caption('Output:')
            st.write(0.2222222222222222)

        with st.expander('Transliteration'):
            st.markdown('''
                #### Transliteration
                Transliteration is the process of converting a text from one script to another.
                * From cyrillic to latin;
                * From latin to cyrillic.    
            ''')
            st.markdown('##### From cyrillic to latin')
            st.caption('Code:')
            st.code('''
                # From cyrillic to latin
                text = input("Enter text: ")
                latin_text = qn.convert2latin(text)
                print(latin_text)
            ''', language='python')
            st.caption('Input:')
            st.write('Бүгін қандай керемет күн!')
            st.caption('Output:')
            st.write('Bùgìn k̦andaj keremet kùn!')

            st.markdown('##### From latin to cyrillic')
            st.caption('Code:')
            st.code('''
                # From latin to cyrillic
                text = input("Enter text: ")
                cyrillic_text = qn.convert2cyrillic(text)
                print(cyrillic_text)
            ''', language='python')
            st.caption('Input:')
            st.write('Bùgìn k̦andaj keremet kùn!')
            st.caption('Output:')
            st.write('Бүгін қандай керемет күн!')
        
        with st.expander('Sentiment Analysis'):
            st.markdown('''
                #### Text Segmentation
                Text segmentation is the process of dividing written text into meaningful units, such as words, sentences, or topics.
            ''')
            st.caption('Code:')
            st.code('''
                text = input("Enter text: ")
                sentimize_score = qnltk.sentimize(text)
                print(sentimize_score)
            ''', language='python')
            st.caption('Input:')
            st.write('Бұл мақала өте нашар жазылған.')
            st.caption('Output:')
            st.write('-1 (negative)')

        with st.expander('Number to text'):
            st.markdown('''
                #### Number to text
                Number to text is the process of converting a number to text.
            ''')
            st.caption('Code:')
            st.code('''
                n = int(input())
                print(qnltk.num2word(n))
            ''', language='python')
            st.caption('Input:')
            st.write('1465')
            st.caption('Output:')
            st.write('мың төрт жүз алпыс бес')

    with tabD:
        st.markdown('### Try it out')
        with st.expander('Tokenization'):
            text = st.text_area('Enter text:', height=200, key='tokenize')
            if st.button('Tokenize'):
                with st.spinner('Tokenizing...'):
                    if text == '':
                        st.error('Text is empty!')
                        st.stop()
                    tokens = qn.tokenize(text)
                    st.write(tokens)
                    st.success('Done')


        with st.expander('Text Segmentation'):
            text = st.text_area('Enter text:', height=200, key='segment')
            if st.button('Segment'):
                with st.spinner('Segmenting...'):
                    if text == '':
                        st.error('Text is empty!')
                        st.stop()
                    sent_tokens = qn.sent_tokenize(text)
                    st.write(sent_tokens)
                    st.success('Done')

        with st.expander('Difference score'):
            textA = st.text_area('Enter text A:', height=200, key='diffA')
            textB = st.text_area('Enter text B:', height=200, key='diffB')
            if st.button('Calculate'):
                with st.spinner('Calculating...'):
                    if textA == '' or textB == '':
                        st.error('Text is empty!')
                        st.stop()
                    similarity_score = qn.calc_similarity(textA, textB)
                    st.write(similarity_score)
                    st.success('Done')

        with st.expander('Transliteration'):
            choice = st.radio('Choose:', ['From cyrillic to latin', 'From latin to cyrillic'], index=0)
            if choice == 'From cyrillic to latin':
                text = st.text_area('Enter text:', height=200, key='c2l')
                if st.button('Convert'):
                    with st.spinner('Converting...'):
                        if text == '':
                            st.error('Text is empty!')
                            st.stop()
                        latin_text = qn.convert2latin(text)
                        st.write(latin_text)
                        st.success('Done')
            else:
                text = st.text_area('Enter text:', height=200, key='l2c')
                if st.button('Convert'):
                    with st.spinner('Converting...'):
                        if text == '':
                            st.error('Text is empty!')
                            st.stop()
                        cyrillic_text = qn.convert2cyrillic(text)
                        st.write(cyrillic_text)
                        st.success('Done')
        
        with st.expander('Sentiment Analysis'):
            text = st.text_area('Enter text', height=200, key='sentimize')
            if st.button('Analyze'):
                with st.spinner('Analyzing...'):
                    if text == '':
                        st.error('Text is empty!')
                        st.stop()
                    sentimize_score = qn.sentimize(text)
                    st.write(sentimize_score)
                    st.success('Done')

        with st.expander('Number to text'):
            n = st.number_input('Enter number:', min_value=0, max_value=1000000000000000, value=1465, step=1)
            if st.button('Convert to text'):
                with st.spinner('Converting...'):
                    if n == 0:
                        st.error('Number is empty!')
                        st.stop()
                    st.write(qn.num2word(n))
                    st.success('Done')