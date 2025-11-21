from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    roast_level = models.CharField(max_length=100)
    process_method = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.country})"

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    method = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField(blank=True)
    instructions = models.TextField()
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, related_name='recipes')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"