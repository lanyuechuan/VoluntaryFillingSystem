from django.contrib import admin
from .models import User

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["username", "password", "email", "mobile", "college_score", "area", "particular_year", "user_role", "join_datatime", "update_datetime"]

admin.site.register(User, UserInfoAdmin)