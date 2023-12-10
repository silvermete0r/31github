import streamlit as st
import cv2
import face_recognition
import numpy as np

def app():
    st.title('Day #9')
    st.subheader('Face Recognition Web App')
    st.markdown("""
        This app detects faces in uploaded images using `face_recognition` library.
        
        * **Python libraries used:** `streamlit`, `opencv-python`, `face_recognition`
                
        * **References:** [Face Recognition](https://pypi.org/project/face-recognition/)
    """)
    st.write('---')

    uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), -1)

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        st.image(rgb_image, caption="Uploaded Image", width=300)

        face_locations = face_recognition.face_locations(rgb_image)
        if face_locations:
            st.success("Found {} face(s)!".format(len(face_locations)))

            for id, face_location in enumerate(face_locations):
                top, right, bottom, left = face_location
                cv2.rectangle(rgb_image, (left, top), (right, bottom), (0, 255, 0), 2)
                st.write(f'Face #{id+1}:')
                st.image(rgb_image, caption="Processed Image", width=300)

            download_img = cv2.imencode('.jpg', rgb_image)[1].tobytes()
            st.download_button(label="Download Image", data=download_img, file_name="enhanced_image.jpg", mime="image/jpg")
        else:
            st.warning("No faces found in the uploaded image. Please try another one.")