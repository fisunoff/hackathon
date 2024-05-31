from django.urls import path

from .views import *

urlpatterns = [
    path('', UpdaterView.as_view(), name=''),
]
