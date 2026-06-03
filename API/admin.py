from django.contrib import admin
from .models import APIKey, Noticia

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):    
    list_display = ('name', 'key', 'is_active', 'expiration_date', 'created_at')
    list_filter = ('is_active', 'expiration_date')
    search_fields = ('name', 'key')
    
    
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'resumo', 'data_publicacao')
    search_fields = ('titulo', 'resumo')