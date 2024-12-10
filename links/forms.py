from django import forms

from .models import Link, Complaint


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


class CreateComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = '__all__'
        widgets = {
            'short_link': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите короткую ссылку'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите описание жалобы'
                }
            )
        }
    
    def clean_short_link(self) -> str:
        short_link = self.cleaned_data['short_link']

        if not Link.objects.filter(short_link=short_link.strip('/')).exists():
            raise forms.ValidationError('Мы не смогли найти такую ссылку')
        return short_link
