
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ------------------------------------
# PAGE CONFIGURATION
# ------------------------------------

st.set_page_config(
    page_title="AI Image Classification",
    page_icon="🧠",
    layout="wide"
)

# ------------------------------------
# CUSTOM CSS
# ------------------------------------

st.markdown("""
<style>
.stApp {
    background-color: #f4f7fb;
}

.title {
    text-align: center;
    color: #173b70;
    font-size: 40px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #555;
    font-size: 18px;
}

.result-box {
    background-color: white;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #dce5f2;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------
# LOAD PRETRAINED MODEL
# ------------------------------------

@st.cache_resource
def load_model():
    model = tf.keras.applications.MobileNetV2(
        weights="imagenet",
        include_top=True
    )
    return model

# ------------------------------------
# IMAGE PREPROCESSING
# ------------------------------------

def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize((224, 224))

    image_array = np.array(image, dtype=np.float32)
    image_array = np.expand_dims(image_array, axis=0)

    image_array = tf.keras.applications.mobilenet_v2.preprocess_input(
        image_array
    )

    return image_array

# ------------------------------------
# PREDICTION
# ------------------------------------

def classify_image(model, image):
    processed_image = preprocess_image(image)

    predictions = model.predict(
        processed_image,
        verbose=0
    )

    decoded_predictions = (
        tf.keras.applications.mobilenet_v2.decode_predictions(
            predictions,
            top=3
        )[0]
    )

    return decoded_predictions

# ------------------------------------
# APPLICATION HEADER
# ------------------------------------

st.markdown(
    '<div class="title">🧠 AI Image Classification System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Upload an image and let Artificial Intelligence identify its contents.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ------------------------------------
# SIDEBAR
# ------------------------------------

st.sidebar.title("⚙️ About Project")

st.sidebar.info(
    """
    **Project:** Image Classification

    **Algorithm:** Convolutional Neural Network (CNN)

    **Model:** MobileNetV2

    **Framework:** TensorFlow

    **Interface:** Streamlit

    **Classes:** 1,000 ImageNet categories
    """
)

st.sidebar.markdown("---")
st.sidebar.write("Upload an image to begin.")

# ------------------------------------
# IMAGE UPLOAD
# ------------------------------------

uploaded_file = st.file_uploader(
    "📤 Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    try:
        image = Image.open(uploaded_file).convert("RGB")

        left, right = st.columns(2)

        with left:
            st.subheader("🖼️ Uploaded Image")
            st.image(
                image,
                caption="Your selected image",
                use_container_width=True
            )

        with right:
            st.subheader("🔍 Classification Results")

            with st.spinner(
                "Loading AI model and analyzing image..."
            ):
                model = load_model()
                results = classify_image(model, image)

            best_label = results[0][1].replace("_", " ").title()
            best_score = float(results[0][2]) * 100

            st.markdown(
                '<div class="result-box">',
                unsafe_allow_html=True
            )

            st.success("Image classified successfully!")

            st.markdown("### 🏆 Predicted Class")
            st.markdown(f"## {best_label}")

            st.metric(
                label="Prediction Score",
                value=f"{best_score:.2f}%"
            )

            st.progress(
                min(max(best_score / 100, 0.0), 1.0)
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

        # --------------------------------
        # TOP 3 PREDICTIONS
        # --------------------------------

        st.write("")
        st.markdown("---")
        st.subheader("📊 Top 3 Predictions")

        for rank, (_, label, score) in enumerate(results, start=1):

            readable_label = label.replace("_", " ").title()
            confidence = float(score) * 100

            st.write(
                f"**{rank}. {readable_label} — {confidence:.2f}%**"
            )

            st.progress(
                min(max(confidence / 100, 0.0), 1.0)
            )

        st.caption(
            "Prediction scores are model outputs, not guaranteed "
            "probabilities of correctness."
        )

    except Exception as error:
        st.error(
            "Unable to process the image. Please try another image."
        )
        st.exception(error)

else:
    st.info(
        "👆 Upload an image above to start classification."
    )

    st.markdown("### 🚀 How to Use")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 1️⃣ Upload")
        st.write("Choose an image from your computer.")

    with col2:
        st.markdown("#### 2️⃣ Analyze")
        st.write("The pretrained CNN model analyzes the image.")

    with col3:
        st.markdown("#### 3️⃣ Predict")
        st.write("View the predicted class and top 3 results.")

