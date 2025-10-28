# watson_mock.py
# Offline AI simulation for HealthAI — smarter, keyword-aware version

import random

def call_granite(prompt: str):
    """
    Local AI simulator that returns meaningful medical responses
    based on keywords in the prompt.
    """

    text = prompt.lower()

    # --- Symptom / disease explanations ---
    if "alzheimer" in text:
        return (
            "🧩 **Alzheimer’s Disease Symptoms:**\n"
            "- Memory loss disrupting daily life\n"
            "- Difficulty planning or solving problems\n"
            "- Confusion with time or place\n"
            "- Misplacing items and mood changes\n\n"
            "🩵 *Tip:* Early diagnosis helps in managing progression with medications and cognitive therapy."
        )

    elif "diabetes" in text:
        return (
            "🩸 **Common Symptoms of Diabetes:**\n"
            "- Increased thirst and frequent urination\n"
            "- Fatigue and blurred vision\n"
            "- Slow-healing sores or infections\n\n"
            "🩺 *Advice:* Maintain a balanced diet, regular checkups, and monitor blood sugar levels."
        )

    elif "fever" in text or "cold" in text or "flu" in text:
        return (
            "🤒 **Typical Symptoms of Fever/Flu:**\n"
            "- Elevated body temperature and chills\n"
            "- Fatigue, sore throat, and headache\n"
            "- Muscle aches and congestion\n\n"
            "🩹 *Care Tip:* Stay hydrated, rest well, and monitor for persistent high fever (>102°F)."
        )

    elif "heart" in text or "cardiac" in text:
        return (
            "❤️ **Heart-Related Warning Signs:**\n"
            "- Chest pain, shortness of breath\n"
            "- Irregular heartbeat or palpitations\n"
            "- Dizziness, fatigue, or nausea\n\n"
            "⚠️ *Urgent:* Seek medical attention immediately for chest pain or pressure."
        )

    elif "covid" in text:
        return (
            "🦠 **COVID-19 Common Symptoms:**\n"
            "- Fever, cough, fatigue\n"
            "- Loss of taste or smell\n"
            "- Shortness of breath or sore throat\n\n"
            "💡 *Note:* Isolate if symptomatic and follow local health guidelines."
        )

    elif "headache" in text or "migraine" in text:
        return (
            "💢 **Migraine Symptoms:**\n"
            "- Throbbing headache (often one-sided)\n"
            "- Nausea, sensitivity to light/sound\n"
            "- Visual disturbances (aura)\n\n"
            "🌿 *Relief:* Stay hydrated, rest in a dark room, and avoid known triggers."
        )

    elif "hypertension" in text or "blood pressure" in text:
        return (
            "💓 **High Blood Pressure (Hypertension) Signs:**\n"
            "- Often asymptomatic (‘silent killer’)\n"
            "- Occasional headaches or dizziness\n"
            "- Nosebleeds in severe cases\n\n"
            "🧘 *Management:* Reduce salt intake, exercise, and monitor BP regularly."
        )

    elif "asthma" in text:
        return (
            "🌬️ **Asthma Symptoms:**\n"
            "- Wheezing, coughing, shortness of breath\n"
            "- Tightness in the chest, especially at night or early morning\n\n"
            "💡 *Care Tip:* Avoid triggers, use prescribed inhalers, and monitor breathing pattern."
        )

    # --- General health or unknown query ---
    elif any(word in text for word in ["what", "how", "symptom", "treatment", "disease", "health"]):
        generic_responses = [
            "🩺 Could you describe your symptoms in more detail? I can help suggest possible conditions.",
            "💬 I can assist with symptom insights and general health information. Please specify your concern.",
            "🧠 I’m here to help with basic medical understanding. Could you rephrase the question with more detail?",
        ]
        return random.choice(generic_responses)

    # --- Default fallback for unrelated queries ---
    else:
        return (
            "🤖 I'm a healthcare assistant trained to discuss medical topics like symptoms, conditions, and wellness.\n"
            "Please ask something health-related for a meaningful answer."
        )
