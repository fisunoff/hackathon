from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'account', views.ProfileView, 'ProfileView')
urlpatterns = router.urls

urlpatterns += [
    path('register/', views.UserCreateView.as_view())
]
