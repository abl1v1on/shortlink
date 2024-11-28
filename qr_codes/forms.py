from django import forms

from .models import QRCode


class CreateQRCodeForm(forms.ModelForm):
    class Meta:
        model = QRCode
        fields = ['source_link', 'tags']
        widgets = {
            'source_link': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите исходную ссылку'
                }
            ),
            'tags': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            )
        }
