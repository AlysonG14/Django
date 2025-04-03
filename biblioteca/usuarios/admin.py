from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAbs

class UserAbsAdmin(UserAdmin):
    list_display = ('username', 'password', 'email', 'telefone', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefone',)}), 
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'telefone')}),  
    )

admin.site.register(UserAbs, UserAbsAdmin)
