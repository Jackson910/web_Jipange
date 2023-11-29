from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, default='To Do')
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)
    completion_percentage = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True, default='uncategorized')
    priority = models.IntegerField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
