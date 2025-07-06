from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

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

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comentário de {self.autor.usuario.username} em "{self.post.titulo}"'

class Curtida(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='curtidas')
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'perfil')  

    def __str__(self):
        return f'{self.perfil.usuario.username} curtiu "{self.post.titulo}"'

class Mensagem(models.Model):
    remetente = models.ForeignKey(User, related_name='mensagens_enviadas', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='mensagens_recebidas', on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data_envio']

    def __str__(self):
        return f'{self.remetente.username} → {self.destinatario.username}'

