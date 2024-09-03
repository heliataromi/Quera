from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Person
from .forms import PersonalInformation


@csrf_exempt
def personal_page(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'main.html', context)

    elif request.method == 'POST':
        form = PersonalInformation(request.POST)
        if form.is_valid():
            person = Person()
            person.full_name = form.cleaned_data['full_name']
            person.gender = form.cleaned_data['gender']
            person.height = form.cleaned_data['height']
            person.age = form.cleaned_data['age']
            person.save()
            return HttpResponse(person, status=201)
        return HttpResponse('Error', status=400)
