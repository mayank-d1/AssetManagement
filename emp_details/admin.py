from django.contrib import admin
from .models import Employee, Device


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name', 'email_id')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Device)

