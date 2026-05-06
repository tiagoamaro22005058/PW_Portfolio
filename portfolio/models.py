from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20)
    grau = models.CharField(max_length=50) 
    duracao_anos = models.IntegerField()
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='licenciatura/', blank=True, null=True)
    url_deisi = models.URLField(blank=True)
    url_lusofona = models.URLField(blank=True)

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=200)
    url_perfil_lusofona = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    foto = models.ImageField(upload_to='docentes/', blank=True, null=True)

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='unidades_curriculares/', blank=True, null=True)
    url_ficha = models.URLField(blank=True)
    concluida = models.BooleanField(default=False)
    docentes = models.ManyToManyField(Docente, blank=True) 

    def __str__(self):
        return f"{self.sigla} - {self.nome}"

class Tecnologia(models.Model):
    CATEGORIA_CHOICES = [
        ('linguagem', 'Linguagem de Programação'),
        ('framework', 'Framework'),
        ('base_dados', 'Base de Dados'),
        ('ferramenta', 'Ferramenta'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    url_website = models.URLField(blank=True)
    nivel_interesse = models.IntegerField(default=1)  # ex: 1 a 5
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='outro')

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    conceitos_aplicados = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    url_video_demo = models.URLField(blank=True)
    url_github = models.URLField(blank=True)
    ano_realizacao = models.IntegerField()
    nota = models.IntegerField(blank=True, null=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    def __str__(self):
        return self.titulo

class Competencia(models.Model):
    TIPO_CHOICES = [
        ('tecnica', 'Técnica'),
        ('soft', 'Soft Skill'),
        ('linguagem', 'Linguagem'),
    ]

    NIVEL_CHOICES = [
        ('basico', 'Básico'),
        ('intermedio', 'Intermédio'),
        ('avancado', 'Avançado'),
    ]

    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='tecnica')
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES, default='basico')
    descricao = models.TextField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    projetos = models.ManyToManyField(Projeto, blank=True)

    def __str__(self):
        return self.nome


class TFC(models.Model):
    titulo = models.CharField(max_length=500)
    autores = models.CharField(max_length=200)
    orientadores = models.CharField(max_length=200, blank=True, null=True)
    curso = models.CharField(max_length=200, blank=True, null=True)
    ano = models.IntegerField()
    sumario = models.TextField(blank=True)
    palavras_chave = models.CharField(max_length=500, blank=True)  # ex: "Python, Django
    areas = models.CharField(max_length=500, blank=True)
    tecnologias = models.CharField(max_length=500, blank=True)
    link_pdf = models.URLField(blank=True, null=True)
    imagem = models.ImageField(upload_to='tfcs/', blank=True, null=True)
    rating = models.IntegerField(default=1)  # 1 a 5 — destaque/interesse

    def __str__(self):
        return self.titulo

class Formacao(models.Model):
    TIPO_CHOICES = [
        ('academica', 'Académica'),
        ('curso', 'Curso Online'),
        ('certificacao', 'Certificação'),
        ('workshop', 'Workshop'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='curso')
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    certificado_url = models.URLField(blank=True)
    descricao = models.TextField(blank=True)

    class Meta:
        ordering = ['-data_inicio']  # ordena do mais recente para o mais antigo <-- visto no Claude

    def __str__(self):
        return f"{self.titulo} - {self.instituicao}"


class MakingOf(models.Model):
    entidade_relacionada = models.CharField(max_length=100)  # ex: "Licenciatura", "Projeto"
    descricao_decisao = models.TextField(blank=True)
    erros_correcoes = models.TextField(blank=True)
    justificacao_modelacao = models.TextField(blank=True)
    foto_papel = models.ImageField(upload_to='making_of/', blank=True, null=True)
    data_registo = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_registo']
        verbose_name = 'Making Of'
        verbose_name_plural = 'Making Of'

    def __str__(self):
        return f"MakingOf - {self.entidade_relacionada} ({self.data_registo.strftime('%d/%m/%Y')})"

