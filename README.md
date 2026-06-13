# Diabetes Prediction Using Machine Learning

A Machine Learning application that predicts the likelihood of diabetes based on patient medical attributes. The project leverages a Support Vector Machine (SVM) classifier trained on the PIMA Indians Diabetes Dataset and is deployed through an interactive Streamlit web interface.

## Project Overview

Early detection of diabetes can significantly improve patient outcomes. This project demonstrates the complete machine learning workflow, from data preprocessing and model training to deployment as a web application.

Users can enter medical parameters and receive an instant prediction indicating whether the patient is likely to be diabetic or non-diabetic.

## Key Features

- End-to-end Machine Learning pipeline
- Data preprocessing and feature standardization
- Support Vector Machine (SVM) classification model
- Model evaluation using train and test datasets
- Real-time diabetes prediction
- Interactive Streamlit-based user interface
- Deployed web application

## Live Application

🔗 **Streamlit Deployment**

https://diabetes-prediction-project-34.streamlit.app

## Dataset

**PIMA Indians Diabetes Dataset**

The dataset contains diagnostic measurements collected from female patients of Pima Indian heritage and is widely used for diabetes prediction research.

## Technology Stack

| Category | Technologies |
|-----------|-------------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Model | Support Vector Machine (SVM) |
| Deployment | Streamlit |
| Development Environment | Google Colab |

## Machine Learning Workflow

```text
Data Collection
       ↓
Data Preprocessing
       ↓
Feature Standardization
       ↓
Train-Test Split
       ↓
SVM Model Training
       ↓
Model Evaluation
       ↓
Prediction System
       ↓
Streamlit Deployment
```

## Model Performance

| Metric | Score |
|----------|----------|
| Training Accuracy | ~78% |
| Testing Accuracy | ~77% |

The model demonstrates consistent performance on both training and testing datasets, indicating reasonable generalization capability.

## Repository Structure

```text
Diabetes-Prediction-Project/
│
├── screenshot/
├── app.py
├── Diabetes_Prediction.ipynb
├── predictive system.py
├── trained_model.sav
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/raghuvendra34/Diabetes-Prediction-Project.git
cd Diabetes-Prediction-Project
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Future Enhancements

- Hyperparameter optimization
- Comparative analysis with additional ML algorithms
- Advanced data visualization dashboard
- Improved model performance through feature engineering
- Cloud-native deployment architecture

## Author

**Raghuvendra Kumar**

GitHub: https://github.com/raghuvendra34