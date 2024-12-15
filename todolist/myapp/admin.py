from .models import Task
from django.contrib import admin

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'status', 'due_date')
    list_filter = ('due_date', 'task_name')
    search_fields = ('task_name', 'description')