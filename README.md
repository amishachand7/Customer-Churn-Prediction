# Customer-Churn-Prediction
# 📊 Customer Churn Prediction

![Flask App](https://img.shields.io/badge/Flask-Application-blue.svg) ![ML Model](https://img.shields.io/badge/Machine%20Learning-Churn%20Prediction-green.svg)

### 🚀 Predict whether a customer will churn based on their details.

This project is a **Flask-based web application** that allows users to input customer details and get a **churn prediction** using a **pre-trained machine learning model**.

---

## 📌 Features
✅ User-friendly web interface  
✅ Takes **customer details** as input  
✅ Uses a **pre-trained ML model** for predictions  
✅ Provides **real-time churn predictions**  
✅ Built with **Flask** and **Python**  

---

## 📂 Project Structure
Customer-Churn-Prediction/ 
  │-- static/ 
    ├── styles.css # Styling for the web app
  │-- templates/  
    ├── index.html # Main UI for user input 
  │-- Customer_Churn.ipynb # Jupyter Notebook for model training 
  │-- Customer_Churn_Prediction.pkl # Trained ML model 
  │-- app.py # Flask backend for serving predictions 
  │-- README.md # Project documentation 
  
---

## ⚙️ Installation
1️⃣ **Clone the repository**  
```bash
git clone https://github.com/amishachand7/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
2️⃣ **Create a virtual environment**
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
3️⃣ **Install dependencies**

🚀 Running the App
Start the Flask app using:
python app.py
Then, open http://127.0.0.1:5000/ in your browser.

📊 Model Details
Model: Machine Learning Classifier
Features used:
Credit Score
Age
Tenure
Balance
Number of Products
Credit Card Ownership
Active Membership
Estimated Salary
Geography (France, Germany, Spain)
Gender (Male, Female)
Output: Churn (Yes/No)

📸 Screenshots
Home Page
![image](https://github.com/user-attachments/assets/e41bb40e-debb-41fb-8206-b02ec2475c81)
Prediction
![image](https://github.com/user-attachments/assets/b7f5527e-f4ff-459d-ba47-316821fc8123)

🤝 Contributing
Feel free to fork this repo, make improvements, and submit a pull request! 🚀

📜 License
This project is licensed under the MIT License.
