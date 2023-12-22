import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

MAX_FILE_SIZE = 5 * 1024 * 1024 # 5MB

# Convert image to bytes
def convert_image(img):
    buffered = BytesIO()
    img.save(buffered, format='PNG')
    byte_img = buffered.getvalue()
    return byte_img

# Background removal function
def remove_background(upload, col1, col2):
    img = Image.open(upload)
    col1.write('Original Image:')
    col1.image(img)

    removed = remove(img)
    col2.write('Background Removed:')
    col2.image(removed) 
    
    st.download_button("Download Fixed Image", convert_image(removed), file_name="fixed.png", mime="image/png")

def app():
    st.title('Day #22')
    st.subheader('Image Background Remover Web App')
    st.markdown('''
        This app removes the background of an image using a python `rembg` module.
    
        Reference: [tyler-simons/BackgroundRemoval](https://github.com/tyler-simons/BackgroundRemoval)
    ''')
    st.write('---')

    st.markdown('''### Upload an image:''')
    uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

    col1, col2 = st.columns(2)

    if uploaded_file is not None:
        if uploaded_file.size > MAX_FILE_SIZE:
            st.error('File size exceeds maximum allowed size of 5MB.')
        else:
            remove_background(uploaded_file, col1, col2)
            st.success('Image successfully processed.')
    else:
        remove_background('media/lebron.png', col1, col2)