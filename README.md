# Loan Recommendation Project

A machine learning-based web application that predicts whether a loan application is likely to be **Approved** or **Rejected** using applicant details.

## Project Overview

This project combines a trained machine learning model with a Flask web application. Users enter applicant information such as income, loan amount, credit history, education, employment status, and property area. The application processes the input and displays the predicted loan status.

## Features

- Simple web interface for entering loan applicant details
- Machine learning-based loan approval prediction
- Flask backend for handling requests
- Pre-trained model loaded using Pickle
- Log transformation of income, loan amount, and loan term features
- Prediction result displayed as Approved or Rejected

## Technologies Used

- Python
- Flask
- NumPy
- Pickle
- Jupyter Notebook
- HTML and CSS
- Machine Learning

## Project Structure

```text
loan-recommendation-project/
│
├── app.py
├── loan prediction.ipynb
├── model.pkl
├── requirements.txt
├── README.md
│
└── templates/
    ├── index.html
    └── prediction.html
```

## Input Features

The application uses the following applicant details:

- Gender
- Marital status
- Number of dependents
- Education
- Self-employment status
- Applicant income
- Co-applicant income
- Loan amount
- Loan amount term
- Credit history
- Property area

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Shantanu5505/loan-recommendation-project.git
cd loan-recommendation-project
```

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask application

```bash
python app.py
```

### 4. Open the application

Open the local URL shown in the terminal, usually:

```text
http://127.0.0.1:5000/
```

## Prediction Workflow

1. Enter the applicant details.
2. Submit the loan application form.
3. The Flask application encodes the input values.
4. Numerical features are transformed and passed to the trained model.
5. The model predicts the loan status.
6. The result is displayed as Approved or Rejected.

## Future Improvements

- Add model performance metrics such as accuracy, precision, recall, and F1-score
- Add data validation and error handling
- Improve the user interface and responsiveness
- Deploy the application online
- Add explainable AI to show the factors influencing the prediction

## Disclaimer

This project is developed for educational and demonstration purposes. Its predictions should not be used as the sole basis for real financial decisions.

## Author

**Shantanu Dhatrak**

GitHub: [Shantanu5505](https://github.com/Shantanu5505)
