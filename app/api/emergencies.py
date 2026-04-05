from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.emergency_services import process_emergency
from app.scoring.bayesian import bayesian_score
from app.ontology.ontology_service import get_all_diseases
router = APIRouter()

class Location(BaseModel):
    latitude: float
    longitude: float

class EmergencyRequest(BaseModel):
    patient_id: str
    raw_symptoms: str
    location: Location

# Endpoint Definition
@router.post("/assess", summary="Assess Patient Symptoms")
async def assess_emergency(payload: EmergencyRequest):
    try:
        result = await process_emergency(payload)

        return {
            "status": "success",
            "assessment": {
                "extracted_terms": result["extracted_terms"],
                "severity": result["severity"],
                "probability_score": result["probability_score"],
                "disease": result["disease"]
            },
            "action_taken": {
                "hospital": result["hospital"],
                "er_notification": result["call_status"]
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
