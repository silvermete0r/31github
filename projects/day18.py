import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

@st.cache_resource()
def load_model():
    model_name = 'Helsinki-NLP/opus-mt-en-fr'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    return model, tokenizer

def translate_text(text, source_lang="en", target_lang="fr"):
    model, tokenizer = load_model()
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding="longest", max_length=512)
    translated = model.generate(**inputs, max_length=128)
    translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)[0]
    return translated_text


def app():
    st.title('Day #18')
    st.subheader('Text English to French Language Translation App')
    st.markdown('''
        This app uses the `Helsinki-NLP/opus-mt-en-fr` model to translate English text to French. 
    
        Reference: [HuggingFace Transformers](https://huggingface.co/transformers/)
    ''')
    st.write('---')

    st.markdown('### Input Text in `English` for Translation to `French`')
    text = st.text_area('Enter text', height=200)

    if st.button('Translate'):
        with st.spinner('Translating...'):
            translated_text = translate_text(text)
        st.markdown('### Output')
        st.write(translated_text)
        st.success('Done!')