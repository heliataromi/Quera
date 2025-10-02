from django.urls import path

from gym import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('<int:pk>/', views.success_view, name='success'),
]
