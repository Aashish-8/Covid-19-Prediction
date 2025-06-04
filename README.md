# 🧠 COVID-19 ICU Prediction using Machine Learning

This project predicts whether a COVID-19 patient is likely to need **ICU care** based on their health data using a **Machine Learning model** and provides a user-friendly interface built with **Streamlit**.

---

## 🚀 Features

* ✅ COVID-19 data preprocessing using **Pandas**
* ✅ ICU prediction model trained using **Scikit-learn**
* ✅ Simple and clean **Streamlit web interface**
* ✅ Interactive inputs for medical conditions (e.g. age, obesity, diabetes)
* ✅ Real-time prediction result

---

## 📂 Project Structure

```
📁 Big-Data-COVID-ICU-Prediction/
│
├── covid_clean_sample.csv       # Cleaned COVID dataset
├── icu_predict_model.pkl        # Trained ML model (Logistic Regression)
├── app.py                       # Streamlit web app code
├── model_training.py            # ML model training script
└── README.md                    # This file
```

---

## 🛠 Tech Stack

| Tool            | Purpose                             |
| --------------- | ----------------------------------- |
| Python 🐍       | Programming Language                |
| Pandas 🧾       | Data Cleaning & Processing          |
| Scikit-learn 📊 | Model Training (LogisticRegression) |
| Streamlit 🌐    | Web App Interface                   |
| Joblib 💾       | Model Serialization                 |

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Aashish-8/COVID-19-Predictor.git
cd COVID-19-Predictor
```

### 2. Install dependencies

Make sure you have Python 3.7+ installed. Then:

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install pandas scikit-learn streamlit joblib
```

### 3. Run the web app

```bash
streamlit run app.py
```

---

## 🧠 Model Info

* **Model**: Logistic Regression
* **Target**: Predict `ICU` need (0 = No, 1 = Yes)
* **Features**: Age, Sex, Obesity, Diabetes, Tobacco use, etc.
* **Dataset**: Sampled and cleaned COVID-19 health records

---

## 🖼️ Screenshot

> *Add a screenshot of your app UI here once it runs*

---

## 🙌 Acknowledgements

* COVID-19 data inspired by public health datasets.
* Built by [Aashish Vishal Bhabal](https://github.com/your-username) as a learning project.

---

## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

Would you like me to:

* Create the `requirements.txt`?
* Help write the `model_training.py` if not already done?
* Add badges or deploy it on Streamlit Cloud?

Let me know and I’ll help you complete the GitHub setup.
