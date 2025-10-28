# src/ml/model_train.py (toy example)
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("src/ml/sample_dataset.csv")  # columns: symptoms_text, diagnosis

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["symptoms_text"])
y = df["diagnosis"]

clf = LogisticRegression(max_iter=200)
clf.fit(X, y)

joblib.dump(clf, "src/ml/clf.joblib")
joblib.dump(vectorizer, "src/ml/vectorizer.joblib")
