from django.contrib import admin

from administrators.models import Administrator
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'iban', 'administrator')

    def save_model(self, request, obj, form, change):
        administrator = Administrator.objects.get(user=request.user)
        obj.administrator = administrator
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return obj is None or obj.administrator.user == request.user

    def has_delete_permission(self, request, obj=None):
        return obj is None or obj.administrator.user == request.user


admin.site.register(Client, ClientAdmin)