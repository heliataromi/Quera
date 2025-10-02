from django.shortcuts import get_object_or_404, render, redirect

from gym.forms import SignUpForm
from gym.models import GymMember

def signup_view(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'gym/signup.html', {'form': form})

    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            birthdate = form.cleaned_data['birthdate']
            start_date = form.cleaned_data['start_date']

            gym_member = GymMember.objects.create(email=email,
                                                  password=password,
                                                  first_name=first_name,
                                                  last_name=last_name,
                                                  birthdate=birthdate,
                                                  start_date=start_date)

            return redirect('success', pk=gym_member.pk)

        return render(request, 'gym/signup.html', {'form': form})



def home_view(request):
    return render(request, 'gym/home.html')


def success_view(request, pk: int):
    member = get_object_or_404(GymMember, pk=pk)
    return render(request, 'gym/success.html', {'member': member})