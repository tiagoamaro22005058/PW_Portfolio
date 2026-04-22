from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='portfolio_home'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('licenciatura/<int:id>', views.licenciatura_view, name='licenciatura'),
    path('unidades_curriculares/', views.ucs_view, name='ucs'),
    path('unidade_curricular/<int:id>', views.uc_view, name='uc'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('making_of/', views.making_of_view, name='making_of'),
]
