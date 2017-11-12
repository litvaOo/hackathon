from accounts.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)
    password2 = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255, required=False)
    country = serializers.CharField(max_length=255, required=False)
    location = serializers.CharField(max_length=255, required=False)
    avatar = serializers.FileField(required=False)

    def validate_email(self, data):
        if User.objects.filter(email=data).exists():
            raise serializers.ValidationError(
                "User with email {} exists".format(data))
        return data

    def validate_password(self, data):
        if len(data) < 6:
            raise serializers.ValidationError(
                "Password length must be large then 6 chars")
        if self.initial_data.get('password2') != data:
            raise serializers.ValidationError(
                "Passwords didn't match")
        return data

    def save(self, request, **kwargs):
        return User.objects.create_user(
            email=self.data.get('email'),
            password=self.data.get('password'),
            first_name=self.data.get('first_name'),
            last_name=self.data.get('last_name'),
            city=self.data.get('city'),
            country=self.data.get('country'),
            avatar=self.data.get('avatar')
        )
