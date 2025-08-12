from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import CustomUser
from django.core.validators import ValidationError
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=15, write_only=True)
    confirm_password = serializers.CharField(max_length=15, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'age', 'password', 'confirm_password']

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Bu email orqali ro‘yxatdan o‘tilgan!")
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Parollar mos emas!")
        if CustomUser.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Bu username orqali ro‘yxatdan o‘tilgan!")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=120)
    password = serializers.CharField(max_length=120)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise ValidationError({
                'message': 'Login yoki parol kiritilmagan',
                'status': status.HTTP_400_BAD_REQUEST
            })

        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError({
                'message': 'Login yoki parol noto‘g‘ri',
                'status': status.HTTP_401_UNAUTHORIZED
            })

        token, _ = Token.objects.get_or_create(user=user)
        return {
            'user': user,
            'token': token.key
        }    



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','age','email']
        read_only_fields = ['username','email']