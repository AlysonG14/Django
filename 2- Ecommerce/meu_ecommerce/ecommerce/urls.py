from django.urls import path
from .import views

urlpatterns = [
    path('', views.lista_ecommerce, name='lista_ecommerce'),
]