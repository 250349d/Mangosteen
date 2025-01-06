from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

CustomManager = get_user_model()

class ManagerCreationForm(UserCreationForm):
    class Meta:
        model = CustomManager
        fields = ['username', 'email', 'last_name', 'first_name', 'is_staff', 'is_active']

class ManagerChangeForm(forms.ModelForm):
    class Meta:
        model = CustomManager
        fields = ['username', 'email', 'last_name', 'first_name', 'is_staff', 'is_active']
