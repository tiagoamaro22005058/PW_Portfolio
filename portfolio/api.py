from ninja import NinjaAPI
from .schemas import UnidadeCurricularOut, ErrorSchema, UnidadeCurricularIn
from typing import List
from .models import UnidadeCurricular


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
         response={200: UnidadeCurricularOut, 404: ErrorSchema},
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
    return 200, unidade


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


