from pydantic import BaseModel

class HumanCreate(BaseModel):
    dna: list[str]