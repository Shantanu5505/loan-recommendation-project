from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":

        # ---------- Read form values ----------
        gender = request.form["gender"]
        married = request.form["married"]
        dependents = request.form["dependents"]
        education = request.form["education"]
        employed = request.form["employed"]
        credit = float(request.form["credit"])
        area = request.form["area"]

        ApplicantIncome = float(request.form["ApplicantIncome"])
        CoapplicantIncome = float(request.form["CoapplicantIncome"])
        LoanAmount = float(request.form["LoanAmount"])
        Loan_Amount_Term = float(request.form["Loan_Amount_Term"])

        # ---------- Encoding ----------

        # Gender
        male = 1 if gender == "Male" else 0

        # Married
        married_yes = 1 if married == "Yes" else 0

        # Dependents ✅ FIXED (NUMERIC, NOT ONE-HOT)
        if dependents == "3+":
            dependents = 3
        else:
            dependents = int(dependents)

        # Education
        not_graduate = 1 if education == "Not Graduate" else 0

        # Self Employed
        employed_yes = 1 if employed == "Yes" else 0

        # Property Area
        semiurban = 1 if area == "Semiurban" else 0
        urban = 1 if area == "Urban" else 0

        # ---------- Log Transform (SAFE) ----------
        ApplicantIncomelog = np.log(ApplicantIncome + 1)
        totalincomelog = np.log(ApplicantIncome + CoapplicantIncome + 1)
        LoanAmountlog = np.log(LoanAmount + 1)
        Loan_Amount_Termlog = np.log(Loan_Amount_Term + 1)

        # ---------- Prediction (12 FEATURES ONLY) ----------
        features = [[
            credit,
            ApplicantIncomelog,
            LoanAmountlog,
            Loan_Amount_Termlog,
            totalincomelog,
            male,
            married_yes,
            dependents,
            not_graduate,
            employed_yes,
            semiurban,
            urban
        ]]

        prediction = model.predict(features)[0]

        # ---------- Output ----------
        result = "Approved ✅" if prediction == "Y" else "Rejected ❌"

        return render_template(
            "prediction.html",
            prediction_text=f"Loan Status: {result}"
        )

    return render_template("prediction.html")


if __name__ == "__main__":
    app.run(debug=True)
