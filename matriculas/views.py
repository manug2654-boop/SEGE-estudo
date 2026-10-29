from django.shortcuts import render

from .models import Aluno


def lista_alunos(request):
    alunos = Aluno.objects.filter(ativo=True).order_by('nome_completo')
    return render(request, 'matriculas/aluno_list.html', {'alunos': alunos})