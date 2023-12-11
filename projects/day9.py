import streamlit as st
import cv2
import numpy as np

def app():
    st.title('Day #9')
    st.subheader('Face Recognition Web App')
    st.markdown("""
        This app detects faces in uploaded images using Haar Cascades.
        
        * **Python libraries used:** `streamlit`, `opencv-python`
                
        * **References:** [OpenCV Haar Cascades](https://docs.opencv.org/4.x/da/d60/tutorial_face_main.html)
    """)
    st.write('---')

    face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

    uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), -1)

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        st.image(rgb_image, caption="Uploaded Image", width=300)

        gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5)

        if len(faces) > 0:
            st.success(f"Found {len(faces)} faces in the image.")

            for idx, (x, y, w, h) in enumerate(faces):
                cv2.rectangle(rgb_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                st.write(f"Face #{idx+1}")
                st.image(rgb_image[y:y+h, x:x+w], caption='Processed Image', width=300)
                
            download_img = cv2.imencode('.jpg', rgb_image)[1].tobytes()
            st.download_button(label="Download Image", data=download_img, file_name="enhanced_image.jpg", mime="image/jpg")
        else:
            st.warning("No faces found in the uploaded image. Please try another one.")