# src/ai/prompts.py
def disease_prediction_prompt(symptoms, patient_profile):
    # Provide structured prompt: symptoms list, age, sex, comorbidities, last vitals
    profile_text = ", ".join(f"{k}: {v}" for k, v in patient_profile.items())
    prompt = f"""
You are a medical assistant that provides differential diagnoses based on user-reported symptoms.
Symptoms: {symptoms}
Patient profile: {profile_text}

Task:
1) List top 3 possible conditions with short rationale for each.
2) Provide likelihood estimate for each (Low/Moderate/High).
3) Recommend immediate next steps (tests/exams) and red flags requiring urgent care.
4) Note uncertainty and recommend consulting a clinician.

Answer in numbered bullets.
"""
    return prompt

def treatment_plan_prompt(diagnosis, patient_profile, constraints=None):
    prompt = f"""
You are a clinical decision support assistant. Patient has been diagnosed with: {diagnosis}.
Profile: {patient_profile}
Constraints: {constraints or "none"}

Provide:
- A short evidence-based treatment plan (medication names with typical adult dosing ranges),
- Non-pharmacologic/lifestyle measures,
- Suggested monitoring and follow-up timeline,
- Important contraindications or drug interactions to watch for.

Cite guideline names where possible and include confidence level.
"""
    return prompt
