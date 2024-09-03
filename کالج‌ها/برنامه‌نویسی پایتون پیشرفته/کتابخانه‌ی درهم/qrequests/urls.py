from django.contrib import admin
from django.urls import path
from qrequest.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('math/', showmathbooks, name='showmathbooks'),
    path('physic/', showphysicsbooks, name='showphysicsbooks'),
    path('chess/', showchessbooks, name='showchessbooks'),
    path('chess1/',showchess1books, name='showchess1books')
]
