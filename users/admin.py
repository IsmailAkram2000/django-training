from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserChangeFrom

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeFrom
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'bio']
    fieldsets = UserAdmin.fieldsets + (
        ("User's Bio", {'fields': ('bio',)}),
    )

admin.site.register(User, CustomUserAdmin)