from django.contrib import admin
from .models import Licenciatura, UnidadeCurricular, Docente, Projeto

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