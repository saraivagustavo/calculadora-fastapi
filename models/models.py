from pydantic import BaseModel

class OperacaoRequest(BaseModel):
    a: float
    b: float

class OperacaoResponse(BaseModel):
    resultado: float