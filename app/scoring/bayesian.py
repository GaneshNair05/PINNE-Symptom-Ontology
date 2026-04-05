def bayesian_score(symptoms, disease_data):
    results = []

    total_diseases = len(disease_data)

    for disease in disease_data:
        disease_name = disease["disease"]
        disease_symptoms = set(disease["symptoms"])

        # PRIOR
        prior = 1 / total_diseases

        # LIKELIHOOD
        matched = len(set(symptoms) & disease_symptoms)
        likelihood = matched / len(disease_symptoms) if disease_symptoms else 0.01

        posterior = prior * likelihood

        severity_weight = disease.get("severity", 0.5)  # 0–1

        # 🔥 FINAL SCORE (IMPORTANT)
        final_score = posterior * severity_weight
        print(f"[DEBUG] Evaluating disease: {disease_name}")
        print(f"[DEBUG] Matched symptoms: {matched}")
        print(f"[DEBUG] Posterior: {posterior}")
        print(f"[DEBUG] Severity weight: {severity_weight}")
        print(f"[DEBUG] Final score: {final_score}")
        print("------")

        results.append({
            "disease": disease_name,
            "probability": round(posterior, 4),
            "severity_weight": severity_weight,
            "final_score": round(final_score, 4)
        })


    return sorted(results, key=lambda x: x["final_score"], reverse=True)