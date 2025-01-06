from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomManager
from notification_app.models import Notification

# Register your models here.

class CustomManagerAdmin(UserAdmin):
    pass

admin.site.register(CustomManager, CustomManagerAdmin)
admin.site.register(Notification)
