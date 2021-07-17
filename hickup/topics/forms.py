from django.forms import ModelForm
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from tinymce.widgets import TinyMCE

User = get_user_model()

from .models import Topics, TopicImages

class TopicForm(ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 40, 'row': 10}))
    class Meta:
        model = Topics
        fields = [
            'title',
            'content',
            'private_reply',
            'email_me'
        ]
