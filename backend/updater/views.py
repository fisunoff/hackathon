from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from utils.getfile import update_data

__all__ = [
    'UpdaterView',
]


class UpdaterView(APIView):
    def post(self, request):
        update_data()
        return Response(status=status.HTTP_201_CREATED)
