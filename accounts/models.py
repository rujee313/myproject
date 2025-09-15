from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    address=models.TextField()

    def __str__(self):
        return self.name

class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    due_date=models.DateField()
    assigned_to=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
