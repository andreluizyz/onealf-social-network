from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *

class FormUsuario(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email')

    def __init__(self, *args, **kwargs):
        super(FormUsuario, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].help_text = None
    
class FormPerfil(forms.ModelForm):
    
    username = forms.CharField(
        label='Nome de Usuário',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded bg-gray-700 text-white'
        })
    )

    class Meta:
        model = Perfil
        fields = ['foto', 'bio']  

    def __init__(self, *args, **kwargs):
        # Pega o usuário para preencher o campo username inicial
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['username'].initial = self.user.username

    def save(self, commit=True):
        perfil = super().save(commit=False)
        # Atualiza o username do User relacionado
        self.user.username = self.cleaned_data['username']
        if commit:
            self.user.save()
            perfil.save()
        return perfil

class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo', 'imagem']
        labels = {
            'titulo': 'Título',
            'conteudo': 'Conteúdo',
            'imagem': 'Imagem (opcional)',
        }

class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']
        labels = {
            'conteudo': 'Comentário',
        }
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Digite seu comentário...'}),
        }

class FormMensagem(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Digite sua mensagem...'}),
        }