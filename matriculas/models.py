from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


def validar_data_nascimento(valor):
    if valor > timezone.localdate():
        raise ValidationError('A data de nascimento não pode ser futura.')


class Aluno(models.Model):
    numero_matricula = models.CharField(max_length=12, unique=True)
    nome_completo = models.CharField(max_length=150)
    data_nascimento = models.DateField(validators=[validar_data_nascimento])
    documento = models.CharField(max_length=20, unique=True)
    morada = models.CharField(max_length=250, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.numero_matricula} - {self.nome_completo}'