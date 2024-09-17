from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

#this method creates a user and generates a token after the user is created
    def create(self, validated_data):
        user = get_user_model().objects.create_user( #get_user_model allows us to be flexible and import the custom user model
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        Token.objects.create(user=user)
        return user

#the commented method below creates a user alone
    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         username = validated_data['username'],
    #         email = validated_data['email'],
    #         password = validated_data['password'],
    #         )
    #     return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username = data['username'], password = data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError('invalid credentials')
    

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
