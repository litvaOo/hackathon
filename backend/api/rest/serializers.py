from accounts.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password1 = serializers.CharField(max_length=30)
    password2 = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)
    country = serializers.CharField(max_length=30)
    location = serializers.CharField(max_length=30)
    avatar = serializers.FileField(required=False)

    def save(self, request, **kwargs):
        return User.objects.create_user(
            email=self.data['email'],
            password=self.data['password1'],
            first_name=self.data['first_name'],
            last_name=self.data['last_name'],
            city=self.data['city'],
            country=self.data['country'],
            avatar=self.data['avatar']
        )
