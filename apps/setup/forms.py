from django import forms
from apps.setup.models import PostageRate

class DeliveryServiceForm(forms.Form):
    service = forms.ModelChoiceField(queryset=PostageRate.objects.all(), widget = forms.Select(attrs={'class':'form-control'}))