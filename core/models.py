from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Coodenador(models.Model):
    nome = models.CharField(max_length=200)
    email = models.TextField()
    data_nascimento = models.DateField()
    matricula = models.IntegerField()
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome