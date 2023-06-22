from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import LoginForm, UserForm


# view -> função python
def login_usuario(request):
    template_name = 'usuarios/login_usuario.html'
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST) # bound
        if form.is_valid():
            username = form.cleaned_data['username']
            senha = form.cleaned_data['senha']
            user = authenticate(username=username, password=senha)
            if user and user.is_active:
                login(request, user)
                messages.success(request, 'Você fez login')
                return redirect('home:pagina_inicial')
            else:
                messages.error(request, 'Usuário ou senha inválido.')
                return redirect('usuarios:login')
    form = LoginForm()
    context['form'] = form
    return render(request, template_name, context)


def logout_usuario(request):
    logout(request)
    return redirect('usuarios:login')


def add_usuario(request):
    template_name = 'usuarios/add_usuario.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.set_password(user_form.password)
            user_form.save()
            messages.success(request, 'Usuário criado com sucesso.')
            return redirect('usuarios:login')
    form = UserForm()
    context['form'] = form
    return render(request, template_name, context)
