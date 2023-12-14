import streamlit as st
import tensorflow as tf
from keras.datasets import boston_housing
from sklearn.preprocessing import StandardScaler

# Load Data
(X_train, y_train), (X_test, y_test) = boston_housing.load_data()

# Data preprocessing: Scale Data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build the Regression Model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile the Model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train the Model
def train_model():
    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=0)

def app():
    st.title('Day #13')
    st.subheader('Tensorflow Regression Model Training Based on Boston Housing Dataset')
    st.markdown('''
        This app demonstrates a simple Tensorflow regression model using the Boston Housing dataset.
        
        * **Python libraries used:** `streamlit`, `tensorflow`, `sklearn` 
        
        * **Dataset used:** [Boston Housing](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/boston_housing)
                
        * **References:** [TensorFlow Guide](https://www.tensorflow.org/guide)
    ''')
    st.write('---')

    st.markdown('### Boston Housing Dataset')
    st.markdown('The Boston Housing dataset contains information collected by the U.S Census Service concerning housing in the area of Boston Mass.')
    st.info(f'Number of Rows: {X_train.shape[0]} | Number of Columns: {X_train.shape[1]}')
    st.dataframe(X_train)
    st.image('media/boston-housing.jpg', width=500, caption='Boston Housing')
    st.write('Features Description:')
    st.json({
            "0. CRIM": "per capita crime rate by town",
            "1. ZN": "proportion of residential land zoned for lots over 25,000 sq.ft.",
            "2. INDUS": "proportion of non-retail business acres per town",
            "3. CHAS": "Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)",
            "4. NOX": "nitric oxides concentration (parts per 10 million)",
            "5. RM": "average number of rooms per dwelling",
            "6. AGE": "proportion of owner-occupied units built prior to 1940",
            "7. DIS": "weighted distances to five Boston employment centres",
            "8. RAD": "index of accessibility to radial highways",
            "9. TAX": "full-value property-tax rate per $10,000",
            "10. PTRATIO": "pupil-teacher ratio by town",
            "11. B": "This is calculated as (1000(Bk - 0.63)^2), where Bk is the proportion of people of African American descent by town",
            "12. LSTAT": "percentage lower status of the population",
            "Target - MEDV": "Median value of owner-occupied homes in $1000's"
    })

    with st.expander('Show Tensorflow Model Architecture'):
        st.markdown('''
            ### Tensorflow Code
            **Model architecture:** 
            * Input layer (13 neurons)
            * Hidden layer (128 neurons)
            * Hidden layer (64 neurons)
            * Output layer (1 neuron)
                    
            ---
        ''')
        st.code('''
            # Load Data
            (X_train, y_train), (X_test, y_test) = boston_housing.load_data()

            # Data preprocessing: Scale Data
            scaler = StandardScaler()
            X_train = scaler.fit_transform(X_train)
            X_test = scaler.transform(X_test)

            # Build the Regression Model
            model = tf.keras.models.Sequential([
                tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
                tf.keras.layers.Dense(64, activation='relu'),
                tf.keras.layers.Dense(1)
            ])

            # Compile the Model
            model.compile(optimizer='adam', loss='mse', metrics=['mae'])
        ''', language='python')

    if st.button('Train Model'):
        st.markdown('### Model Training')
        st.code("""
            # Train the model
            model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=0)
        """, language='python')
        with st.spinner('Training in progress...'):
            train_model()
            st.success('Model trained!')

        st.markdown('### Model Performance')
        st.code("""
            # Evaluate the model
            loss = model.evaluate(X_test, y_test, verbose=0)
        """, language='python')
        with st.spinner('Evaluating in progress...'):
            loss = model.evaluate(X_test, y_test, verbose=0)
            st.json({
                'loss': loss[0],
                'mae': loss[1]
            })
        with st.spinner('Drawing performance chart...'):
            st.line_chart(loss)
            st.success('Work completed!')