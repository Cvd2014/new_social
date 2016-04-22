from django import forms
from .models import Thread, Post


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['name']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['comment']


class ThreadForm(forms.ModelForm):
    name = forms.CharField(label="Thread Name")
    is_a_poll = forms.BooleanField(label="Include a poll?", required=False)
   # num_choices = forms.IntegerField(default=2)

    class Meta:
        model = Thread
        fields = ['name']
