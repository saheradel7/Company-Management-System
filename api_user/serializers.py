from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserAccount, UserRole

class UserAccountSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=UserRole.choices)

    class Meta:
        model = UserAccount
        fields = ['user', 'role']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=UserRole.choices)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')
        role = validated_data.pop('role')

        user = User.objects.create_user(**validated_data)

        user_account = UserAccount.objects.create(user=user, role=role)
        
        user.set_password(password)
        user.save()

        return user_account
