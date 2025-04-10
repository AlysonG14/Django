from django.urls import path
from . import views

urlpatterns = [
    path('crud/', views.lista_crud, name='lista_crud'), 
    path('crud/criar/', views.book_create, name='criar'),  
    path('crud/<int:pk>', views.book_views, name='book_views'),  
    path('crud/atualizar/<int:pk>', views.book_update, name='atualizar'),  
    path('crud/deletar/<int:pk>', views.delete_book, name='delete'), 
    path('crud/busca/', views.search_book, name='busca'), 

]
