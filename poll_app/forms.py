from django.forms import ModelForm
from django import forms

from .models import Poll

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'example']