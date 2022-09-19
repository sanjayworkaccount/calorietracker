from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField(null=None)
    protein = models.FloatField(null=None)
    fats = models.FloatField(null=None)
    calories = models.IntegerField(null=None)

    def __str__(self):
        return self.name

class selected_item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
