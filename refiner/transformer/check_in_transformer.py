from typing import Dict, Any, List
from refiner.transformer.base_transformer import DataTransformer
from refiner.models.refined import Base, CheckInRefined
from refiner.models.unrefined import CheckIn
from refiner.utils.date import parse_timestamp

class CheckInTransformer(DataTransformer):
    """
    Transformer for check-in data as defined in the schema.
    """
    
    def transform(self, data: Dict[str, Any]) -> List[Base]:
        """
        Transform raw check-in data into SQLAlchemy model instances.
        
        Args:
            data: Dictionary containing check-in data
            
        Returns:
            List of SQLAlchemy model instances
        """

        logging.info(f"Transforming check-in data: {data}")
        # Validate data with Pydantic
        unrefined_check_in = CheckIn.model_validate(data)
        
        # Create check-in instance
        check_in = CheckInRefined(
            user_hash=unrefined_check_in.user_hash,
            timestamp=unrefined_check_in.timestamp,
            mood=unrefined_check_in.mood,
            health_comment=unrefined_check_in.health_comment,
            doctor_visit=unrefined_check_in.doctor_visit,
            health_profile_update=unrefined_check_in.health_profile_update,
            anxiety_level=unrefined_check_in.anxiety_level,
            anxiety_details=unrefined_check_in.anxiety_details,
            pain_level=unrefined_check_in.pain_level,
            pain_details=unrefined_check_in.pain_details,
            fatigue_level=unrefined_check_in.fatigue_level,
            fatigue_details=unrefined_check_in.fatigue_details
        )
        
        return [check_in] 