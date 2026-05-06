from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('registo/', views.registo_view, name='registo_view'),
    path('magic/', views.magic_link_request_view, name='magic_link_request'),
    path('magic/<uuid:token>/', views.magic_link_verify_view, name='magic_link_verify'),
]
