import streamlit as st
from transformers import pipeline

@st.cache_resource()
def load_model():
    model = pipeline('summarization', model='facebook/bart-large-cnn')
    return model

def generate_chunks(inp_str):
    max_chunk = 500
    inp_str = inp_str.replace('.', '.<eos>')
    inp_str = inp_str.replace('?', '?<eos>')
    inp_str = inp_str.replace('!', '!<eos>')

    sentences = inp_str.split('<eos>')
    current_chunk = 0
    chunks = []

    for sentence in sentences:
        if len(chunks) == current_chunk + 1:
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            chunks.append(sentence.split(' '))
    
    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])
    
    return chunks

def app():
    st.title('Day #14')
    st.subheader('Text Summarization using HuggingFace Transformers')   
    st.markdown("""
        This app is a simple text summarization app using `BART` model from HuggingFace Transformers.
        
        The model used is `facebook/bart-large-cnn` which is a BART model fine-tuned on CNN/DailyMail dataset.
        
        Reference: [HuggingFace Transformers](https://huggingface.co/transformers/) 
        
        Mention: [Ahmed Hafez](https://www.kaggle.com/code/ahmedtronic/text-summarization-huggingface)
    """)
    st.write('---')
    
    st.markdown('### Input Text for Summarization')
    text = st.text_area('Text', height=300)
    max_length = st.slider('Max Length', 100, 500, 200)
    min_length = st.slider('Min Length', 10, 100, 30)
    if text == '':
        st.warning('Please enter some text for summarization')
    if max_length <= min_length:
        st.warning('Max Length should be greater than Min Length')
    if st.button('Summarize'):
        with st.spinner('Summarizing...'):
            model = load_model()
            chunks = generate_chunks(text)
            summary = model(chunks, max_length=max_length, min_length=min_length)
            summary_text = ' '.join([summ['summary_text'] for summ in summary])
        st.markdown('### Output')
        st.write(summary_text)
        st.success('Done!')
    