from django import forms

class BMIForm(forms.Form):
    height = forms.FloatField(
        label="Height (cm)",
        min_value=1,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Enter height in centimeters'}
        )
    )
    weight = forms.FloatField(
        label="Weight (kg)",
        min_value=1,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Enter weight in kilograms'}
        )
    )
    age = forms.IntegerField(
        label="Age",
        min_value=20,
        max_value=120,
        widget=forms.NumberInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Enter your age'}
        )
    )
    gender = forms.ChoiceField(
        label="Gender",
        choices=[('M', 'Male'),
                 ('F', 'Female')],
        widget=forms.Select(
            attrs={'class': 'form-select',}
        )
    )

    def calculate_bmi(self, height_m, weight):
        return round(weight / (height_m ** 2), 2)

    def calculate_fat(self, bmi, age, gender):
        return round((1.20 * bmi) + (0.23 * age) - (10.8 * int(gender == 'M')) - 5.4, 1)

    def get_result(self) -> dict:
        height_m = self.cleaned_data['height'] / 100
        weight = self.cleaned_data['weight']
        age = self.cleaned_data['age']
        gender = self.cleaned_data['gender']

        bmi = self.calculate_bmi(height_m, weight)
        fat = self.calculate_fat(bmi, age, gender)

        if bmi < 18.5:
            category = 'Underweight'
        elif 18.5 <= bmi < 25:
            category = 'Healthy weight'
        elif 25 <= bmi < 30:
            category = 'Overweight'
        else:
            category = 'Obese'

        result = {
            'bmi': bmi,
            'body_fat': fat,
            'category': category
        }

        return result
