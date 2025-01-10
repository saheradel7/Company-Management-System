from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import UserSerializer

class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
        Handle user registration
        """
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            user_account = serializer.save()
            return Response({"message": "User registered successfully", "user": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
