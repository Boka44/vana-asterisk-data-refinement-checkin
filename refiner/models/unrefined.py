from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class CheckIn(BaseModel):
    user_hash: str
    timestamp: datetime
    mood: Optional[str] = None
    health_comment: Optional[str] = None
    doctor_visit: Optional[bool] = None
    health_profile_update: Optional[bool] = None
    anxiety_level: Optional[str] = None
    anxiety_details: Optional[str] = None
    pain_level: Optional[int] = None
    pain_details: Optional[str] = None
    fatigue_level: Optional[int] = None
    fatigue_details: Optional[str] = None