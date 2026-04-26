from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    Licenciatura, UnidadeCurricular, Tecnologia,
    Projeto, Competencia, Formacao, MakingOf
)
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm


def home_view(request):
    return render(request, 'portfolio/home.html')


def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.prefetch_related('unidadecurricular_set').all()  # Busca todas as licenciaturas com as suas UCs pré-carregadas
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})


def licenciatura_view(request, id):
    licenciatura = Licenciatura.objects.prefetch_related('unidadecurricular_set').get(id=id)
    return render(request, 'portfolio/licenciatura.html', {'licenciatura': licenciatura})


def ucs_view(request):
    ucs = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes').all() # Busca todas as UCs com a licenciatura (select_related) e docentes (prefetch_related) pré-carregados
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})


def uc_view(request, id):
    uc = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes', 'projeto_set').get(id=id)
    return render(request, 'portfolio/uc.html', {'uc': uc})


def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})


def projetos_view(request):
    projetos = Projeto.objects.select_related('uc').prefetch_related('tecnologias').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})


def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('tecnologias').order_by('tipo')
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})


def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})


def making_of_view(request):
    registos = MakingOf.objects.all()
    return render(request, 'portfolio/making_of.html', {'registos': registos})


def sobre_view(request):
    tecnologias = Tecnologia.objects.filter(
        nome__in=['Django', 'HTML', 'CSS', 'Git', 'GitHub']
    ).order_by('categoria', 'nome')
    registos = MakingOf.objects.all()
    modelos = [
        {'icone': '🎓', 'nome': 'Licenciatura',        'relacoes': None,                           'campos': ['nome, sigla, grau', 'duração, descrição', 'imagem, URLs']},
        {'icone': '📚', 'nome': 'UnidadeCurricular',   'relacoes': '→ Licenciatura (FK) · → Docente (M2M)', 'campos': ['nome, sigla', 'ano, semestre, ECTS']},
        {'icone': '👤', 'nome': 'Docente',             'relacoes': None,                           'campos': ['nome, email', 'foto, URL perfil']},
        {'icone': '🗂️', 'nome': 'Projeto',             'relacoes': '→ UC (FK) · → Tecnologia (M2M)', 'campos': ['título, descrição, nota', 'ano, GitHub, demo, imagem']},
        {'icone': '⚙️', 'nome': 'Tecnologia',          'relacoes': None,                           'campos': ['nome, categoria', 'descrição, logo', 'nível de interesse']},
        {'icone': '🧠', 'nome': 'Competência',         'relacoes': '→ Tecnologia (M2M) · → Projeto (M2M)', 'campos': ['nome, tipo, nível', 'descrição']},
        {'icone': '📜', 'nome': 'Formação',            'relacoes': None,                           'campos': ['título, instituição, tipo', 'datas, certificado URL']},
        {'icone': '📝', 'nome': 'MakingOf',            'relacoes': None,                           'campos': ['entidade relacionada', 'decisões, erros', 'justificações, foto']},
    ]
    return render(request, 'portfolio/sobre.html', {
        'tecnologias': tecnologias,
        'registos': registos,
        'modelos': modelos,
    })

# ── Projeto CRUD ──────────────────────────────────────

def projeto_create_view(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/projeto_form.html', {'form': form, 'titulo': 'Novo Projeto'})


def projeto_edit_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/projeto_form.html', {'form': form, 'titulo': f'Editar: {projeto.titulo}'})


def projeto_delete_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')
    return render(request, 'portfolio/projeto_confirm_delete.html', {'projeto': projeto})


# ── Tecnologia CRUD ──────────────────────────────────────

def tecnologia_create_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/tecnologia_form.html', {'form': form, 'titulo': 'Nova Tecnologia'})


def tecnologia_edit_view(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/tecnologia_form.html', {'form': form, 'titulo': f'Editar: {tecnologia.nome}'})


def tecnologia_delete_view(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')
    return render(request, 'portfolio/tecnologia_confirm_delete.html', {'tecnologia': tecnologia})


# ── Competencia CRUD ─────────────────────────────────────

def competencia_create_view(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/competencia_form.html', {'form': form, 'titulo': 'Nova Competência'})


def competencia_edit_view(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    form = CompetenciaForm(request.POST or None, instance=competencia)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/competencia_form.html', {'form': form, 'titulo': f'Editar: {competencia.nome}'})


def competencia_delete_view(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')
    return render(request, 'portfolio/competencia_confirm_delete.html', {'competencia': competencia})


# ── Formacao CRUD ────────────────────────────────────────

def formacao_create_view(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/formacao_form.html', {'form': form, 'titulo': 'Nova Formação'})


def formacao_edit_view(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    form = FormacaoForm(request.POST or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/formacao_form.html', {'form': form, 'titulo': f'Editar: {formacao.titulo}'})


def formacao_delete_view(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('formacoes')
    return render(request, 'portfolio/formacao_confirm_delete.html', {'formacao': formacao})
