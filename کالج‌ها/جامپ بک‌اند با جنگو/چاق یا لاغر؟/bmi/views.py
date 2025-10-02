# demo/views.py
from django.shortcuts import render

from bmi.forms import BMIForm

def bmi_calculator(request):
    result = None

    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            result = form.get_result()
    else:
        form = BMIForm()

    return render(request, 'bmi.html', {'form': form, 'result': result})
