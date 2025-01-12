from django.contrib import admin
from .models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'active_review', 'review_date', 'review_feedback', 'review_status']

admin.site.register(Review, ReviewAdmin)