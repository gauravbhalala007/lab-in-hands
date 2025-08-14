from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('index',views.index, name = 'home'),
    path('about',views.about, name = 'about'),
    path('doctor',views.doctor, name = 'doctor'),
    path('contact',views.contact, name = 'contact'),
    path('login',views.login, name = 'LOGIN'),   
]