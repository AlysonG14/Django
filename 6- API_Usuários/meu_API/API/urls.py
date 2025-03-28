from django.urls import path
from . import views

urlpatterns = [
    path('usuario/', view=views.usuario),
]