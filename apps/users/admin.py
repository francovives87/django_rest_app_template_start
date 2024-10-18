from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Campos que se mostrarán en el formulario de edición
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('custom_field1', 'custom_field2')}),  # Reemplaza con tus propios campos personalizados
    )

    # Campos que serán de solo lectura
    readonly_fields = ('date_joined',)

    # Excluir 'username' si tu modelo no tiene este campo
    exclude = ('username',)

    # Ajusta el ordenamiento si el campo 'username' no existe en tu modelo
    ordering = ('email',)  # Suponiendo que 'email' es un campo en tu modelo

    # Lista de campos que se mostrarán en la lista de objetos del admin
    list_display = ('email', 'first_name', 'last_name')  # Reemplaza con los campos de tu modelo

admin.site.register(CustomUser, CustomUserAdmin)
