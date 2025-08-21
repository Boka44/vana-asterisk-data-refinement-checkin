from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class CheckIn(BaseModel):
    user_hash: str
    timestamp: datetime
    checkinId: str
    mood: Optional[str] = None
    health_comment: Optional[str] = None
    doctor_visit: Optional[bool] = None
    health_profile_update: Optional[bool] = None
    anxiety_level: Optional[float] = None
    anxiety_details: Optional[str] = None
    pain_level: Optional[float] = None
    pain_details: Optional[str] = None
    fatigue_level: Optional[float] = None
    fatigue_details: Optional[str] = None

    class Config:
        from_attributes = True