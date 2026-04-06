import spacy

nlp = spacy.load("en_core_web_sm")

# 🔹 Mapping layer 
SYMPTOM_MAP = {
    "shortness_of_breath": "dyspnea",
    "breathing_difficulty": "dyspnea",
    "chest_pain": "chest_pain",
    "tightness_in_chest": "chest_pain"
}

def normalize(symptoms):
    return [SYMPTOM_MAP.get(s, s) for s in symptoms]


def extract_symptoms(text: str):
    doc = nlp(text)

    raw_symptoms = []
    for ent in doc.ents:
        raw_symptoms.append(ent.text.lower().replace(" ", "_"))

    return normalize(list(set(raw_symptoms)))