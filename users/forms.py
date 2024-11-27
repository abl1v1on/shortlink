from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Введите имя пользователя'
        }
    ))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Введите пароль'
        }
    ))


class RegisterUserForm(forms.ModelForm):
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password2']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_password2(self) -> str:
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2
    
    def clean_email(self) -> str:
        email = self.cleaned_data['email']

        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email-ом уже существует')
        return email

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

            field.widget.attrs['placeholder'] = f'Введите {field.label}'.capitalize()
