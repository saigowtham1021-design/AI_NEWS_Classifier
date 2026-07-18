# 📰 AI News Classifier

An AI-powered News Classification application built using **Natural Language Processing (NLP)** and **Machine Learning**. The application predicts the category of a news article into one of four classes:

- 🌍 World
- 🏏 Sports
- 💼 Business
- 💻 Science & Technology

The model is deployed with **Streamlit**, providing an interactive web interface for users to classify news articles.

---

## 📌 Features

- News article classification using Machine Learning
- Text preprocessing for clean input
- TF-IDF feature extraction
- Support Vector Machine (SVM) classifier
- Interactive Streamlit web application
- Fast and accurate predictions

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Joblib

---

## 📂 Dataset

**Dataset:** AG News Dataset

The dataset contains four news categories:

| Label | Category             |
|-------|----------------------|
| 1     | World                |
| 2     | Sports               |
| 3     | Business             |
| 4     | Science & Technology |

---

## 🔄 Project Workflow

1. Load the AG News dataset
2. Perform text preprocessing
   - Convert text to lowercase
   - Remove URLs
   - Remove punctuation
   - Remove numbers
   - Tokenization
   - Stopword removal
   - Lemmatization
3. Convert text into numerical vectors using TF-IDF
4. Train multiple Machine Learning models
5. Compare model performance
6. Select the best-performing model (Support Vector Machine)
7. Save the trained model and vectorizer
8. Build a Streamlit web application
9. Predict the category of new news articles

---

## 📁 Project Structure

```
News-Classifier/
│
├── app.py
├── best_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
└── dataset/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/saigowtham1021-design/News-Classifier.git
```

Move into the project folder

```bash
cd News-Classifier
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📷 Sample Prediction

**Input**

```
India defeated Australia by six wickets in the final match.
```

**Output**

```
🏏 Sports
```

---

## 🎯 Machine Learning Model

The following models were trained and evaluated:

- Multinomial Naive Bayes
- Logistic Regression
- Support Vector Machine (SVM)

After evaluation, **Support Vector Machine (SVM)** achieved the best performance and was selected for deployment.

---

## 📦 Deployment

The application is deployed using **Streamlit Community Cloud**.

---

## 📈 Future Improvements

- Add prediction confidence scores
- Display top keywords influencing predictions
- Support multiple languages
- Improve UI with custom themes
- Add preprocessing pipeline inside the application

---

## 👨‍💻 Author

**Gullapudi Shanmuka Ramana Sai Gowtham**

B.Tech – Computer Science and Engineering (AI & ML)

GitHub: https://github.com/saigowtham1021-design

---

## ⭐ If you found this project useful, please consider giving it a Star.
