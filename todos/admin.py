from django.contrib import admin
from .models import Task
# Register your models here.
class Taskadmin(admin.ModelAdmin):
    list_display= ('task','is_completed','updated_at')
    search_fields=('tasks',)
admin.site.register(Task,Taskadmin)