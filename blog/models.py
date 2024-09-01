from django.db import models
from PIL import Image

class Estado (models.Model):
    nome = models.CharField (max_length = 100)
    sigla = models.CharField (max_length = 5)

    def __str__ (self):
        return self.nome

class Cidade (models.Model):
    nome = models.CharField (max_length = 100)
    sigla = models.CharField (max_length = 5)

    def __str__ (self):
        return self.nome

class Campus (models.Model):
    nome = models.CharField (max_length = 100)
    sigla = models.CharField (max_length = 5)

    def __str__ (self):
        return self.sigla

class Curso (models.Model):
    nome = models.CharField (max_length = 100)
    carga_horaria = models.IntegerField ()

    def __str__ (self):
        return self.nome

class Aluno (models.Model):
    nome = models.CharField (max_length = 100)
    idade = models.IntegerField ()
    email = models.EmailField ()
    telefone = models.IntegerField ()
    endereco = models.CharField (max_length = 100)
    numero_casa = models.IntegerField ()
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete = models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete = models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    serie = models.CharField (max_length = 20)
    descricao = models.TextField (max_length = 2000)
    foto = models.ImageField (upload_to = 'foto/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        foto = Image.open(self.foto.path)

        if foto.height > 430 or foto.width > 430:
            output_size = (430, 430)
            foto.thumbnail(output_size)
            foto.save(self.foto.path)
    
    def __str__(self):
        return self.nome
