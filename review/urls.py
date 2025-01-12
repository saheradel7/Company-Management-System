from django.urls import path
from .apis import ReviewAPIView,ReviewListAPIView,ChangeReviewStatusAPIView
urlpatterns = [
    path('create/', ReviewAPIView.as_view(), name='create-review'),
    path('list/', ReviewListAPIView.as_view(), name='list-review'),
    path('change-status/<int:pk>/', ChangeReviewStatusAPIView.as_view(), name='change-review-status'),
]