import streamlit as st
import numpy as np
import cv2

def app():
    st.title('Day #7')
    st.subheader('Image Quality Enhancement Web App')
    st.markdown("""
        This app enhances the quality of an image using various techniques. The techniques are listed below:
        - Sharpening
        - Noise Removal
        - Brightness & Contrast Adjustment
        - Blur
        - Gamma Correction

        **Libraries:** `Streamlit`, `Numpy`, `OpenCV`        
    """)
    st.write('---')

    techniques = ["Sharpening", "Noise Removal", "Brightness & Contrast Adjustment", "Blur", "Gamma Correction"]

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=("jpg", "png", "jpeg", "jfif"))
    
    # Main logic
    if uploaded_file is not None:
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
        st.image(image, caption="Original Image")
        selected_technique = st.selectbox("Choose Enhancement Technique", techniques, index=0)

        enhanced_image = None
        if selected_technique == "Sharpening":
            st.markdown("""
                **Note:** Sharpness, which is also known as acutance, refers to how crisp an image appears.
            """)
            val = st.slider("Sharpening", 1, 10, 1)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (val, val))
            enhanced_image = cv2.filter2D(image, -1, kernel)
        elif selected_technique == "Noise Removal":
            st.markdown("""
                **Note:** Image noise is random variation of brightness or color information in images, and is usually an aspect of electronic noise.
            """)
            val = st.slider("Noise Removal", 1, 15, 3, 2)
            enhanced_image = cv2.medianBlur(image, val)
        elif selected_technique == "Brightness & Contrast Adjustment":
            st.markdown("""
                **Note:** Brightness refers to the overall lightness or darkness of the image. Contrast is the difference in brightness between objects or regions.
            """)
            alpha = st.slider("Brightness", 0.0, 10.0, 1.0)
            beta = st.slider("Contrast", 0.0, 10.0, 1.0)
            enhanced_image = cv2.addWeighted(image, alpha, image, 1.0, beta)
        elif selected_technique == "Blur":
            st.markdown("""
                **Note:** Blurring is a technique for modifying the sharpness of an image. It is used to reduce the image noise and reduce the details of an image.
            """)
            val = st.slider("Blur", 1, 15, 3, 1)
            enhanced_image = cv2.blur(image, (val, val))
        elif selected_technique == "Gamma Correction":
            st.markdown("""
                **Note:** Gamma correction, or often simply gamma, is a nonlinear operation used to encode and decode luminance or tristimulus values in video or still image systems.
            """)
            gamma = st.slider("Gamma Correction", 0.0, 10.0, 1.0)
            invGamma = 1.0 / gamma
            table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
            enhanced_image = cv2.LUT(image, table)

        if enhanced_image is not None:
            st.image(enhanced_image, caption="Enhanced Image", use_column_width=True)
            download_img = cv2.imencode('.jpg', enhanced_image)[1].tobytes()
            st.download_button(label="Download Image", data=download_img, file_name="enhanced_image.jpg", mime="image/jpg")
            
    else:
        st.info("Please upload an image to enhance.")