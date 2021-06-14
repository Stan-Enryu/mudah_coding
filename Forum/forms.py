from django import forms

from .models import PostReply, Topic

class CreateTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            'title', 'description'
        ]
        widgets = {
            'title': forms.TextInput(
                    attrs = {
                        'class':'form-control',

                    }
                ),
            'description': forms.TextInput(
                    attrs = {
                        'class':'form-control',

                    }
                ),
        }

class CreatePostReplyForm(forms.ModelForm):
    class Meta:
        model = PostReply
        fields = [
            'description', 'author', 'post'
        ]
        