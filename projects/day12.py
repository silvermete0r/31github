import streamlit as st
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, Input
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
X = iris.data
y = iris.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = Sequential([
    Input(shape=X_train.shape[1:]),
    Dense(1024, activation='relu'),
    Dense(512, activation='relu'),
    Dense(256, activation='relu'),
    Dropout(0.2),
    Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

def train_model(X_train, y_train, epochs=30):
    return model.fit(X_train, y_train, epochs=epochs, verbose=1)

def evaluate_model(X_test, y_test):
    loss, accuracy = model.evaluate(X_test, y_test, verbose=1)
    return loss, accuracy

def draw_performance_chart(history):
    history_df = pd.DataFrame(history.history)
    st.line_chart(history_df[['loss', 'accuracy']])

def app():
    st.title('Day #12')
    st.subheader('Tensorflow Simple Iris Classification App')
    st.markdown("""
        This app demonstrates a simple TensorFlow Iris classification model using the Sklearn Iris dataset.
        
        * **Python libraries used:** `streamlit`, `tensorflow`, `sklearn`
        
        * **Dataset used:** [Iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)
        
        * **References:** [TensorFlow Guide](https://www.tensorflow.org/guide)
    """)
    st.write('---')

    st.markdown('### Iris Dataset')
    st.markdown('The Iris dataset contains 3 classes of 50 instances each, where each class refers to a type of iris plant.')
    st.image('media/iris-classes-img.png', width=500)
    st.write('Class labels:')
    st.json({
        '0': iris.target_names[0],
        '1': iris.target_names[1],
        '2': iris.target_names[2]
    })
    
    with st.expander('Show Tensorflow Model Architecture'):
        st.markdown('''
            ### Tensorflow Code
            **Model architecture:** 
            * Input layer (4 neurons)
            * Hidden layer 1 (1024 neurons) using ReLU activation function
            * Hidden layer 2 (512 neurons) using ReLU activation function
            * Hidden layer 3 (256 neurons) using ReLU activation function
            * Dropout layer (20%)
            * Output layer (3 neurons) using Softmax activation function
                    
            ---
        ''')
        st.code("""
            # Load Iris dataset
            iris = load_iris()
            X = iris.data
            y = iris.target

            # Standardize the feature data
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)

            # Split the dataset into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

            # Build a simple neural network model
            model = Sequential([
                Input(shape=X_train.shape[1:]),
                Dense(1024, activation='relu'),
                Dense(512, activation='relu'),
                Dense(256, activation='relu'),
                Dropout(0.2),
                Dense(3, activation='softmax')
            ])

            model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        """, language='python')

    if st.button('Train Model'):
        st.markdown('### Model Training')
        st.code("""
            # Train the model
            model.fit(X_train, y_train, epochs=10, verbose=0)
        """, language='python')
        with st.spinner('Training in progress...'):
            history = train_model(X_train, y_train)
            st.success('Model trained!')

        st.markdown('### Model Performance')
        st.code("""
            # Evaluate the model
            loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
        """, language='python')
        with st.spinner('Evaluating model...'):
            loss, accuracy = evaluate_model(X_test, y_test)
            st.json({
                'loss': loss,
                'accuracy': accuracy
            })
        with st.spinner('Drawing performance chart...'):
            draw_performance_chart(history)
            st.success('Work completed!')