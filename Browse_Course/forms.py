from django import forms
from codemirror import CodeMirrorTextarea

from .models import Sub_Step_Course, Review

class form_code(forms.ModelForm):
    class Meta:
        model = Sub_Step_Course
        fields = ['code']
        widgets = {
            'code': CodeMirrorTextarea(
                    mode="C", 
                    theme="abbott", 
                    config={"fixedGutter": True,}, 
                    attrs={'style': 'width:600px; height:500px'}
                ),
        }
