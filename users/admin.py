from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ["id", "nickname", "email", "is_active", "is_staff", "is_superuser"]
    list_display_links = ["id", "nickname", "email"]
    search_fields = ["nickname", "email"]
    readonly_fields = ["id", "is_staff", "is_superuser"]

    fieldsets = (
        ("User Info", {"fields": ("id", "nickname", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    add_fieldsets = (
        (
            "Required User Info",
            {
                "classes": ("wide",),
                "fields": ("nickname", "email", "password1", "password2"),
            },
        ),
    )

    ordering = ("id",)
