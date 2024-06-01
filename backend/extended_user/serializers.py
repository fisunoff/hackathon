from rest_framework import serializers
from rest_framework.authtoken.admin import User

from extended_user.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True, 'required': True}, 'email': {'required': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        email = validated_data.pop('email')
        user = User(**validated_data)
        user.set_password(password)
        user.email = email
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    # is_manager = serializers.BooleanField(read_only=True)

    class Meta:
        model = Profile
        fields = ('name', 'surname', 'patronymic', 'bio', 'post', 'manager', 'notify_me')
