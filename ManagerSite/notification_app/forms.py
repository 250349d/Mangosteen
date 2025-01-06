from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    """
    Notificationを作成したり修正したりするためのフォーム
    """
    class Meta:
        model = Notification
        fields = ['manager', 'title', 'text', 'limit_of_time']
