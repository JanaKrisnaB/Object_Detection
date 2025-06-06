# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17bENUy8rdBa9QT6UmTdd81GkWLzqHwF8
"""

!pip install streamlit

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import gdown
import os

st.title("🚀 CIFAR-10 Image Classifier using ResNet50")

@st.cache_resource
def load_model():
    model_path = "resnet50_cifar10_model.h5"
    if not os.path.exists(model_path):
        url = "https://drive.google.com/uc?id=13KgM2DddlsscFQx4uoYK0lesSE6-DAo3"
        gdown.download(url, model_path, quiet=False)
    model = tf.keras.models.load_model(model_path)
    return model

model = load_model()

class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer',
               'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img = image.resize((32, 32))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    if st.button("Predict"):
        with st.spinner("Predicting..."):
            prediction = model.predict(img_array)
            predicted_label = class_names[np.argmax(prediction)]
            confidence = np.max(prediction) * 100
            st.success(f"🧠 Prediction: **{predicted_label}** ({confidence:.2f}%)")

