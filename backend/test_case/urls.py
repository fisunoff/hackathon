from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'api', TestCaseView, 'TestCase')
urlpatterns = router.urls
