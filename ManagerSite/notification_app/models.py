from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
CustomManager = get_user_model()

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="deleted")[0] 

class Notification(models.Model):
    manager = models.ForeignKey(
            CustomManager,
            on_delete=models.SET(get_sentinel_user),
            related_name='manager_id'
    )
    title = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    limit_of_time = models.DateTimeField()
