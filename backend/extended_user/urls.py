from django.urls import path
from rest_framework import routers

from . import views

urlpatterns = []

urlpatterns += [
    path('register/', views.UserCreateView.as_view()),
    path('account/', views.ProfileView.as_view())
]