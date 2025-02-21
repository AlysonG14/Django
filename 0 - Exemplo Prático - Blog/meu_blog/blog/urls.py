from django.urls import path
from .import views

urlpatterns = [
 path('', views.lista_postagens, name='lista_postagens'),
 
] 

