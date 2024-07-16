from django.db import models

# Create your models here.
class employees(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Age=models.IntegerField()
    Address=models.TextField()