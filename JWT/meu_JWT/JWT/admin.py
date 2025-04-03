from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAbs

# Register your models here.

class UserAbsAdmin(UserAdmin):
    list_display = ('username', 'email', 'telefone', 'cargo', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('telefone', 'cargo')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('telefone', 'cargo')}),
    )

admin.site.register(UserAbs, UserAbsAdmin)