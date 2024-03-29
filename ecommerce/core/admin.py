from django.contrib import admin
from core.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.utils.translation import gettext_lazy as _


# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["uid", "id", "phone_number", "email", "full_name"]
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        (_("Personal Info"), {"fields": ("full_name",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "password1",
                    "password2",
                    "full_name",
                    "image",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    readonly_fields = ["uid", "last_login"]

    list_filter = ["is_active", "is_staff", "is_superuser"]

    search_fields = ["phone_number", "full_name"]


admin.site.register(User, UserAdmin)


