# 📊 Student Placement Prediction App

**A Flask web application that predicts whether a student can get placed using a trained Machine Learning model.**

This project uses student academic attributes (like CGPA, test scores, etc.) to estimate the likelihood of getting placed in campus recruitment. It’s deployed using Render and can be extended into a full career guidance tool.

---

## 📌 Tech Stack

- 🐍 Python
- 🧠 Machine Learning (scikit-learn)
- 📊 Flask (Web backend)
- 📦 Render (Deployment)
- 📄 HTML & Jinja templates

---

## 📁 Project Structure
├── app.py
├── model.pkl
├── templates/
├── requirements.txt
├── Procfile
├── runtime.txt
└── README.md
## 🧠 How It Works

1. The app loads a pretrained ML model (`model.pkl`).
2. Users input academic information through a web form.
3. The model predicts if the student **will be placed** or **not**.
4. The result is displayed on a web page.

---

## 🚀 Usage

### 🏃‍♂️ Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/MAN123-SAH/placement-prediction.git
   cd placement-prediction
   Create virtual environment & install:

2. python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Run:
flask run
