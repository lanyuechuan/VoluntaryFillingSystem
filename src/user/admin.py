from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "password", "email", "mobile", "college_score", "area", "particular_year", "user_role"]

admin.site.register(User, UserAdmin)