from django.contrib import admin
from .models import Food, FoodCategory , ReserveTable , About , ContactForm
# Register your models here.
admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(ReserveTable)
admin.site.register(About)
admin.site.register(ContactForm)
