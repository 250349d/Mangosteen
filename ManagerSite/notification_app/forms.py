from django import forms
from .models import Notification

class DateInput(forms.DateInput):
    input_type = 'date'

class NotificationForm(forms.ModelForm):
    """
    Notificationを作成したり修正したりするためのフォーム
    """
    class Meta:
        model = Notification
        fields = ['manager', 'title', 'text', 'limit_of_time']
        widgets = {
            'limit_of_time': DateInput(),
        }
