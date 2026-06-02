from ninja import NinjaAPI
from .schemas import UnidadeCurricularOut, ErrorSchema, UnidadeCurricularIn, ProjetoOut, ProjetoIn, TecnologiaOut, TecnologiaIn, NoticiaOut
from typing import List
from .models import Noticia, UnidadeCurricular, Projeto, Tecnologia, Noticia


api = NinjaAPI(
    title="API RESTfull portfolio",
    
)   

####UnidadesCurriculares####

#listar unidadeCurricular
@api.get("unidadesCurriculares/",
         response={200: List[UnidadeCurricularOut]},
         tags=["UnidadesCurriculares"],
         description="Lista todas as unidades curriculares"
        )
def lista_UnidadesCurriculares(request):
    return 200, UnidadeCurricular.objects.all()


#ver unidadeCurricular por id
@api.get("unidadesCurriculares/{unidade_id}", 
         response={200: UnidadeCurricularOut, 404: ErrorSchema}, #Pode der um In ?
         tags=["UnidadesCurriculares"],
         description="Ver detalhes de uma unidade curricular por id"
         )
def ver_UnidadeCurricular(request, unidade_id):
    try:
        return 200, UnidadeCurricular.objects.get(id=unidade_id)
    except:
        return 404, {"messagem": "Unidade Curricular não encontrada"}


#criar unidadeCurricular
@api.post("unidadesCurriculares/",
          response={201: UnidadeCurricularOut},
          tags=["UnidadesCurriculares"],
          description="Criar uma nova unidade curricular"
          )
def criar_UnidadeCurricular(request, data:UnidadeCurricularIn):
    return 201, UnidadeCurricular.objects.create(**data.dict())


#atualizar unidadeCurricular
@api.put("unidadesCurriculares/{unidade_id}",
         response={200: UnidadeCurricularOut, 404: ErrorSchema},
         tags=["UnidadesCurriculares"],
         description="Atualizar uma unidade curricular por id"
        )
def atualizar_UnidadeCurricular(request, unidade_id: int, data: UnidadeCurricularIn):
    try:
        unidade = UnidadeCurricular.objects.get(id=unidade_id)
    except UnidadeCurricular.DoesNotExist:
        return 404, {"messagem": "Unidade Curricular não encontrada"}
    for attr, value in data.dict().items():
        setattr(unidade, attr, value)
    unidade.save()
    return 200, unidade  #nao sei como por mensagem de sucesso


#apagar unidadeCurricular
@api.delete("unidadesCurriculares/{unidade_id}",
            response={204: None, 404: ErrorSchema},
            tags=["UnidadesCurriculares"],
            description="Excluir uma unidade curricular por id"
            )
def apagar_UnidadeCurricular(request, unidade_id: int):
    try:
        unidade = UnidadeCurricular.objects.get(id=unidade_id)
    except UnidadeCurricular.DoesNotExist:
        return 404, {"messagem": "Unidade Curricular não encontrada"}
    unidade.delete()
    return 204, {"messagem": "Unidade Curricular excluída com sucesso"}


####Projetos####

#listar Projetos
@api.get("projetos/",
         response={200: List[ProjetoOut]},
         tags=["Projetos"],
         description="Lista todos os projetos"
        )
def lista_Projetos(request):
    return 200, Projeto.objects.select_related("uc").all()


#ver projeto por id
@api.get("projetos/{projeto_id}",
         response={200: ProjetoOut, 404: ErrorSchema},
         tags=["Projetos"],
         description="Ver detalhes de um projeto por id"
         )
def ver_Projeto(request, projeto_id: int):
    try:
        return 200, Projeto.objects.select_related("uc").get(id=projeto_id)
    except Projeto.DoesNotExist:
        return 404, {"messagem": "Projeto não encontrado"}
   
    
#criar unidadeCurricular
@api.post("projetos/",
          response={201: ProjetoOut},
          tags=["Projetos"],
          description="Criar um novo projeto"
          )
def criar_Projeto(request, data: ProjetoIn):
    return 201, Projeto.objects.create(**data.dict())    


#atualizar projectos
@api.put("projetos/{projeto_id}",
         response={200: ProjetoOut, 404: ErrorSchema},
         tags=["Projetos"],
         description="Atualizar um projeto por id"
        )
def atualizar_Projeto(request, projeto_id: int, data: ProjetoIn):
    try:
        projeto = Projeto.objects.get(id=projeto_id)
    except Projeto.DoesNotExist:
        return 404, {"messagem": "Projeto não encontrado"}
    for attr, value in data.dict().items():
        setattr(projeto, attr, value)
    projeto.save()
    return 200, projeto  #nao sei como por mensagem de sucesso  


#apagar projeto
@api.delete("projetos/{projeto_id}",
            response={204: None, 404: ErrorSchema},
            tags=["Projetos"],
            description="Excluir um projeto por id"
            )
def apagar_Projeto(request, projeto_id: int):
    try:
        projeto = Projeto.objects.get(id=projeto_id)
    except Projeto.DoesNotExist:
        return 404, {"messagem": "Projeto não encontrado"}
    projeto.delete()
    return 204, {"messagem": "Projeto excluído com sucesso"}


####Projetos####

#listar tecnologias
@api.get("tecnologias/",
         response={200: List[TecnologiaOut]},
         tags=["Tecnologias"],
         description="Lista todas as tecnologias"
        )
def lista_Tecnologias(request):
    return 200, Tecnologia.objects.all()

#ver tecnologia por id
@api.get("tecnologias/{tecnologia_id}",
         response={200: TecnologiaOut, 404: ErrorSchema},
         tags=["Tecnologias"],
         description="Ver detalhes de uma tecnologia por id"
         )
def ver_Tecnologia(request, tecnologia_id: int):
    try:
        return 200, Tecnologia.objects.get(id=tecnologia_id)
    except Tecnologia.DoesNotExist:
        return 404, {"messagem": "Tecnologia não encontrada"}   
    
    
#criar tecnologia
@api.post("tecnologias/",
          response={201: TecnologiaOut},
          tags=["Tecnologias"],
          description="Criar uma nova tecnologia"
          )
def criar_Tecnologia(request, data: TecnologiaIn):
    return 201, Tecnologia.objects.create(**data.dict())    

#atualizar tecnologia
@api.put("tecnologias/{tecnologia_id}",
         response={200: TecnologiaOut, 404: ErrorSchema},
         tags=["Tecnologias"],
         description="Atualizar uma tecnologia por id"
        )
def atualizar_Tecnologia(request, tecnologia_id: int, data: TecnologiaIn):
    try:
        tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    except Tecnologia.DoesNotExist:
        return 404, {"messagem": "Tecnologia não encontrada"}
    for attr, value in data.dict().items():
        setattr(tecnologia, attr, value)
    tecnologia.save()
    return 200, tecnologia  #nao sei como por mensagem de sucesso   

#apagar tecnologia
@api.delete("tecnologias/{tecnologia_id}",
            response={204: None, 404: ErrorSchema},
            tags=["Tecnologias"],
            description="Excluir uma tecnologia por id"
            )
def apagar_Tecnologia(request, tecnologia_id: int):     
    try:
        tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    except Tecnologia.DoesNotExist:
        return 404, {"messagem": "Tecnologia não encontrada"}
    tecnologia.delete()
    return 204, {"messagem": "Tecnologia excluída com sucesso"}


####Noticas####

#listar noticias
@api.get("noticias/",
         response={200: List[NoticiaOut]},
         tags=["Noticias"],
         description="Lista todas as noticias"
        )
def lista_Noticias(request):
    return 200, Noticia.objects.all()