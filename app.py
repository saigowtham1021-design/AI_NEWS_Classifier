import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("best_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Category labels
labels = {
    1: "🌍 World",
    2: "🏏 Sports",
    3: "💼 Business",
    4: "💻 Science & Technology"
}

st.set_page_config(
    page_title="AI News Classifier",
    page_icon="📰",
    layout="centered"
)

st.title("📰 AI News Classifier")
st.markdown("### Classify News Articles using Machine Learning")

st.write("---")

news = st.text_area(
    "📝 Enter News Article",
    height=200,
    placeholder="Type or paste a news article here..."
)

if st.button("🚀 Predict Category"):

    if news.strip() == "":
        st.warning("Please enter a news article.")
    else:
        news_vector = vectorizer.transform([news])
        prediction = model.predict(news_vector)[0]

        st.success(f"### Predicted Category: {labels[prediction]}")

st.write("---")
st.caption("Developed using Python, Scikit-learn, TF-IDF, SVM and Streamlit")