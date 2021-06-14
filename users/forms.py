from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SettingForm(PasswordChangeForm):

    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']

        widgets = {
            'old_password': forms.TextInput(
                    attrs = {
                        'class':'form-control',

                    }
                ),
            'new_password1': forms.PasswordInput(
                    attrs = {
                        'class':'form-control',

                    }
                ),
            'new_password2': forms.TextInput(
                    attrs = {
                        'class':'form-control',

                    }
                ),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','handphone','image','email','linkedin','twitter','instagram','facebook','description']
        widgets = {
            'name': forms.TextInput(
                    attrs = {
                        'class':'form-control',
                    }
                ),
            'handphone': forms.TextInput(
                    attrs = {
                        'class':'form-control',
                    }
                ),
            'email': forms.TextInput(
                    attrs = {
                        'class':'form-control',
                    }
                ),
            'linkedin': forms.TextInput(
                    attrs = {
                        'class':'form-control',
                    }
                ),
            'twitter': forms.TextInput(
                    attrs = {
                        'class':'form-control',
                    }
                ),
            'instagram': forms.TextInput(
                    attrs = {
                        'class':'form-control',
                    }
                ),
            'facebook': forms.TextInput(
                    attrs = {
                        'class':'form-control',
                    }
                ),
        }