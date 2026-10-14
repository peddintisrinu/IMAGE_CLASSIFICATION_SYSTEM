# 🧠 AI Image Classification System

An AI-powered Image Classification System built using Python, TensorFlow, MobileNetV2, and Streamlit. The application allows users to upload images and automatically identify objects using a pretrained Convolutional Neural Network (CNN).

## 🚀 Project Overview

Image classification is a computer vision task that enables computers to recognize and categorize objects in images.

This project uses the **MobileNetV2 deep learning model**, pretrained on the ImageNet dataset, to classify uploaded images into recognizable categories. It displays the predicted class, prediction score, and top three predictions through an interactive web interface.

## ✨ Features

* 🖼️ **Image Upload:** Upload images in JPG, JPEG, and PNG formats.
* 🤖 **AI-Powered Classification:** Identify objects using a pretrained deep learning model.
* 📊 **Prediction Confidence:** View the model's score for the predicted class.
* 🏆 **Top 3 Predictions:** Display the three highest-scoring categories.
* 🎨 **Interactive Interface:** Simple and user-friendly web application.
* ⚡ **Pretrained Model:** Use MobileNetV2 without training a model from scratch.
* ☁️ **Cloud Deployment:** Deploy the application using Streamlit Community Cloud.

## 🛠️ Technologies Used

| Technology     | Purpose                                 |
| -------------- | --------------------------------------- |
| Python         | Main programming language               |
| TensorFlow     | Deep learning framework                 |
| MobileNetV2    | Pretrained image classification model   |
| NumPy          | Numerical computations and image arrays |
| Pillow (PIL)   | Image processing                        |
| Streamlit      | Interactive web application             |
| ImageNet       | Dataset used to pretrain the model      |
| Git and GitHub | Version control and source code hosting |

## 📂 Project Structure

```text
image-classification-model/
│
├── App.py
├── requirements.txt
└── README.md
```

### File Description

* **App.py:** Contains the image upload interface, preprocessing, model loading, and prediction logic.
* **requirements.txt:** Lists the Python dependencies required to run the application.
* **README.md:** Provides project documentation and setup instructions.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/image-classification-model.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the Project Folder

```bash
cd image-classification-model
```

### 3. Install the Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run App.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

**Note:** Use a Python version supported by your chosen TensorFlow release. An internet connection is generally required the first time the pretrained model weights are downloaded.

## 📋 Requirements

Create a `requirements.txt` file containing:

```text
streamlit
tensorflow
numpy
pillow
```

## 🔍 How It Works

The image classification system follows these steps:

1. **Image Upload:** The user uploads an image through the Streamlit interface.
2. **Image Preprocessing:** The image is converted to RGB format and resized to 224 × 224 pixels.
3. **Input Preparation:** The image is converted into a NumPy array and normalized using MobileNetV2's preprocessing function.
4. **Feature Extraction:** The pretrained CNN processes the image and extracts useful visual features.
5. **Image Classification:** MobileNetV2 generates scores for its ImageNet categories.
6. **Prediction Display:** The application displays the top predicted category, its score, and the top three predictions.

## 🧠 Deep Learning Model

**MobileNetV2** is a lightweight convolutional neural network designed for efficient image recognition.

In this project, the model uses pretrained ImageNet weights and can classify images into 1,000 ImageNet categories.

### Why MobileNetV2?

* Efficient architecture for image classification.
* Pretrained weights reduce the need for model training.
* Supports recognition of many everyday objects and animals.
* Integrates with TensorFlow and Keras.
* Suitable for demonstrating transfer learning concepts.

## 📊 Expected Output

After uploading an image, the application displays:

* The uploaded image.
* The predicted object category.
* The prediction score.
* The top three predicted categories with their scores.

For example, an uploaded dog image might produce a prediction such as *Golden Retriever*.

Actual predictions and scores depend on the image and model output.

## 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud**.

### Deployment Steps

1. Upload the project files to GitHub.
2. Ensure `App.py` and `requirements.txt` are in the repository's root directory.
3. Sign in to Streamlit Community Cloud using GitHub.
4. Create a new application.
5. Select the repository and branch.
6. Set `App.py` as the main application file.
7. Deploy the application.

Streamlit Cloud installs the dependencies specified in `requirements.txt` during deployment.

## 🎯 Applications of Image Classification

Image classification is used in many real-world applications, including:

* Animal and plant recognition.
* Product categorization.
* Medical image research.
* Agricultural image analysis.
* Wildlife monitoring.
* Smart image organization.
* Automated visual inspection.

**Note:** This demonstration is not designed or validated for medical diagnosis or other safety-critical decisions.

## ⚠️ Limitations

* Classification is limited to the categories supported by the pretrained ImageNet model.
* The model may misclassify unfamiliar images or objects.
* Prediction scores do not guarantee that a prediction is correct.
* Custom categories require a suitable dataset and additional training or fine-tuning.
* Classification quality depends on image quality and the model's learned features.

## 🔮 Future Enhancements

Potential improvements include:

* Train a custom CNN using a dedicated dataset.
* Add a prediction history feature.
* Support batch image classification.
* Display charts comparing prediction scores.
* Add downloadable classification reports.
* Develop a custom animal or plant classification model.
* Improve the interface for mobile devices.
* Explore deployment optimizations for faster inference.

## 👨‍💻 Author

**Peddinti Srinu**

Computer Science and Engineering Student

Interests: Machine Learning, Deep Learning, Artificial Intelligence, and Web Development.

## 📄 License

This project is intended for educational and demonstration purposes. If you distribute it, specify an appropriate license and review the licensing terms of the libraries and pretrained model you use.

---

⭐ If you find this project useful, consider giving the repository a star on GitHub.
