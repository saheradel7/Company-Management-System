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


class EmptySerializer(serializers.Serializer):
    pass