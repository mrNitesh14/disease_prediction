# Disease Prediction App

This is a disease prediction web application built using [Streamlit](https://streamlit.io/), which predicts potential diseases based on the symptoms selected by the user. The prediction is made using a trained machine learning model.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Contributing](#contributing)
- [License](#license)

## Overview
The Disease Prediction App takes a set of symptoms as input from the user and predicts the disease. The app allows the user to choose symptoms from a list of 40 common symptoms, divided into 4 groups with 10 symptoms each.

## Features
- User-friendly interface built with Streamlit.
- Users can select symptoms using drop-downs.
- Machine learning model predicts the disease based on the selected symptoms.
- Prediction is displayed instantly upon clicking the "Predict" button.

## Requirements
The following packages and libraries are required to run the app:
- Python 3.7+
- Streamlit
- scikit-learn
- joblib
- numpy

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/mrNitesh14/disease_prediction.git
    cd disease-prediction-app
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Place the trained model:**
   - Download or place your `disease_prediction_model.pkl` file in the root of your project directory.

## Usage

1. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

2. **Interact with the app:**
   - Open your browser and go to `http://localhost:8501/`.
   - Select symptoms from the provided drop-downs.
   - Click the "Predict" button to see the disease prediction.

## Model
The machine learning model used for prediction was trained on a dataset of symptoms and diseases. Ensure the correct model is saved as `disease_prediction_model.pkl`. 

### Training the Model
If you need to retrain the model, follow these steps:
1. Preprocess your dataset.
2. Train a model using scikit-learn.
3. Save the trained model using `joblib`:
    ```python
    import joblib
    joblib.dump(trained_model, 'disease_prediction_model.pkl')
    ```
