from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_process', 'In Process'),
        ('done', 'Done'),
    ]

    task_name = models.CharField(max_length=150)
    description = models.TextField()
    due_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')

    def __str__(self):
        return f'{self.task_name}'