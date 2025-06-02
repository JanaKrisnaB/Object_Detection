# 🧠 Object Detection using ResNet50 on CIFAR-10

This project demonstrates the process of building a high-accuracy image classification model using **ResNet50** on the **CIFAR-10** dataset.

## 📌 Overview

- **Dataset**: CIFAR-10 (50,000 training images, 10,000 test images across 10 categories)
- **Architecture**: ResNet50 (pretrained or custom from scratch)
- **Libraries Used**: TensorFlow, Keras, NumPy, Pandas, OpenCV, Matplotlib
- **Accuracy Achieved**: ✅ 96%

## 🚀 Features

- Automated dataset download via Kaggle API
- Extraction of `.zip` and `.7z` files using `zipfile` and `py7zr`
- Data preprocessing and normalization
- Conversion of images to NumPy arrays and label encoding
- Train/test split using `sklearn.model_selection.train_test_split`
- Model training using a deep neural network (ResNet50)
- Evaluation of model performance
