# Sample symptoms and basic advice
medical_advice = {
    "headache": "Drink water, rest, and avoid bright screens.",
    "fever": "Take a fever-reducing medicine, stay hydrated, and rest.",
    "stomach pain": "Avoid solid food, drink clear liquids, and rest.",
    "chest pain": "Seek immediate medical attention if severe.",
    "dizziness": "Sit down, take deep breaths, and stay hydrated."
}

# Function to provide advice
def get_medical_advice(symptom):
    return medical_advice.get(symptom, "Please consult a healthcare professional.")

# User input
symptom = "fever"  # Example symptom

# Get advice
advice = get_medical_advice(symptom)
print(f"Advice for {symptom}: {advice}")
