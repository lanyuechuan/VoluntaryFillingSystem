from django.contrib import admin
from .models import UserInfo

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["username", "password", "email", "mobile", "college_score", "area", "particular_year", "user_role"]

admin.site.register(UserInfo, UserInfoAdmin)