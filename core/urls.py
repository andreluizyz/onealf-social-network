from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('perfil/<str:username>', views.perfil, name='perfil'),
    path('editar_perfil/<str:username>', views.editar_perfil, name='editar_perfil'),
    path('criar_post/', views.criar_post, name='criar_post'),

]
