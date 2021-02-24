from django import forms
from django.core import validators

class Food (forms.Form):
    FoodName = forms.CharField(max_length=30)
    Description = forms.CharField(max_length=200)
    Size = forms.CharField(max_length=2,choices=[('1','1'),('2','2'),('3','3')],default=1)
    Price = modles.IntegerField()
    #PreparationTime =  DateTimeField()
    Image = forms.ImageField()
    SpecialFood =  forms.CharField(max_length=3, choices=[('yes','yes'),('No','NO')]
	
class ReserveTable(forms.Form):
	Name = forms.CharField(max_length=30)
	Number = forms.CharField(max_length=1, choices=[('1','1'),('2','2'),('3','3'),('+4','4')])
	Date = forms.DateTimeField()
class FoodCategory(forms.Form):
	
	FoodGroup = forms.CharField(max_length=20)