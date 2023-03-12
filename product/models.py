from django.db import models

# Create your models here.

class House(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()
    creation_date = models.DateField(auto_now_add=True)

