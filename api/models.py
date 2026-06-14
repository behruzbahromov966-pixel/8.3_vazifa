from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ConstructionCompany(models.Model):
    name = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Building(models.Model):
    company = models.ForeignKey(ConstructionCompany, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    floors = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name

class Comment(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text