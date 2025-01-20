from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class SignupForm(UserCreationForm):
    birthdate = forms.DateField(label="生年月日", widget=forms.SelectDateWidget(years=[x for x in range(1900, 2024)]))
    class Meta:
        model = CustomUser 
        fields = ['last_name','first_name', 'email', 'password1', 'password2', 'telephone_number', 'birthdate', 'post_code', 'address', 'street_address'
        ]
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
