from django.contrib import admin
from api_user.models import UserAccount

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','role']

    def username(self, obj):
        return obj.user.username
    username.short_description = 'Username'
    
    def email(self, obj):
        return obj.user.email
    email.short_description = 'Email'
admin.site.register(UserAccount , UserAccountAdmin)