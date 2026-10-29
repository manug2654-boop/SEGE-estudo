from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Aluno


@login_required
def lista_alunos(request):
    alunos = Aluno.objects.filter(ativo=True).order_by('nome_completo')
    return render(request, 'matriculas/aluno_list.html', {'alunos': alunos})