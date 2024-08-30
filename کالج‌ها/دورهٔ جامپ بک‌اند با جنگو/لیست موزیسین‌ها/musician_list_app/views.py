from django.shortcuts import render, HttpResponse
from django.views import View

from .models import Musician, Album


class Musician_list(View):
	def get(self, request):
		musicians = Musician.objects.all().order_by('name').values_list('name', flat=True)
		return HttpResponse(musicians)
