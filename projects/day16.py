import streamlit as st
from transformers import pipeline

@st.cache_resource()
def load_model():
    model = pipeline('text-generation', model='gpt2')
    return model

def app():
    st.title('Day #16')
    st.subheader('Text Completion using HuggingFace Transformers')
    st.markdown("""
        This app is a simple text completion app using GPT-2 model from HuggingFace Transformers.
                
        The model used is `GPT-2` WebText-data-based pre-trained model. The model is fine-tuned on a dataset of 8 million+ web pages and has 1.5 billion parameters. Initial Release of GPT-2 was in February 2019.
                
        Reference: [HuggingFace Transformers](https://huggingface.co/transformers/model_doc/gpt2.html)
    """)
    st.write('---')

    st.markdown('### Input Text for Completion')
    text = st.text_area('Enter Text', height=200)
    if text == '':
        st.warning('Please enter some text for completion')
    if st.button('Complete'):
        with st.spinner('Completing...'):
            model = load_model()
            completed_text = model(text)
        st.markdown('### Output')
        st.write(completed_text)
        st.success('Done!')

