from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.FloatField(default=0.0)


    def __str__(self):
        return f"{self.name}"