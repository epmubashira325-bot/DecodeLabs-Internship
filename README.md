# Iris Flower Classification using Machine Learning

## Overview

This project uses the famous Iris dataset to classify iris flowers into three species:

* Setosa
* Versicolor
* Virginica

Multiple machine learning algorithms are trained and evaluated, including K-Nearest Neighbors (KNN), Random Forest, and Support Vector Machine (SVM).

## Features

* Data loading and preprocessing
* Exploratory Data Analysis (EDA)
* Data visualization using Matplotlib and Seaborn
* Feature scaling using StandardScaler
* KNN Classification
* Random Forest Classification
* SVM Classification
* Model evaluation using Confusion Matrix, Classification Report, and F1 Score
* K-value optimization for KNN
* Prediction on new flower samples

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

## Dataset

The project uses the built-in Iris dataset available in Scikit-learn.

Features:

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

Target Classes:

* Setosa
* Versicolor
* Virginica

## Project Structure

iris-classification/

│

├── app.py

├── README.md

## Installation

Install required packages:

pip install numpy pandas matplotlib seaborn scikit-learn

## How to Run

Execute the Python file:

python app.py

## Workflow

### 1. Load Dataset

* Load Iris dataset from Scikit-learn.
* Convert dataset into a Pandas DataFrame.

### 2. Exploratory Data Analysis

* Display dataset information.
* View statistical summaries.
* Analyze class distribution.

### 3. Data Preprocessing

* Split dataset into training and testing sets.
* Apply feature scaling using StandardScaler.

### 4. Data Visualization

* Generate pair plots to visualize relationships between features.

### 5. Model Training

Train the following models:

* K-Nearest Neighbors (KNN)
* Random Forest
* Support Vector Machine (SVM)

### 6. Model Evaluation

Evaluate models using:

* Confusion Matrix
* Classification Report
* F1 Score

### 7. Prediction

Predict flower species for new user-provided samples.

## Sample Output

Predicted species name: setosa

Weighted F1 Score: 1.0000

Best K value: 5

## Results

The models achieve high classification accuracy on the Iris dataset due to its well-separated classes.

Performance Metrics:

* Accuracy
* Precision
* Recall
* F1 Score

## Learning Outcomes

* Data preprocessing techniques
* Feature scaling
* Classification algorithms
* Model evaluation
* Hyperparameter tuning
* Data visualization

## Future Enhancements

* Deploy using Streamlit
* Accept user inputs through a web interface
* Compare additional machine learning models
* Use cross-validation for better evaluation

## Author

Mubashira EP

B.Tech in Artificial Intelligence and Data Science
