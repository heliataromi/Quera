from django.urls import path
from bmi.views import bmi_calculator

urlpatterns = [
    path('', bmi_calculator, name='home'),
]
