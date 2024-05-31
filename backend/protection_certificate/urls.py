from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'api', ProtectionToolCertificateViewSet)
router.register(r'diff', ProtectionToolCertificateDiffViewSet)
urlpatterns = router.urls
urlpatterns += [
    path('recalc_functions/', RecalcFunctionsView.as_view(), name='recalc-functions'),
]
