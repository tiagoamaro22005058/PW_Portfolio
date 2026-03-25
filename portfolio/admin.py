from django.contrib import admin
from .models import Licenciatura

@admin.register(Licenciatura) # em vez de por admin.site.register(Licenciatura, Licenciatura Admin) <-- Visto no Claude
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'grau', 'duracao_anos')
    search_fields = ('nome', 'sigla')
