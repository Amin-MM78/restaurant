from django.db import models
from django.core import validators

class Food (models.Model):
    FoodName = models.CharField(max_length=30)
    Description = models.CharField(max_length=200)
    Size = models.CharField(max_length=2,choices=[('1','1'),('2','2'),('3','3')],default=1)
    Price = modles.IntegerField()
    #PreparationTime =  DateTimeField()
    Image = models.ImageField()
    SpecialFood =  models.CharField(max_length=3, choices=[('yes','yes'),('No','NO')]
	
class ReserveTable(models.Model):
	Name = models.CharField(max_length=30)
	Number = models.CharField(max_length=1, choices=[('1','1'),('2','2'),('3','3'),('+4','4')])
	Date = models.DateTimeField()
class FoodCategory(models.Model):
	
	FoodGroup = models.CharField(max_length=20)