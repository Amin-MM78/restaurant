from django import forms
from .models import ReserveTable

class ReserveTableForm (forms.ModelForm):
	class Meta:
		model = ReserveTable
		fields = "__all__"
   