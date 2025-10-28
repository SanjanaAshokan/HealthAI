# src/ml/predictor.py
# Mock disease predictor (no ML model required)

def predict_from_symptoms(symptom_text):
    """
    Simulates a disease prediction model using simple keyword matching.
    Works even without clf.joblib or vectorizer.joblib.
    """

    text = symptom_text.lower()

    if any(word in text for word in ["cough", "cold", "sneeze", "throat"]):
        preds = [("Common Cold", 0.85), ("Allergy", 0.1), ("Flu", 0.05)]

    elif any(word in text for word in ["fever", "chills", "tired", "headache"]):
        preds = [("Viral Fever", 0.75), ("COVID-19", 0.15), ("Malaria", 0.1)]

    elif any(word in text for word in ["pain", "cramp", "stomach", "abdomen"]):
        preds = [("Gastritis", 0.6), ("Ulcer", 0.25), ("Food Poisoning", 0.15)]

    elif any(word in text for word in ["rash", "itch", "skin"]):
        preds = [("Allergic Reaction", 0.7), ("Eczema", 0.2), ("Infection", 0.1)]

    else:
        preds = [("General Fatigue", 0.5), ("Stress", 0.3), ("Dehydration", 0.2)]

    return preds
