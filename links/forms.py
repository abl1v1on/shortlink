from django import forms

from .models import Link


class CreateLinkForm(forms.ModelForm):
    class Meta:
        model = Link
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
                    'class': 'form-control choices'
                }
            )
        }
