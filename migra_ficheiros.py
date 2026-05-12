import os
from django.core.files import File
from django.conf import settings

from portfolio.models import Licenciatura, Docente, UnidadeCurricular, Tecnologia, Projeto, TFC, MakingOf
from artigos.models import Artigo
from escola.models import Curso

MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')

def migrar(obj, campo_nome):
    campo = getattr(obj, campo_nome)
    if not campo or not campo.name:
        return
    local_path = os.path.join(MEDIA_ROOT, campo.name)
    if not os.path.exists(local_path):
        print(f"  [não encontrado] {local_path}")
        return
    with open(local_path, 'rb') as f:
        campo.save(os.path.basename(local_path), File(f), save=True)
    print(f"  Migrado: {obj} -> {campo.url}")

print("=== Licenciatura (imagem) ===")
for obj in Licenciatura.objects.all():
    migrar(obj, 'imagem')

print("=== Docente (foto) ===")
for obj in Docente.objects.all():
    migrar(obj, 'foto')

print("=== UnidadeCurricular (imagem) ===")
for obj in UnidadeCurricular.objects.all():
    migrar(obj, 'imagem')

print("=== Tecnologia (logo) ===")
for obj in Tecnologia.objects.all():
    migrar(obj, 'logo')

print("=== Projeto (imagem) ===")
for obj in Projeto.objects.all():
    migrar(obj, 'imagem')

print("=== TFC (imagem) ===")
for obj in TFC.objects.all():
    migrar(obj, 'imagem')

print("=== MakingOf (foto_papel) ===")
for obj in MakingOf.objects.all():
    migrar(obj, 'foto_papel')

print("=== Artigo (fotografia) ===")
for obj in Artigo.objects.all():
    migrar(obj, 'fotografia')

print("=== Curso (imagem) ===")
for obj in Curso.objects.all():
    migrar(obj, 'imagem')

print("=== Migração concluída ===")
