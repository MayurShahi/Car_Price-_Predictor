# Car_Price-_Predictor
# 🚗 Car Price Prediction using XGBoost

## 📌 Project Overview

This project predicts the selling price of used cars using machine learning techniques. The goal is to build an accurate regression model that helps estimate car prices based on various features such as year, fuel type, transmission, and mileage.

---

## 📊 Dataset

The dataset contains information about used cars, including:

            brand=car.brand,
            model=car.model,
            model_year=car.model_year,
            milage=car.milage,
            fuel_type=car.fuel_type,
            transmission=car.transmission,
            ext_col=car.ext_col,
            int_col=car.int_col,
            clean_title=car.clean_title,
            accident_occurred=car.Accident_occured,
            engine_capacity=car.Engine_capacity,
            horse_power=car.Horse_Power,

---

## ⚙️ Technologies Used

* Python
* Pandas & NumPy
* Matplotlib & Seaborn (for visualization)
* Scikit-learn (for preprocessing & evaluation)
* XGBoost (for model training)

---

## 🤖 Model Used

This project uses **XGBoost Regressor**, a powerful gradient boosting algorithm known for:

* High performance on structured/tabular data
* Regularization to prevent overfitting
* Handling of missing values
* Fast and efficient computation

---

## 📈 Model Performance

* Model: XGBoost Regressor
* Evaluation Metrics:

  * R² Score
  * Mean Absolute Error (MAE)
  * Mean Squared Error (MSE)

The model achieved strong predictive performance on test data, making it suitable for real-world price estimation.

---

## 🔍 Workflow

1. Data Cleaning & Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Model Training using XGBoost
5. Model Evaluation
6. Prediction

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/MayurShahi/Car_Price-_Predictor.git
cd Car_Price-_Predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the notebook or script

```bash
jupyter notebook
```

or

```bash
python src/train.py
```

---

## 📁 Project Structure

```
Car_Price_Predictor/
│
├── data/
├── notebooks/
├── src/
├── models/
├── README.md
└── requirements.txt
```

---

## 🎯 Future Improvements

* Hyperparameter tuning of XGBoost
* Deploy model using Streamlit web app
* Add more real-world data
* Feature selection optimization

---

## 👨‍💻 Author

**Mayur Shahi**
Aspiring Machine Learning Engineer

---

## ⭐ Acknowledgment

This project is built for learning and demonstrating machine learning skills in real-world applications.
