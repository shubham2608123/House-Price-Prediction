# 🏠 Bangalore House Price Prediction

## 📌 Project Overview

The Bangalore House Price Prediction System is a Machine Learning web application that predicts house prices based on property features such as location, total square feet area, number of bedrooms (BHK), bathrooms, and balconies.

The project uses historical Bengaluru housing data and applies data preprocessing, feature engineering, and machine learning techniques to estimate property prices accurately. The application provides an interactive interface where users can enter property details and receive an instant price prediction.

---

## 🚀 Features

- Predict house prices in Bangalore
- Location-based price estimation
- User-friendly web interface
- Real-time predictions
- Data cleaning and preprocessing
- Feature engineering
- One-Hot Encoding for categorical features
- Outlier detection and removal
- Machine Learning model training and evaluation
- Model deployment using Streamlit

---

## 📊 Dataset

Dataset: Bengaluru House Price Dataset

Features Used:

- Location
- Total Square Feet
- Number of Bathrooms
- Number of Balconies
- Number of Bedrooms (BHK)

Target Variable:

- Price (in Lakhs)

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib
- Seaborn

### Machine Learning
- Linear Regression
- Random Forest Regressor

### Deployment
- Streamlit

### Development Environment
- Jupyter Notebook
- VS Code

---

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── data/
│   └── Bengaluru_House_Data.csv
│
├── notebooks/
│   └── House_Price_Prediction.ipynb
│
├── model/
│   ├── house_price_model.pkl
│   └── columns.pkl
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Machine Learning Workflow

### 1. Data Collection
- Load Bengaluru House Price Dataset

### 2. Data Cleaning
- Handle missing values
- Remove irrelevant columns
- Convert data types

### 3. Feature Engineering
- Extract BHK feature
- Create meaningful numerical features

### 4. Outlier Removal
- Remove unrealistic property records
- Remove abnormal price variations

### 5. Encoding
- One-Hot Encoding for Location feature

### 6. Train-Test Split
- Split dataset into training and testing sets

### 7. Model Training
- Linear Regression
- Random Forest Regressor

### 8. Model Evaluation
- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

### 9. Model Saving
- Save trained model using Joblib

### 10. Deployment
- Build Streamlit interface
- Predict house prices in real time

---

## 📈 Model Performance

Evaluation Metrics Used:

- R² Score
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)

The model was trained on cleaned and preprocessed housing data to generate accurate property price predictions.

---

## 🖥️ Running the Project

### Clone Repository

```bash
git clone https://github.com/yourusername/house-price-prediction.git
```

### Navigate to Project

```bash
cd house-price-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## 📋 Sample Input

| Feature | Value |
|----------|--------|
| Location | Indira Nagar |
| BHK | 2 |
| Bathrooms | 2 |
| Balconies | 1 |
| Total Sqft | 1200 |

---

## 🎯 Sample Output

```text
Estimated House Price: ₹ 85.50 Lakhs
```

*(Prediction may vary depending on trained model and dataset.)*

---

## 🔮 Future Enhancements

- Use latest real-estate datasets
- Add property age feature
- Add parking information
- Add nearby metro/school information
- Integrate maps and geolocation
- Deploy on cloud platforms
- Build REST API using FastAPI
- Improve accuracy using XGBoost

---

## 👨‍💻 Author

Shubham Dalvi

Machine Learning & Data Science Enthusiast

---

## 📜 License

This project is developed for educational and learning purposes.
