from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(PasswordChangeForm):

    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password1']

        # new_password2 = forms.CharField(
        #     label=("New password confirmation"),
        #     strip=False,
        #     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        # )
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
            'new_password1': forms.TextInput(
                    attrs = {
                        'class':'form-control',

                    }
                ),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nama','handphone','image','email','linkedin','twitter','instagram','facebook','description']
        widgets = {
            'nama': forms.TextInput(
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