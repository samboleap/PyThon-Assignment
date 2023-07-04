from django.urls import path
from . import views

urlpatterns = [
    path('contact-us/', views.members, name='members'),
]