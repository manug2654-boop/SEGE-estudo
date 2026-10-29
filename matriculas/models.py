from django.db import models


class Aluno(models.Model):
    numero_matricula = models.CharField(max_length=12, unique=True)
    nome_completo = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    documento = models.CharField(max_length=20, unique=True)
    morada = models.CharField(max_length=250, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.numero_matricula} - {self.nome_completo}'