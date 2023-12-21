import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import cv2

# Load the pre-trained MobileNetV2 model
@st.cache_resource()
def load_model():
    model = tf.keras.applications.mobilenet_v2.MobileNetV2(
        input_shape=None,
        alpha=1.0,
        include_top=True,
        weights='imagenet',
        input_tensor=None,
        pooling=None,
        classes=1000,
        classifier_activation='softmax'
    )
    return model

# Image Classification function
def classify_object(image):
    model = load_model()

    # Resize the image to fit the MobileNetV2 input size
    resized_img = cv2.resize(image, (224, 224))
    resized_img = np.expand_dims(resized_img, axis=0)

    try:
        # Preprocess the image for the MobileNetV2 model
        preprocessed_img = tf.keras.applications.mobilenet_v2.preprocess_input(resized_img)

        # Get model predictions
        predictions = model.predict(preprocessed_img)
        
        # Decode predictions
        decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions)

        # Extract top prediction
        top_prediction = decoded_predictions[0][0]

        return top_prediction[1], top_prediction[2]
    
    except Exception as e:
        st.warning("Image not recognized. Please try another one.")
        return None, None
        
# Main App Logic
def app():
    st.title('Day #10')
    st.subheader('Multi-Object Classifier Web App')
    st.markdown("""
        This app predicts the class of different objects in an image using a pre-trained MobileNetV2 model.
        
        * **Python libraries used:** `streamlit`, `tensorflow`, `OpenCV`, `Pillow`
                
        * **Pre-trained model:** [MobileNetV2](https://www.tensorflow.org/api_docs/python/tf/keras/applications/mobilenet_v2/MobileNetV2)
    """)
    st.write('---')

    uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image_array = np.array(image)
        st.image(image, caption="Uploaded Image", width=300)
        predicted_label, confidence_score = classify_object(image_array)
        if predicted_label is not None and confidence_score is not None:
            st.success(f"Prediction: {predicted_label} | Confidence Score: {confidence_score:.2%}")
    else:
        st.info('Please upload an image file (jpg, jpeg, or png).')