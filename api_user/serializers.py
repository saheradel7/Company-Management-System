from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserAccount, UserRole
from rest_framework.authtoken.models import Token


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=UserRole.choices, write_only=True)  

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']  

    def create(self, validated_data):
        role = validated_data.get('role')
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        UserAccount.objects.create(user=user, role=role)
        
        return user



class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']
        
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password =serializers.CharField(write_only =True)

    class Meta:
        model = User
        #fields= ['username', 'email','password']
        exclude = [
            'email',
            "last_login",
            "is_superuser",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions"
        ]
    