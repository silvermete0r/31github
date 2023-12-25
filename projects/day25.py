import streamlit as st
from PIL import Image
from io import BytesIO
import base64
import cv2

# Convert image to bytes
def convert_image(img):
    buffered = BytesIO()
    img.save(buffered, format='PNG')
    byte_img = buffered.getvalue()
    return byte_img

def app():
    st.title('Day #25')
    st.subheader('Certificate of Completion Generator')
    st.markdown('''
        This app is a simple certificate of completion generator using `OpenCV` and `Pillow`.
                
        Reference: [OpenCV Docs](https://docs.opencv.org/4.x/)
    ''')
    st.write('---')

    st.markdown('### Enter your Full Name:')
    name = st.text_input('Name', 'Kazbek Kazbekov')

    template_path = 'media/certificate-template.png'
    certificate_path = 'media/fixed_certificate.png'
    font_size = 3
    font_color = (0, 0, 0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    coordinate_y_adjustment = 15
    coordinate_x_adjustment = 7

    if st.button('Generate'):
        with st.spinner('Generating...'):
            img = cv2.imread(template_path)
            text_size = cv2.getTextSize(name, font, font_size, 10)[0]
            text_x = (img.shape[1] - text_size[0]) / 2 + coordinate_x_adjustment
            text_y = (img.shape[0] + text_size[1]) / 2 - coordinate_y_adjustment
            text_x = int(text_x)
            text_y = int(text_y)
            cv2.putText(img, name, (text_x, text_y), font, font_size, font_color, 10)
            cv2.imwrite(certificate_path, img)
            st.image(certificate_path)
            st.download_button('Download', convert_image(Image.open(certificate_path)), file_name="certificate_fixed.png", mime="image/png")
        st.success('Done!')