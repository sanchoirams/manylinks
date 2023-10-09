from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from links.models import Link


@login_required
def pagina_inicial(request):
    template_name = 'base.html'
    links = Link.objects.filter(usuario=request.user)
    try:
        visualizacao = links.first().visualizacao
    except AttributeError:
        visualizacao = 0
    context = {
        'links': links,
        'visualizacao': visualizacao
    }
    return render(request, template_name, context)
