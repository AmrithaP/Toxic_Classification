import streamlit as st
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer



def load_tfidf():
    tfidf = pickle.load(open("tf_idf.pkt", "rb"))
    return tfidf

def load_model():
    nb_model = pickle.load(open("toxic_model.pkt", "rb"))
    return nb_model

st.header("Toxicity Detection App")

st.subheader("Input your text")

text_input = st.text_input("Enter your text")

# Disable the button if the text_input is empty
button_disabled = not text_input

# Create a button with the conditional disabled attribute
button_clicked = st.button("Analyse", disabled=button_disabled)

if button_clicked and text_input:

    vect1 = load_tfidf()
    text_tfidf = vect1.transform([text_input]).toarray()
    nb_model = load_model()
    prediction = nb_model.predict(text_tfidf)
    result = "Toxic" if prediction == 1 else "Non-Toxic"
    st.subheader("Result:")
    st.info("The result is "+ result + ".")