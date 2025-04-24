from django.contrib import admin
from .models import Usuario, UsuarioAuthenticate
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'idade', 'telefone', 'escolaridade', 'animais']
    search_fields = ['nome', 'telefone']
    list_filter = ['escolaridade']


class UsuarioAuthenticateAdmin(UserAdmin):
    list_display = ['username', 'is_active', 'idade', 'nome']

    fieldsets = UserAdmin.fieldsets + (
        ('Campos Novos', {'fields':('nome', 'idade')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Novos', {'fields':('nome', 'idade')}),
    )

    search_fields = ['username', 'nome']
    list_fielter = ['is_active']

admin.site.register(Usuario)
admin.site.register(UsuarioAuthenticate, UsuarioAuthenticateAdmin)




