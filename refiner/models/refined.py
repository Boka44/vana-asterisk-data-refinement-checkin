from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Base model for SQLAlchemy
Base = declarative_base()

# Define database models - the schema is generated using these
class CheckInRefined(Base):
    __tablename__ = 'check_ins'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_hash = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    checkinId = Column(String, nullable=False, unique=True)
    mood = Column(String, nullable=True)
    health_comment = Column(String, nullable=True)
    doctor_visit = Column(Boolean, nullable=True)
    health_profile_update = Column(Boolean, nullable=True)
    anxiety_level = Column(Float, nullable=True)
    anxiety_details = Column(String, nullable=True)
    pain_level = Column(Float, nullable=True)
    pain_details = Column(String, nullable=True)
    fatigue_level = Column(Float, nullable=True)
    fatigue_details = Column(String, nullable=True)
