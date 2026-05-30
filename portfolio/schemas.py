from ninja import Schema
from typing import List, Optional


#====Unidade Curricular====
class UnidadeCurricularOut(Schema):
      id: int
      nome: str
      sigla: str
      ano: int
      semestre: int
      ects: int
      concluida: bool
      licenciatura_id: int = 1
      
class UnidadeCurricularIn(Schema):
      nome: str
      sigla: str
      ano: int
      semestre: int
      ects: int
      concluida: bool
      licenciatura_id: int = 1
      
#====Projeto====
class ProjetoOut(Schema):
      id: int
      titulo: str
      descricao: str
      nota: Optional[int]
      ano_realizacao: int
      uc_id: int

class ProjetoIn(Schema):
      titulo: str
      descricao: str
      nota: Optional[int] = None
      ano_realizacao: int
      uc_id: int
      
#====Tecnologia====      
class TecnologiaOut(Schema):
    id: int
    nome: str
    descricao: Optional[str] = None
    url_website: Optional[str] = 'https://example.com'
    nivel_interesse: int = 1
    categoria: str = 'outro'
      
class TecnologiaIn(Schema):
    nome: str
    descricao: Optional[str] = None
    url_website: Optional[str] = 'https://example.com'
    nivel_interesse: int = 1
    categoria: str = 'outro'    
      
      
      
      
      
class ErrorSchema(Schema):
    messagem: str
    
    
    
