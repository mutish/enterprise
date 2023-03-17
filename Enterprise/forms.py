from django import forms
from Enterprise.models import Shoes
class ShoesForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = '__all__'
