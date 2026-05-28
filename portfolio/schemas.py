from ninja import Schema
from typing import List, Optional

class UnidadeCurricularOut(Schema):
      id: int
      nome: str
      sigla: str
      ano: int
      semestre: int
      ects: int
      concluida: bool
      licenciatura_id: int

    
class UnidadeCurricularIn(Schema):
      nome: str
      sigla: str
      ano: int
      semestre: int
      ects: int
      concluida: bool
      licenciatura_id: int
      
      
      
class ErrorSchema(Schema):
    messagem: str