from ninja import Schema
from typing import List, Optional
from datetime import date

      
class NoticiaOut(Schema):
    id: int
    titulo: str
    resumo: str
    url: str
    categoria: str
    fonte: str
    data_publicacao: date
    destaque: bool
    visualizacoes: int

class NoticiaIn(Schema):
    titulo: str
    resumo: str
    url: Optional[str] = ''
    categoria: str = 'outro'
    fonte: Optional[str] = ''
    data_publicacao: date
    destaque: bool = False
    visualizacoes: int = 0
      
      
      
class ErrorSchema(Schema):
    messagem: str
    
    