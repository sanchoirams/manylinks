from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import LinkForm
from .models import Link


@login_required
def add_link(request):
    template_name = 'links/add_link.html'
    context = {}
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            link_form = form.save(commit=False)
            link_form.usuario = request.user
            link_form.save()
            messages.success(request, 'Link criado com sucesso')
            return redirect('links:lista')
    form = LinkForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def lista_links(request):
    template_name = 'links/lista_links.html'
    links = Link.objects.filter(usuario=request.user) # select * from links where usuario = admin
    context = {
        'links': links
    }
    return render(request, template_name, context)


@login_required
def editar_link(request, id_link):
    template_name = 'links/add_link.html'
    context = {}
    link = get_object_or_404(Link, pk=id_link, usuario=request.user)
    if request.method == 'POST':
        form = LinkForm(data=request.POST, instance=link)
        if form.is_valid():
            form.save()
            messages.success(request, 'Link alterado com sucesso')
            return redirect('links:lista')
    form = LinkForm(instance=link)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def apagar_link(request, id_link):
    link = Link.objects.get(id=id_link) # delete from links where id = id_link
    link.delete()
    return redirect('links:lista')


def perfil(request, username):
    template_name = 'links/perfil.html'
    links = Link.objects.filter(usuario__username=username)
    for link in links:
        link.visualizacao += 1
        link.save()
    context = {
        'links': links
    }
    return render(request, template_name, context)


def clique_link(request, id_link):
    link = get_object_or_404(Link, pk=id_link)
    link.clique += 1
    link.save()
    return HttpResponseRedirect(link.url)
