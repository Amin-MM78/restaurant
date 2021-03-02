from django import forms
from . import models

class ReserveTableForm (forms.ModelForm):
	class Meta:
		model = ReserveTable
		fields = "__all__"
   