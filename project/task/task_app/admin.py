from django.contrib import admin
from .models import User, Employee, Teamleader, Manager

# Register your models here.
admin.site.register(User)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','employeeid','gender','email','mobile','address','salary','performance','doj','empimage','is_active']
    list_filter=['is_active']
admin.site.register(Employee,EmployeeAdmin)

class TeamleaderAdmin(admin.ModelAdmin):
    list_display=['name','employeeid','gender','email','mobile','address','salary','performance','doj','empimage','is_active']
    list_filter=['is_active']
admin.site.register(Teamleader,TeamleaderAdmin)

class ManagerAdmin(admin.ModelAdmin):
    list_display=['name','employeeid','gender','email','mobile','address','salary','performance','doj','empimage','is_active']
    list_filter=['is_active']
admin.site.register(Manager,ManagerAdmin)