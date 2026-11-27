# Loan Recommendation Project

A machine-learning-based web application that estimates whether a loan application is likely to be approved or rejected using applicant-provided information.

## Project Overview

This project combines a trained machine learning model with a Flask web application. Users enter applicant details, the application prepares the input features, and the model returns a predicted loan status.

## Features

- Web form for entering applicant information
- Machine-learning-based loan status prediction
- Flask application backend
- Pre-trained model loaded with Pickle
- Log transformation of selected income, loan amount and loan-term features
- Prediction result displayed in the web interface

## Technology Stack

- Python
- Flask
- NumPy
- Scikit-learn / serialized model
- Jupyter Notebook
- HTML and CSS

## Input Features

The model workflow uses applicant attributes such as:

- Gender, marital status and dependents
- Education and self-employment status
- Applicant and co-applicant income
- Loan amount and loan term
- Credit history
- Property area

## Repository Structure

```text
loan-recommendation-project/
├── app.py
├── loan prediction.ipynb
├── model.pkl
├── requirements.txt
├── README.md
└── templates/
    ├── index.html
    └── prediction.html
```

## Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/Shantanu5505/loan-recommendation-project.git
   cd loan-recommendation-project
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask application:

   ```bash
   python app.py
   ```

4. Open the local address printed by Flask (commonly `http://127.0.0.1:5000/`).

## Prediction Workflow

1. Enter applicant details in the form.
2. Submit the form to the Flask backend.
3. The application prepares and transforms the input features.
4. The trained model generates a prediction.
5. The result is displayed on the result page.

## Screenshots

The repository includes three interface screenshots: [1.PNG](1.PNG), [2.PNG](2.PNG) and [3.PNG](3.PNG).

## Future Improvements

- Add evaluation metrics such as precision, recall, F1-score and confusion matrix
- Add input validation and clearer error handling
- Document the training dataset, preprocessing and model selection
- Add explainability to communicate factors influencing a prediction
- Add automated tests and deployment instructions

## Responsible Use

This is an educational demonstration. A model prediction is not a credit decision and must not be used as the sole basis for real lending decisions. Real lending requires validated models, fairness testing, regulatory compliance and human oversight.

## Author

**Shantanu Dhatrak** · [GitHub](https://github.com/Shantanu5505)
