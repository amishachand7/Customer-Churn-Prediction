from flask import Flask, render_template, request
import pickle
import numpy as np
import os

# Check if the model file exists
model_filename = "Customer_Churn_Prediction.pkl"
if not os.path.exists(model_filename):
    raise FileNotFoundError(f"Model file '{model_filename}' not found!")

# Load the trained model
try:
    model = pickle.load(open(model_filename, "rb"))
except Exception as e:
    raise RuntimeError(f"Error loading model: {str(e)}")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract numerical inputs
        features = [
            float(request.form["CreditScore"]),
            float(request.form["Age"]),
            float(request.form["Tenure"]),
            float(request.form["Balance"]),
            float(request.form["NumOfProducts"]),
            float(request.form["HasCrCard"]),
            float(request.form["IsActiveMember"]),
            float(request.form["EstimatedSalary"]),
        ]

        # Process categorical inputs (Geography and Gender)
        geography = request.form["Geography"]
        features.append(1 if geography == "Germany" else 0)  # Geography_Germany
        features.append(1 if geography == "Spain" else 0)  # Geography_Spain

        gender = request.form["Gender"]
        features.append(1 if gender == "Male" else 0)  # Gender_Male

        # Convert to numpy array and reshape
        input_data = np.array(features).reshape(1, -1)

        # Print input for debugging (Optional)
        print("Input Data for Prediction:", input_data)

        # Make prediction
        prediction = model.predict(input_data)[0]
        result = "Churn" if prediction == 1 else "No Churn"

        return render_template("index.html", prediction_text=f"Customer is likely to: {result}")

    except KeyError as e:
        return render_template("index.html", prediction_text=f"Error: Missing input for '{str(e)}'")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Prediction Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
