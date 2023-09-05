from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser



@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("nickname", "email", "phone", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "role")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("nickname", "phone", "image")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "role", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "registration_date", "update_time")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "nickname", "email", "password1", "password2",
                "is_staff", "is_active", "role", "groups", "user_permissions"
            )
        }),
    )
    search_fields = ("nickname", "email")
    ordering = ("email",)

