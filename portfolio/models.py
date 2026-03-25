from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20)
    grau = models.CharField(max_length=50)  # ex: "Licenciatura", "Mestrado"
    duracao_anos = models.IntegerField()
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='licenciatura/', blank=True, null=True)
    url_deisi = models.URLField(blank=True)
    url_lusofona = models.URLField(blank=True)

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

    def __str__(self):
        return f"{self.sigla} - {self.nome}"
