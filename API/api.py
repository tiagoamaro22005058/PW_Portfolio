
from ninja import NinjaAPI
from ninja.security import APIKeyHeader
from .models import APIKey, Noticia
from .schemas import ErrorSchema, NoticiaOut, NoticiaIn
from typing import List

## Esta classe serve para validar uma API Key enviada no header HTTP 
### e decidir se o utilizador pode aceder à API.
class AuthAPIKey(APIKeyHeader):
    # O nome do cabeçalho HTTP onde a chave será enviada
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        try:
            # Procura a chave na base de dados
            api_key = APIKey.objects.get(key=key)
            # Usa o método que criámos no modelo para validar estado e data
            if api_key.is_valid():
                return api_key.name
        except APIKey.DoesNotExist:
            pass
        return None  # Se retornar None, o Ninja devolve erro 401 Unauthorized


api = NinjaAPI()

#listar noticias
@api.get("noticias/",
         response={200: List[NoticiaOut]},
         tags=["Noticias"],
         description="Lista todas as noticias"
        )
def lista_Noticias(request):
    return 200, Noticia.objects.all()


#ver noticia por id
@api.get("noticias/{noticia_id}",
         response={200: NoticiaOut, 404: ErrorSchema},
         tags=["Noticias"],
         description="Ver detalhes de uma noticia por id"
        )
def ver_Noticia(request, noticia_id: int):
    try:
        return 200, Noticia.objects.get(id=noticia_id)
    except Noticia.DoesNotExist:
        return 404, {"messagem": "Notícia não encontrada"}


#criar noticia
@api.post("noticias/",
          response={201: NoticiaOut},
          tags=["Noticias"],
          description="Criar uma nova noticia",
          auth=AuthAPIKey()
         )
def criar_Noticia(request, data: NoticiaIn):
    return 201, Noticia.objects.create(**data.dict())


#atualizar noticia
@api.put("noticias/{noticia_id}",
         response={200: NoticiaOut, 404: ErrorSchema},
         tags=["Noticias"],
         description="Atualizar uma noticia por id",
         auth=AuthAPIKey()
        )
def atualizar_Noticia(request, noticia_id: int, data: NoticiaIn):
    try:
        noticia = Noticia.objects.get(id=noticia_id)
    except Noticia.DoesNotExist:
        return 404, {"messagem": "Notícia não encontrada"}
    for attr, value in data.dict().items():
        setattr(noticia, attr, value)
    noticia.save()
    return 200, noticia


#apagar noticia
@api.delete("noticias/{noticia_id}",
            response={204: None, 404: ErrorSchema},
            tags=["Noticias"],
            description="Excluir uma noticia por id",
            auth=AuthAPIKey()
           )
def apagar_Noticia(request, noticia_id: int):
    try:
        noticia = Noticia.objects.get(id=noticia_id)
    except Noticia.DoesNotExist:
        return 404, {"messagem": "Notícia não encontrada"}
    noticia.delete()
    return 204, None