from typing import Optional
from pydantic import BaseModel, Field

from refiner.models.offchain_schema import OffChainSchema

class Output(BaseModel):
    refinement_url: Optional[str] = None
    schema_data: Optional[OffChainSchema] = Field(default=None, alias='schema')

    class Config:
        populate_by_name = True