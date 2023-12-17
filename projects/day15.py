import streamlit as st
from transformers import pipeline

@st.cache_resource()
def load_model():
    model = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')
    return model

def app():
    st.title('Day #15')
    st.subheader('Text Sentiment Analysis using HuggingFace Transformers')
    st.markdown("""
        This app is a simple text sentiment analysis app using `BERT` model from HuggingFace Transformers.
                
        The model used is `nlptown/bert-base-multilingual-uncased-sentiment` which is a BERT model fine-tuned on IMDB dataset.
                
        Reference: [HuggingFace Transformers](https://huggingface.co/transformers/)
    """)
    st.write('---')
    
    st.markdown('### Input Text for Sentiment Analysis')
    text = st.text_area('Text', height=200)
    if st.button('Analyze'):
        if text == '':
            st.warning('Please enter some text for sentiment analysis')
        else:
            with st.spinner('Analyzing...'):
                model = load_model()
                result = model(text)
            st.markdown('### Output')
            st.write(result)
            st.success('Done!')