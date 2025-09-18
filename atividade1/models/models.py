from pydantic import BaseModel

class OperacaoRequest(BaseModel): #formata a requisição que vai ser enviada como parâmetro para as funções
    a: float
    b: float

class OperacaoResponse(BaseModel): #formata o return das operações
    resultado: float