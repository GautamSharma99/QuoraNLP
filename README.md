# 🔍 Quora Duplicate Question Detector

This is a **Flask-based web app** that detects whether two questions are semantically duplicates of each other, inspired by the [Quora Question Pairs](https://www.kaggle.com/c/quora-question-pairs) dataset.

### 🚀 Live Demo
🔗 [https://quoranlp.onrender.com](https://quoranlp.onrender.com)

---

## 📌 Features

- 🧠 ML model trained using XGBoost and TF-IDF/BoW
- 🌐 Clean and responsive frontend with HTML + CSS
- 💬 Predicts whether two questions are duplicates
- ✅ Works with user input directly from the browser
- ☁️ Deployed on [Render](https://render.com)

---

## 🧠 Tech Stack

| Layer         | Tools & Libraries                      |
|---------------|-----------------------------------------|
| Backend       | Python, Flask                          |
| ML Model      | scikit-learn, XGBoost, TF-IDF/BoW       |
| Frontend      | HTML, CSS                              |
| Deployment    | Render (Gunicorn WSGI server)          |


## ⚙️ How to Run Locally
```
-> git clone https://github.com/yourusername/QuoraNLP.git
-> cd QuoraNLP
-> pip install -r requirements.txt
-> python app.py
-> Then visit: http://localhost:5000
```

## Project Structure

```bash
├── app.py               # Flask backend
├── xgb_model.pkl        # Trained XGBoost model
├── vectorizer.pkl       # TF-IDF or CountVectorizer
├── requirements.txt     # All dependencies
├── Procfile             # For Render deployment
└── templates/
    └── index.html       # Frontend form UI
```




