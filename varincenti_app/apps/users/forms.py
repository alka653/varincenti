# -*- encoding: utf-8 -*-
from django.forms import *
from django import forms
from .models import *

class LoginForm(forms.Form):
	username = forms.CharField(label = 'Usuario')
	password = forms.CharField(widget = forms.PasswordInput, label = 'Contraseña')