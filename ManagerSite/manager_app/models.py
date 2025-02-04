from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomManager(AbstractUser):
    """
    管理者モデルと権限の作成
    """
    class Meta:
        permissions = [
            ("notification_list", "notification list"),
            ("notification_detail", "notification detail"),
            ("notification_create", "notification create"),
            ("notification_delete", "notification delete"),
            ("contact_list", "contact list"),
            ("contact_detail", "contact detail"),
            ("contact_delete", "contact delete"),
            ("manager_list", "manager list"),
            ("manager_detail", "manager detail"),
            ("manager_create", "manager create"),
            ("manager_delete", "manager delete"),
            ("user_list", "user list"),
            ("user_detail", "user detail"),
            ("user_delete", "user delete"),
            ("task_list", "task list"),
            ("task_detail", "task detail"),
            ("transaction_detail", "transaction detail"),
        ]
