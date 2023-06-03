from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import LinkForm


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
            return redirect('links:add_link')
    form = LinkForm()
    context['form'] = form
    return render(request, template_name, context)
