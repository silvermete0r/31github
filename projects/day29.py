import streamlit as st

def app():
    st.title('Day #29')
    st.subheader('Brain Tumor Detection using TensorFlow')
    st.markdown('''
        This app is a demo of Brain Tumor Detection using TensorFlow.
                
        Reference: [Tensorflow Guide](https://www.tensorflow.org/)
    ''')
    st.write('---')

    st.subheader('Install TensorFlow')
    st.code('!pip install tensorflow')

    st.subheader('Import Libraries')
    st.code('''
        import tensorflow as tf
        from tensorflow.keras.preprocessing import image
        import numpy as np
    ''')

    st.subheader('Load Model')
    st.code('''
        model = tf.keras.models.load_model('model.h5')
    ''')

    st.subheader('Load Image')
    st.code('''
        img = image.load_img('test_image.jpg', target_size=(64, 64))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
    ''')

    st.subheader('Predict Image')
    st.code('''
        prediction = model.predict(img)
        prediction = np.argmax(prediction, axis=1)
    ''')

    st.subheader('Display Prediction')
    st.code('''
        if prediction == 0:
            st.write('Brain Tumor Detected')
        else:
            st.write('Brain Tumor Not Detected')
    ''')