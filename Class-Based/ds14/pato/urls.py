from django.urls import path
from . views import PatoListCreateAPIView

urlpatterns = [
    path("patos/", PatoListCreateAPIView.as_view(), name='pato-list-create'),
]