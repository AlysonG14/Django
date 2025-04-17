from django.contrib import admin
from .models import Usuario, UsuarioAuthenticate
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UsuarioAuthenticateAdmin(UserAdmin):
    list_display = ['username', 'is_active', 'idade']

    fieldsets = UserAdmin.fieldsets + (
        ('Campos Novos', {'fields':('nome', 'idade')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Novos', {'fields':('nome', 'idade')}),
    )

admin.site.register(Usuario)
admin.site.register(UsuarioAuthenticate, UsuarioAuthenticateAdmin)




