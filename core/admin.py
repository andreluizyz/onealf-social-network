from django.contrib import admin

from .models import *

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio')  
    search_fields = ('usuario__username', 'bio')  
    list_filter = ('usuario__is_staff',)  

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao')  
    search_fields = ('titulo', 'conteudo', 'autor__usuario__username') 
    list_filter = ('data_criacao',)
    ordering = ('-data_criacao',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('conteudo', 'autor', 'data_criacao')  
    search_fields = ('post_titulo', 'conteudo', 'autor__usuario__username') 
    list_filter = ('data_criacao',)
    ordering = ('-data_criacao',)