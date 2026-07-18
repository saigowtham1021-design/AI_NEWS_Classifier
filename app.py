import streamlit as st
import joblib
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# -----------------------------
# Download NLTK Resources
# -----------------------------
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

# -----------------------------
# Load Model & Vectorizer
# -----------------------------
model = joblib.load("best_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")   # Change if your filename is different

# -----------------------------
# Initialize NLP Objects
# -----------------------------
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# -----------------------------
# Preprocessing Function
# -----------------------------
def preprocess(text):
    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove Numbers
    text = re.sub(r"\d+", "", text)

    # Remove Punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # Tokenization
    words = word_tokenize(text)

    # Remove Stopwords
    words = [word for word in words if word not in stop_words]

    # Lemmatization
    words = [lemmatizer.lemmatize(word) for word in words]

    # Join back into sentence
    return " ".join(words)

# -----------------------------
# Labels
# -----------------------------
labels = {
    1: "🌍 World",
    2: "🏏 Sports",
    3: "💼 Business",
    4: "💻 Science & Technology"
}

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="AI News Classifier",
    page_icon="📰",
    layout="centered"
)

st.title("📰 AI News Classifier")

st.write("Classify a news article into one of four categories using Machine Learning.")

st.write("---")

news = st.text_area(
    "Enter News Article",
    height=200,
    placeholder="Type or paste the news article you have..."
)

if st.button("🚀 Predict Category"):

    if news.strip() == "":
        st.warning("⚠ Please enter a news article.")

    else:

        # Preprocess input
        clean_news = preprocess(news)

        # Convert to TF-IDF
        news_vector = vectorizer.transform([clean_news])

        # Prediction
        prediction = model.predict(news_vector)[0]

        # Display result
        st.success(f"### Predicted Category: {labels[prediction]}")
st.write("---")
st.caption("Developed using Python • Scikit-learn • TF-IDF • SVM • Streamlit")