from django.urls import path

from courses import views


app_name = 'courses'

urlpatterns = [
    path('', views.list_view, name='list'),
    path('<int:pk>/', views.detail_view, name='detail'),
]
