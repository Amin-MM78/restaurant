from django.db import models

class FoodCategory(models.Model):
    Name=models.CharField(max_length=30)

class Food(models.Model):
   FoodName=models.CharField(max_length=30)
   FCategory=models.ForeignKey(FoodCategory,on_delete=models.PROTECT)
   Description=models.TextField(max_length=300)
   Size=models.CharField(choices=[('1','1'),('2','2'),('3','3')],max_length=2,default='1')
   Price=models.IntegerField()
   ImageFood=models.ImageField()
   PreparationTime=models.SmallIntegerField()
   SpecialFood=models.BooleanField(default=False)
   

class ReserveTable(models.Model):
    name=models.CharField(max_length=30)
    ReserveDateTime=models.DateTimeField()   
    how_many=models.SmallIntegerField(verbose_name='Number of People')
