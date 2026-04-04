from django.contrib import admin
from .models import Licenciatura, UnidadeCurricular, Docente, Projeto, Tecnologia, TFC, Competencia, Formacao, MakingOf

@admin.register(Licenciatura) # em vez de por admin.site.register(Licenciatura, Licenciatura Admin) <-- Visto no Claude
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'grau', 'duracao_anos')
    search_fields = ('nome', 'sigla')

@admin.register(UnidadeCurricular) #mesma coisa que em cima
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'ano', 'semestre', 'ects', 'concluida')
    list_filter = ('ano', 'semestre', 'concluida', 'licenciatura')
    search_fields = ('nome', 'sigla')

@admin.register(Docente) #mesma coisa que em cima
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome',)

@admin.register(Projeto) #mesma coisa que em cima
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'uc', 'ano_realizacao', 'nota')
    list_filter = ('ano_realizacao', 'uc')
    search_fields = ('titulo',)

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'nivel_interesse')
    list_filter = ('categoria',)
    search_fields = ('nome',)

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autores', 'ano', 'rating')
    list_filter = ('ano', 'rating')
    search_fields = ('titulo', 'autores', 'palavras_chave', 'areas')


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'nivel')
    list_filter = ('tipo', 'nivel')
    search_fields = ('nome',)

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instituicao', 'tipo', 'data_inicio', 'data_fim')
    list_filter = ('tipo',)
    search_fields = ('titulo', 'instituicao')

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('entidade_relacionada', 'data_registo')
    list_filter = ('entidade_relacionada',)
    search_fields = ('entidade_relacionada', 'descricao_decisao')