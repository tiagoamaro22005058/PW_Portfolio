from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='portfolio_home'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('licenciatura/<int:id>', views.licenciatura_view, name='licenciatura'),

    path('unidades_curriculares/', views.ucs_view, name='ucs'),
    path('unidade_curricular/<int:id>', views.uc_view, name='uc'),

    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tecnologias/criar/', views.tecnologia_create_view, name='tecnologia_criar'),
    path('tecnologias/<int:id>/editar/', views.tecnologia_edit_view, name='tecnologia_editar'),
    path('tecnologias/<int:id>/apagar/', views.tecnologia_delete_view, name='tecnologia_apagar'),

    path('projetos/', views.projetos_view, name='projetos'),
    path('projetos/criar/', views.projeto_create_view, name='projeto_criar'),
    path('projetos/<int:id>/editar/', views.projeto_edit_view, name='projeto_editar'),
    path('projetos/<int:id>/apagar/', views.projeto_delete_view, name='projeto_apagar'),

    path('competencias/', views.competencias_view, name='competencias'),
    path('competencias/criar/', views.competencia_create_view, name='competencia_criar'),
    path('competencias/<int:id>/editar/', views.competencia_edit_view, name='competencia_editar'),
    path('competencias/<int:id>/apagar/', views.competencia_delete_view, name='competencia_apagar'),
    
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('formacoes/criar/', views.formacao_create_view, name='formacao_criar'),
    path('formacoes/<int:id>/editar/', views.formacao_edit_view, name='formacao_editar'),
    path('formacoes/<int:id>/apagar/', views.formacao_delete_view, name='formacao_apagar'),
    path('making_of/', views.making_of_view, name='making_of'),
]
