from django.contrib import path
from . import views

urlpatterns = [
    path('', views.lista_crud, name='lista_crud')
]