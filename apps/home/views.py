from django.shortcuts import render

# Create your views here.


def pagina_inicial(request):
    template_name = 'base.html'
    return render(request, template_name, {})
