from django.shortcuts import render
from .models import Ecommerce

# Create your views here.

def lista_ecommerce(request):
    meuecommerce = Ecommerce.objects.all().order_by('-data_criacao')
    return render(request, 'ecommerce/lista_ecommerce.html', {'meuecommerce': meuecommerce})


