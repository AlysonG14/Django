from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Register your models here.

class UserAbsAdmin(UserAdmin):
    list_display = ('nome', 'telefone', 'endereco', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('telefone', 'endereco')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('telefone', 'endereco')}),
    )

admin.site.register(Usuario, UserAbsAdmin)



