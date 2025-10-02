import re
from datetime import date
from django import forms

from gym.models import GymMember

class SignUpForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Enter your email'}
        ),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Enter your password'}
        )
    )
    password_confirm = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Confirm your password'}
        )
    )
    first_name = forms.CharField(
        label='First Name',
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Enter your first name'}
        )
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Enter your last name'}
        )
    )
    birthdate = forms.DateField(
        label='Birthdate',
        widget=forms.DateInput(
            attrs={'class': 'form-control'}
        )
    )
    start_date = forms.DateField(
        label='Start Date',
        required=False,
        widget=forms.DateInput(
            attrs={'class': 'form-control'}
        ),
        help_text='When you started working out (leave blank to use today’s date).'
    )

    def clean_email(self):
        email = self.cleaned_data['email']

        if GymMember.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered. Please use a different email.')

        return email

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')

        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError('Password must contain at least one uppercase letter.')

        if not re.search(r'[0-9]', password):
            raise forms.ValidationError('Password must contain at least one number.')

        return password

    def clean_birthdate(self):
        birthdate = self.cleaned_data['birthdate']
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

        if age < 18:
            raise forms.ValidationError('You must be at least 18 years old to register.')

        return birthdate

    def clean_start_date(self):
        start_date = self.cleaned_data['start_date']

        if not start_date:
            return date.today()

        return start_date

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords do not match.')
