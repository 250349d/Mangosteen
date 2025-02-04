from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import CustomUser
from client_app.models import Task, Transaction, Request, Order
from send_contact_app.models import Contact
from chat_app.models import Chat

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("last_name", "first_name", "email", "telephone_number", "birthdate", "post_code", "address", "street_address", "password")}),
        (_("Personal info"), {"fields": ("bank_name", "branch_number", "bank_account_number")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("last_name", "first_name", "email", "telephone_number", "birthdate", "post_code", "address", "street_address", "password1", "password2"),
            },
        ),
    )
    list_display = ("id", "email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("id",)

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Task)
admin.site.register(Transaction)
admin.site.register(Request)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(Chat)
