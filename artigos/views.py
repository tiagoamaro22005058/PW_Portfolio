from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Artigo, Like, Comentario
from .forms import ArtigoForm, ComentarioForm


def _is_autor(user):
    return user.is_authenticated and user.groups.filter(name='autores').exists()


def lista_artigos(request):
    artigos = Artigo.objects.order_by('-data_criacao')
    return render(request, 'artigos/lista.html', {'artigos': artigos})


def detalhe_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    sessao = request.session.session_key
    if not sessao:
        request.session.create()
        sessao = request.session.session_key
    ja_gostou = Like.objects.filter(artigo=artigo, sessao=sessao).exists()
    comentarios = artigo.comentarios.order_by('data')
    form_comentario = ComentarioForm()
    return render(request, 'artigos/detalhe.html', {
        'artigo': artigo,
        'ja_gostou': ja_gostou,
        'comentarios': comentarios,
        'form_comentario': form_comentario,
    })


@login_required
def criar_artigo(request):
    if not _is_autor(request.user):
        raise PermissionDenied
    form = ArtigoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('detalhe_artigo', pk=artigo.pk)
    return render(request, 'artigos/form.html', {'form': form, 'titulo': 'Novo Artigo'})


@login_required
def editar_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if not _is_autor(request.user) or artigo.autor != request.user:
        raise PermissionDenied
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('detalhe_artigo', pk=artigo.pk)
    return render(request, 'artigos/form.html', {'form': form, 'titulo': 'Editar Artigo'})


def like_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if not request.session.session_key:
        request.session.create()
    sessao = request.session.session_key
    like, created = Like.objects.get_or_create(artigo=artigo, sessao=sessao)
    if not created:
        like.delete()
    return redirect('detalhe_artigo', pk=pk)


@login_required
def adicionar_comentario(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()
    return redirect('detalhe_artigo', pk=pk)
