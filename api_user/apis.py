from .serializers import UserRegisterSerializer ,EmptySerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import TokenAuthentication,get_authorization_header

from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class LoginView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'username': user.username,
            'email': user.email,
            'token': token.key,
        }, status=status.HTTP_200_OK)

class Logout(generics.GenericAPIView):
    queryset = Token.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = EmptySerializer

    def post(self, request, *args, **kwargs):
        auth_header = get_authorization_header(request).decode('utf-8')
        if not auth_header.startswith('Token '):
            return Response({'error': 'Invalid token header'}, status=status.HTTP_400_BAD_REQUEST)
        token_key = auth_header.split('Token ')[1]
        try:
            token = Token.objects.get(key=token_key)
            token.delete()
            return Response({'success': 'Logged out successfully'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)
