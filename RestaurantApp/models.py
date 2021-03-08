from django.db import models
from django.contrib.auth.models import User
class FoodCategory(models.Model):
    name=models.CharField(max_length=30)

class Food(models.Model):
   food_name = models.CharField(max_length=30)
   FCategory = models.ForeignKey(FoodCategory,on_delete=models.PROTECT)
   description = models.TextField(max_length=300)
   size = models.CharField(choices=[('1','1'),('2','2'),('3','3')],max_length=2,default='1')
   price = models.IntegerField()
   image_food = models.ImageField()
   preparation_time = models.SmallIntegerField()
   special_food = models.BooleanField(default=False)
   author = models.ForeignKey(User, on_delete=models.CASCADE)

   def __str__(self):
      return self.food_name

class ReserveTable(models.Model):
    name = models.CharField(max_length=30)
    ReserveDateTime = models.TextField(max_length=20)   
    how_many = models.SmallIntegerField(verbose_name='Number of People')

class About(models.Model):
  title = models.CharField(max_length=10)
  description = models.TextField(max_length=300)
  image = models.ImageField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
      return self.title

class ContactForm(models.Model):
  name = models.CharField(max_length=10)
  email = models.EmailField(max_length=30 , verbose_name='write your email here')
  subject = models.CharField(max_length=20)
  message = models.TextField(max_length=300)

class Gallery(models.Model):
  image_food = models.ImageField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)