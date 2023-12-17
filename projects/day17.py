import streamlit as st
from transformers import pipeline

@st.cache_resource()
def load_model():
    model = pipeline('ner', model='dslim/bert-base-NER', grouped_entities=True)
    return model

def app():
    st.title('Day #17')
    st.subheader('Named Entity Recognition (NER) using BERT model from HuggingFace')
    st.markdown('''
        This app helps to identify the entities in a given text. The `bert-base-NER` model used from HuggingFace.
                
        Reference: [HuggingFace Transformers]('https://huggingface.co/dslim/bert-base-NER')
    ''')
    st.write('---')

    st.markdown('### Input Text for NER')
    text = st.text_area('Enter text', height=200)
    if st.button('Submit'):
        if text == '':
            st.warning('Please enter some text for NER')
        else:
            with st.spinner('Identifying entities..'):
                model = load_model()
                result = model(text)
            st.markdown('### Output')
            st.write(result)
            st.success('Done!')