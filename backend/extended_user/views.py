from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics, status
from rest_framework.authtoken.admin import User
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer


@extend_schema_view(
    create=extend_schema(
        summary='Create a new user',
        responses={
            status.HTTP_200_OK: UserSerializer(many=False),
        }
    )
)
@extend_schema(tags=['Account'])
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
