from app.ontology.ontology_service import get_disease_scores

def extract_symptoms(text: str):
    text = text.lower()
    symptoms = []
    if "chest pain" in text:
        symptoms.append("chest_pain")
    if "breath" in text or "dyspnea" in text:
        symptoms.append("dyspnea")

    return symptoms

# CHANGE 1: Made this function async
async def compute_probability(symptoms):
    # CHANGE 2: Added await here
    results = await get_disease_scores(symptoms)

    if not results:
        return 0.0, "unknown"

    top = results[0]
    return top["probability"], top["disease"], top["severity_weight"]

def classify_severity(probability, severity_weight):
    final_risk_score = probability * severity_weight

    if final_risk_score >= 0.6:
        return "Critical"
    elif final_risk_score >= 0.3:
        return "Moderate"
    else:
        return "Normal"
def get_hospital_recommendation(severity):
    if severity == "Critical":
        return {"name": "General Hospital", "eta_minutes": 12}
    return None

def trigger_emergency(severity):
    if severity == "Critical":
        return "Dispatched"
    return None

# CHANGE 3: Made this function async
async def process_emergency(payload):
    symptoms = extract_symptoms(payload.raw_symptoms)
    print(f"DEBUG - Symptoms extracted: {symptoms}")
    # CHANGE 4: Added await here
    probability, disease, db_severity = await compute_probability(symptoms)
    
    severity = classify_severity(probability, db_severity)
    hospital = get_hospital_recommendation(severity)
    call_status = trigger_emergency(severity)

    return {
        "extracted_terms": symptoms,
        "disease": disease,
        "severity": severity,
        "probability_score": probability,
        "hospital": hospital,
        "call_status": call_status
    }