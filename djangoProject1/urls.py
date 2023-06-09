from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('course', views.course, name='course'),
    path('lectures', views.lectures, name='lectures'),
]
