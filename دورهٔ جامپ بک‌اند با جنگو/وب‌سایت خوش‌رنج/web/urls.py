from django.urls import path

from .views import *

urlpatterns = [
	path('sad/<str:name>/', sad),
	path('happy/<str:name>/<int:times>/', happy)
]
