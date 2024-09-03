from django import forms


class PersonalInformation(forms.Form):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    gender = forms.ChoiceField(choices=GENDERS)
    full_name = forms.CharField(min_length=5, max_length=60)  # 5 <= fullname's length <= 60
    height = forms.IntegerField(min_value=70, max_value=250)     # 70 <= height <= 250
    age = forms.IntegerField(min_value=14, max_value=99)        # 14 <= age <= 99

    # implement full_name validation function here
    # full_name should be a title
    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if not full_name.istitle():
            message = "Full name must me in title form."
            raise forms.ValidationError(message)
        return full_name
