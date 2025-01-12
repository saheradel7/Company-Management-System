from django.db import models

# Create your models here.
class ReviewStatus(models.TextChoices):
    PENDING = 'PENDING'
    CONFIRMED = 'CONFIRMED'
    SCHEDULED = 'SCHEDULED'
    REVIEW_MEETING = 'REVIEW_MEETING'
    SUBMITTED_FOR_MANAGERIAL = 'SUBMITTED_FOR_MANAGERIAL'
    REVIEW_APPROVED = 'REVIEW_APPROVED'
    REVIEW_REJECTED = 'REVIEW_REJECTED'


class Review(models.Model):
    user = models.ForeignKey('api_user.UserAccount', on_delete=models.CASCADE)
    active_review = models.BooleanField(default= True)
    review_date = models.DateTimeField(blank= True, null= True)
    review_feedback = models.TextField(blank= True, null= True)
    review_status = models.CharField(max_length=100 , choices=ReviewStatus.choices, default=ReviewStatus.PENDING)

    def __str__(self):
        return self.user.user.email
    