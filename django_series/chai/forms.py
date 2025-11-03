from django import forms
from .models import chaivarity

class ChaivarityForm(forms.Form):
    chai_varity=forms.ModelChoiceField(queryset=chaivarity.objects.all(),label="select chai variety")