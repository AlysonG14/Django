from django.contrib import admin
from .models import DonoDoPato, Pato
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class DonoDoPatoAdmin(UserAdmin): 
    list_display = ['username', 'is_active', 'foto_de_perfil']

    fieldsets = UserAdmin.fieldsets + (
        ('Campos Novos', {'fields':('nome', 'foto_de_perfil', 'bio')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Novos', {'fields':('nome', 'foto_de_perfil', 'bio')}),
    )



admin.site.register(Pato)
admin.site.register(DonoDoPato, DonoDoPatoAdmin)