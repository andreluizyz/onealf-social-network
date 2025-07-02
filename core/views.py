from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import *
from .models import *

def register(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = FormUsuario()
    return render(request, 'register.html', {'form': form})

@login_required(login_url='login')
def home(request):
    posts = Post.objects.all().order_by('-data_criacao')
    return render(request, 'home.html', {'posts': posts})

@login_required
def perfil(request, username):
    user = get_object_or_404(User, username=username)
    perfil = get_object_or_404(Perfil, usuario=user)
    return render(request, 'perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request, username):
    user = get_object_or_404(User, username=username)

    if request.user.username != username:
        return redirect('perfil', username=request.user.username)

    perfil = get_object_or_404(Perfil, usuario=user)

    if request.method == 'POST':
        form = FormPerfil(request.POST, request.FILES, instance=perfil, user=user)
        if form.is_valid():
            form.save()
            return redirect('perfil',  username=form.cleaned_data['username'])
    else:
        form = FormPerfil(instance=perfil, user=user)

    return render(request, 'editar_perfil.html', {'form': form})

@login_required
def criar_post(request):
    perfil = request.user.perfil

    if request.method == 'POST':
        form = FormPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = perfil
            post.save()
            return redirect('home')
    else:
        form = FormPost()

        return render(request, 'criar_post.html', {'form': form})