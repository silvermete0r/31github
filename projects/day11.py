import streamlit as st
import tensorflow as tf
import keras
import time

'''
# Load MNIST Dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Show 5 Images
for i in range(5):
    st.image(x_train[i], use_column_width=True)

# Data Preprocessing
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build Model
model = tf.keras.models.Sequential([
    # Input Layer (Flatten)
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    # Hidden Layer (Dense)
    tf.keras.layers.Dense(128, activation='relu'),
    # Dropout Layer
    tf.keras.layers.Dropout(0.2),
    # Output Layer (Dense)
    tf.keras.layers.Dense(10)
])

# Compile Model
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])

# Train Model
model.fit(x_train, y_train, epochs=5)

# Evaluate Model
model.evaluate(x_test, y_test, verbose=2)

# Download Model
model.save('models/day11.h5')
'''

def app():
    st.title('Day #11')
    st.subheader('Tensorflow Image Classification DL Model Training Baseline')
    st.markdown("""
        This app trains a simple CNN model on the MNIST dataset using Tensorflow.
        
        * **Python libraries used:** `streamlit`, `tensorflow`
                
        * **Dataset used:** [MNIST](https://keras.io/api/datasets/mnist/)
        
        * **MNIST:** *Modified National Institute of Standards and Technology - is a large database of handwritten digits that is commonly used for training various image processing systems.*
        
        * **References:** [Tensorflow Guide](https://www.tensorflow.org/guide)
    """)
    with st.expander('What is Tensorflow?', expanded=True):
        colA, colB = st.columns([2, 5])
        colA.image('https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Tensorflow_logo.svg/1280px-Tensorflow_logo.svg.png', width=200)
        colB.markdown("""
            * **TensorFlow** is a free and open-source software library for `machine learning` and `artificial intelligence`.
            * It was developed by the Google Brain team for internal Google use. It was released under the Apache License 2.0 on November 9, 2015.
            * It can be used across a range of tasks but has a particular focus on training and inference of `deep neural networks`.
            * **Tensorflow** is a symbolic math library based on `dataflow` and `differentiable programming`.
            * It is used for both research and production at Google.
            * It can be used in wide variety of languages such as `Python`, `JavaScript`, `C++` & `Java`.
            * **Official Website:** [tensorflow.org](https://www.tensorflow.org/) | **Github:** [Tensorflow](https://github.com/tensorflow/tensorflow) | **Source:** [Wikipedia](https://en.wikipedia.org/wiki/TensorFlow)
        """)
        st.write('---')
        st.caption('TensorFlow Architecture')
        st.image('media/tf-architecture.png', use_column_width=True)
    st.write('---')

    # Evaluation Results
    eval_results = {
        'loss': 0.074,
        'accuracy': 0.977
    }

    ##############################
    # Step-1: Install Tensorflow #
    ##############################
    st.markdown('### 1. Tensorflow Installation')
    st.code("""
        pip install tensorflow
    """, language='python')
    if st.button('Install Tensorflow'):
        with st.spinner('Installing Tensorflow...'):
            time.sleep(1)
            st.success('Tensorflow Installed!')
    st.write('---')

    ##############################
    # Step-2: Load MNIST Dataset #
    ##############################
    st.markdown('### 2. Load MNIST Dataset')
    st.code("""
        mnist = tf.keras.datasets.mnist
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
    """, language='python')
    if st.button('Load Dataset'):
        with st.spinner('Loading Dataset...'):
            time.sleep(1.5)
            st.success('Dataset Loaded!')
            st.caption('Sample Images:')
            col1, col2, col3, col4, col5 = st.columns(5)
            for idx, img_id in enumerate((0, 1, 4, 5, 9)):
                eval(f'col{idx+1}').image(f'media/digit-{img_id}.jpg', use_column_width=True)
    st.write('---')

    ##############################
    # Step-3: Data Preprocessing #
    ##############################
    st.markdown('### 3. Data Preprocessing')
    st.code("""
        x_train, x_test = x_train / 255.0, x_test / 255.0
    """, language='python')
    if st.button('Preprocess Data'):
        with st.spinner('Preprocessing Data...'):
            time.sleep(1)
            st.success('Data Preprocessed!')
    st.write('---')

    #######################
    # Step-4: Build Model #
    #######################
    st.markdown('### 4. Build Model')
    st.code("""
        model = tf.keras.models.Sequential([
            # Input Layer (Flatten)
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            # Hidden Layer (Dense)
            tf.keras.layers.Dense(128, activation='relu'),
            # Dropout Layer
            tf.keras.layers.Dropout(0.2),
            # Output Layer (Dense)
            tf.keras.layers.Dense(10)
        ])
    """, language='python')
    with st.expander('Architecture of the Network'):
        st.markdown("""
            * **Input Layer** for 28x28 images in MNiST Dataset.
            * **Dense layer** with 128 neurons and ReLU activation function.
            * **Output layer** with 10 neurons for classification of input images as one of ten digits (0-9).
        """)
    if st.button('Build Model'):
        with st.spinner('Building Model...'):
            time.sleep(1)
            st.success('Model Built!')
    st.write('---')
    
    #########################
    # Step-5: Compile Model #
    #########################
    st.markdown('### 5. Compile Model')
    st.code("""
        loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
        model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])
    """, language='python')
    with st.expander('What are Loss Functions, Optimizers & Metrics?'):
        st.markdown("""
            * **Loss Functions** are used to measure how well the model did on training.
            * **Optimizers** are used to improve the model based on the loss function.
            * **Metrics** are used to monitor the training and testing steps.
        """)
    if st.button('Compile Model'):
        with st.spinner('Compiling Model...'):
            time.sleep(1.5)
            st.success('Model Compiled!')
    st.write('---')
        
    #######################
    # Step-6: Train Model #
    #######################
    st.markdown('### 6. Train Model')
    st.code("""
        model.fit(x_train, y_train, epochs=5)
    """, language='python')
    with st.expander('What are Epochs?'):
        st.markdown("""
            * **Epochs** are the number of times the model will cycle through the data.
            * **1 Epoch** is when an entire dataset is passed both forward and backward through the neural network only once.
        """)
    if st.button('Train Model'):
        with st.spinner('Training Model...'):
            time.sleep(2.5)
            st.success('Model Trained!')
    st.write('---')
    
    ##########################
    # Step-7: Evaluate Model #
    ##########################
    st.markdown('### 7. Evaluate Model')
    st.code("""
        model.evaluate(x_test, y_test, verbose=2)
    """, language='python')
    if st.button('Evaluate Model'):
        # st spinner for 2 seconds
        with st.spinner('Evaluating Model...'):
            time.sleep(1)
            st.write(eval_results)
            st.success('Congratulations! You have successfully trained a simple CNN model on the MNIST dataset using Tensorflow!')
            st.balloons()
    st.write('---')
    
    ##################################
    # Step-8: Download Trained Model #
    ##################################
    st.markdown('### 8. Download Model')
    st.code("""
        model.save('models/day11.h5')
    """, language='python')
    if st.download_button('Download Model', 'models/day11.h5'):
        with st.spinner('Downloading Model...'):
            st.success('Model Downloaded!')
    st.write('---')