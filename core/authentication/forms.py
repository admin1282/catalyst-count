from django.contrib.auth.forms import AuthenticationForm,UsernameField,_
from django import forms
from django.contrib.auth.models import User

class login(AuthenticationForm):
      username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'usernamepass','class':'form-control'}))
      password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}),
    )
      

class FileUploadForm(forms.Form):
    file = forms.FileField()


