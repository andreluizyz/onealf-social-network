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


def home(request):
    posts = Post.objects.all().order_by('-data_criacao')
    return render(request, 'home.html', {'posts': posts})

def sobre(request):
    return render(request, 'sobre.html')

@login_required(login_url='login')
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

@login_required
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id) 

    if request.user != post.autor.usuario: 
        return redirect('home')

    if request.method == 'POST':
        form = FormPost(request.POST, request.FILES, instance=post) 
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FormPost(instance=post)
    return render(request, 'editar_post.html', {'form': form})

@login_required
def ver_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = post.comentarios.all().order_by('-data_criacao')
    perfil = request.user.perfil

    perfil_curtiu = post.curtidas.filter(perfil=perfil).exists()

    if request.method == 'POST':
        form = FormComentario(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post  
            comentario.autor = perfil  
            comentario.save()
            return redirect('ver_post', post_id=post.id) 
    else:
        form = FormComentario()
    
    return render(request, 'ver_post.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form,
        'perfil_curtiu': perfil_curtiu,
    })

@login_required
def curtir_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    perfil = request.user.perfil

    curtida_existente = Curtida.objects.filter(post=post, perfil=perfil).first()

    if curtida_existente:
        curtida_existente.delete()
    else:
        Curtida.objects.create(post=post, perfil=perfil)

    return redirect('ver_post', post_id=post.id)

@login_required
def chat_view(request, username):
    outro_usuario = get_object_or_404(User, username=username)
    mensagens = Mensagem.objects.filter(
        (models.Q(remetente=request.user) & models.Q(destinatario=outro_usuario)) |
        (models.Q(remetente=outro_usuario) & models.Q(destinatario=request.user))
    ).order_by('timestamp')

    if request.method == 'POST':
        conteudo = request.POST.get('mensagem')
        if conteudo:
            Mensagem.objects.create(remetente=request.user, destinatario=outro_usuario, conteudo=conteudo)
            return redirect('chat', username=outro_usuario.username)

    return render(request, 'chat.html', {'mensagens': mensagens, 'outro_usuario': outro_usuario})