from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

def get_sentinel_user():
    return CustomUser.objects.get_or_create(
            first_name = "None",
            last_name = "None",
            birthdate = '0000-00-00',
            post_code = "None",
            address = "None",
            street_address = "None",
            email = "none@example.com",
            telephone_number = "None"
    )[0]

# Contact model
class Contact(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET(get_sentinel_user),
        verbose_name="ユーザーID"
    )
    title = models.CharField(
        max_length=60,
        verbose_name="件名",
        blank=True,
        null=True
    )
    content = models.TextField(
        verbose_name="本文",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        verbose_name="問い合わせ日時",
        auto_now_add=True,
        blank=True,
        null=True
    )
