from pydantic import BaseModel, Field

class OffChainSchema(BaseModel):
    name: str
    version: str
    description: str
    dialect: str
    schema_definition: str = Field(alias='schema')

    class Config:
        populate_by_name = True