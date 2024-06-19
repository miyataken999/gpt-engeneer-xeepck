from django import forms
from .models import Ring

class RingForm(forms.ModelForm):
    class Meta:
        model = Ring
        fields = ('material', 'size', 'weight', 'damage', 'scratches')