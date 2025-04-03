from django.urls import path
from . import views

urlpatterns = [
    path('criarUsuario/', view=views.create_user, name='create_user'),
    path('logar/', view=views.logar, name='logar'),
    path('fazAlgumaCoisa/', view=views.view_protegida, name='view_protegida')


]