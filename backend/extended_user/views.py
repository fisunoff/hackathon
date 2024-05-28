import json

from django.http import HttpResponse
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics, status, permissions
from rest_framework.authtoken.admin import User
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import UserSerializer, ProfileSerializer


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
    permission_classes = (AllowAny,)


@extend_schema(tags=['Account'])
@extend_schema_view(get=extend_schema(
    summary='Данные текущего залогиненного пользователя',
    responses={
        status.HTTP_200_OK: ProfileSerializer(many=False),
        status.HTTP_404_NOT_FOUND: None,
    }
),
    post=extend_schema(
        summary='Поменять данные текущего залогиненного пользователя',
        responses={
            status.HTTP_200_OK: ProfileSerializer(many=False),
            status.HTTP_404_NOT_FOUND: None,
        }
    )
)
class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self, request):
        return get_object_or_404(Profile, user=self.request.user)

    def get(self, request, *args, **kwargs):
        instance = self.get_object(request)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        instance = self.get_object(request)
        serializer = self.serializer_class(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
