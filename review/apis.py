from company.permissions import(AdminPermission, ManagerPermission, EmployeePermission)
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .serializers import ReviewSerializer
from .models import Review, ReviewStatus
from api_user.models import UserAccount
from rest_framework.response import Response

class ReviewAPIView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,AdminPermission]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

class ReviewListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def list(self, request, *args, **kwargs):
        user  = UserAccount.objects.get(user = request.user)
        if user.role == 'admin':
            queryset = Review.objects.all()
        elif user.role == 'employee':
            queryset = Review.objects.filter(user__role = 'employee')
        else:
            queryset = Review.objects.filter(review_status = ReviewStatus.SUBMITTED_FOR_MANAGERIAL)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
