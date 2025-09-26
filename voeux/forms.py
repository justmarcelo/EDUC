from django import forms
from .models import Voeu

class VoeuForm(forms.ModelForm):
    class Meta:
        model = Voeu
        fields = ['formation']
