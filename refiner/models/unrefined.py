from typing import Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime

class CheckIn(BaseModel):
    user_hash: str
    timestamp: datetime
    mood: Optional[str] = None
    health_comment: Optional[str] = None
    doctor_visit: Optional[bool] = None
    health_profile_update: Optional[bool] = None
    anxiety_level: Optional[Union[str, int]] = None
    anxiety_details: Optional[str] = None
    pain_level: Optional[Union[str, int]] = None
    pain_details: Optional[str] = None
    fatigue_level: Optional[Union[str, int]] = None
    fatigue_details: Optional[str] = None

    class Config:
        from_attributes = True

    def __init__(self, **data):
        super().__init__(**data)
        if isinstance(self.anxiety_level, int):
            self.anxiety_level = str(self.anxiety_level)
        if isinstance(self.pain_level, int):
            self.pain_level = str(self.pain_level)
        if isinstance(self.fatigue_level, int):
            self.fatigue_level = str(self.fatigue_level)