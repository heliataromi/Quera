from datetime import datetime

from django import forms
from django.utils import timezone

from gym.models import Course, Enrollment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'coach': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def clean_capacity(self):
        capacity = self.cleaned_data['capacity']

        if capacity < 5:
            raise forms.ValidationError('Capacity should be at least 5.')

        return capacity

    def clean_start_date(self):
        start_date = self.cleaned_data['start_date']

        if start_date < datetime.today().date():
            raise forms.ValidationError('Start date cannot be in the past.')

        return start_date

    def clean(self):
        cleaned_data = super().clean()

        end_date = cleaned_data.get('end_date')
        start_date = cleaned_data.get('start_date')

        if start_date and end_date and end_date <= start_date:
            raise forms.ValidationError('End date must be after start date.')

        return cleaned_data


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        exclude = ('course', 'registered_at')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'national_id': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }

    def __init__(self,  *args, **kwargs):
        self.course = kwargs.pop('course', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        course_enrollments = Enrollment.objects.filter(course=self.course).count()

        if self.course.capacity <= course_enrollments:
            raise forms.ValidationError('This course is already full.')

        return cleaned_data
