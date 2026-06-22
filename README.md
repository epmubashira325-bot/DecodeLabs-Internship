#Project 1

# LLM Text Generator using Ollama

## Overview

This project is a Streamlit-based application that interacts with a Large Language Model (LLM) using Ollama. Users can enter prompts and receive AI-generated responses.

## Features

* Interactive web interface
* AI-powered text generation
* Integration with Ollama
* Supports local LLM models

## Technologies Used

* Python
* Streamlit
* Ollama

## Project Structure

llm-text-generator/
│
├── app.py
├── README.md

## Prerequisites

Install Ollama:

https://ollama.com

Install dependencies:

pip install streamlit ollama

Pull the model:

ollama pull llama3.2

## How to Run

Start Ollama:

ollama serve

Run Streamlit:

streamlit run app.py

Open the browser URL displayed in the terminal.

## Usage

1. Enter a prompt.
2. Click Generate Response.
3. View the AI-generated output.

## Example Prompt

Explain Machine Learning in simple terms.

## Learning Outcomes

* Working with Large Language Models
* Streamlit application development
* Prompt engineering basics
* Ollama integration

## Future Enhancements

* Chat history support
* Multiple model selection
* File upload support
* Conversation memory

  
#Project 2

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

#Project 3

# AI Recommendation System

## Overview

This project is a simple recommendation system built using Python. It recommends movies based on user preferences by matching genres and calculating a similarity score.

## Features

* Takes user preferences as input
* Matches user interests with movie genres
* Calculates match scores
* Displays recommended movies in descending order of relevance

## Technologies Used

* Python
* Lists
* Dictionaries
* Loops
* Conditional Statements

## Project Structure

recommendation-system/
│
├── app.py
├── README.md

## How to Run

1. Install Python.
2. Open terminal in the project folder.
3. Run:

python app.py

4. Enter genres when prompted.

Example:

Enter your favorite genres (comma separated): Action,Sci-Fi

## Sample Output

Recommended Movies:
Avengers - Match Score: 2
Avatar - Match Score: 2
Interstellar - Match Score: 1
John Wick - Match Score: 1

## Learning Outcomes

* Recommendation system basics
* Pattern matching
* User input handling
* Similarity scoring logic

## Future Enhancements

* Add more movies
* Use a database
* Implement content-based filtering
* Build a web interface using Streamlit

