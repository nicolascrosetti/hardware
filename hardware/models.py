from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=64)

    def __str__(self):
        return self.categoryName

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1200)
    image_url = models.CharField(max_length=1200)
    price = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="listings")

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=64)
    mail = models.CharField(max_length=64)
    message = models.CharField(max_length=2400)

    def __str__(self):
        return "Mensaje de " + self.mail
