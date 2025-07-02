from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Nome de usuário: {self.usuario.username}'

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='postagens/', blank=True, null=True)
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Data de criação: {self.data_criacao}'

# class Comentario(models.Model):

# class Curtida(models.Model):

