from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Version
from utils.getfile import update_data

__all__ = [
    'UpdaterView',
]


class UpdaterView(APIView):
    def get(self, request):
        version = Version.get_last_update()  # type: Version
        return Response(
            {
                'created': version.created,
                'status': version.status,
            }
        )

    def post(self, request):
        update_data()
        return Response(status=status.HTTP_200_OK)
