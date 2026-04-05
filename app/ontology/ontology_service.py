from app.core.db import ontology_collection

# 1. Add 'async' to the function definition
async def get_disease_scores(symptoms):
    diseases = []
    cursor = ontology_collection.find()

    async for record in cursor:
        # Calculate matching symptoms
        matched = list(set(symptoms) & set(record["symptoms"]))

        if matched:
            score = len(matched) / len(record["symptoms"])

            diseases.append({
                "disease": record["disease"],
                "probability": round(score, 2),
                "severity_weight": record.get("severity_weight", 0.5)
            })

    # Return the sorted list of diseases
    return sorted(diseases, key=lambda x: x["probability"], reverse=True)