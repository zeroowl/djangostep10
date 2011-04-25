# encoding: utf-8

import re

from django.contrib.auth.models import User
from django import forms

from publicauth.models import PublicID
from annoying.functions import get_object_or_None


class ExtraForm(ExtraForm):
    first_name = forms.CharField(max_length=255,label='Имя')
    last_name = forms.CharField(max_length=255,label='Фамилия')
    email = forms.EmailField(max_length=255,label='E-mail')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r"^[a-zA-Z\d\-_]{3,}$", username):
            raise forms.ValidationError(u"Логин не соответствует маске! Используемое регулярное выражение: r'^[a-zA-Z\d\-_]{3,}$'")
        if get_object_or_None(User, username=username):
            raise forms.ValidationError(u"Данное имя уже занято.")
        return username

    def save(self, request, identity, provider):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        username = self.cleaned_data['username']
        user = User.objects.create(username=username, first_name=first_name, last_name=last_name)
        # most important thing!
        PublicID.objects.create(user=user, identity=identity, provider=provider)
        return user

