from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User







class NewUser(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length =200)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

        def save(self, commit=True):
            user = super(NewUser, self).save(commit=False)
            user.email = save.clean_data['email']
            if commit:
                user.save
            return user
            