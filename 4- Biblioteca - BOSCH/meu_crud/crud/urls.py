from django.urls import path
from .import views

urlpatterns = [
    path('crud/', views.lista_crud, name='lista_crud.html'),
    path('crud/criar/', views.book_create, name='criar.html'),
    path('crud/<int:pk>', views.book_views),
    path('crud/atualizar/<int:pk>', views.book_update, name='atualizar.html'),
    path('crud/deletar/<int:pk>', views.delete_book, name='delete.html'),
    path('crud/busca/', views.search_book, name='busca.html')

]