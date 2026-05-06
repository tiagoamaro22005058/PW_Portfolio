from django.contrib import admin
from .models import Artigo, Comentario, Like

admin.site.register(Artigo)
admin.site.register(Comentario)
admin.site.register(Like)
