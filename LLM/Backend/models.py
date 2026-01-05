from pydantic import BaseModel

class promptRequest(BaseModel):
    prompt: str