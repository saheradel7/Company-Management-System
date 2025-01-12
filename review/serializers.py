from rest_framework import serializers
from .models import Review
from api_user.models import UserAccount

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        write_only_fields= [
            'active_review',
            'review_date',
            'review_feedback',
            'review_status',
        ]

    def validate_user(self, value):
        if value is None:
            raise serializers.ValidationError("User Account is required")
     
        if value.role != 'employee':
            raise serializers.ValidationError("You can only create review request for an employee")
        return value