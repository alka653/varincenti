# -*- encoding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.conf import settings
from django.forms import *
from django import forms
from .models import *

class LoginForm(forms.Form):
	username = forms.CharField(label = 'Usuario')
	password = forms.CharField(widget = forms.PasswordInput, label = 'Contraseña')

class RegisterForm(forms.Form):
	first_name = forms.CharField(label = 'Nombres', widget = forms.TextInput(attrs = {'required': True, 'placeholder': 'Ingrese su nombre'}))
	last_name = forms.CharField(label = 'Apellidos', widget = forms.TextInput(attrs = {'required': True, 'placeholder': 'Ingrese sus apellidos'}))
	email = forms.EmailField(label = 'Correo Electrónico', widget = forms.TextInput(attrs = {'required': True, 'placeholder': 'Ingrese su correo electrónico', 'type': 'email'}))
	number_telephone = forms.CharField(required = False, max_length = 10, label = 'Número Telefónico', widget = forms.TextInput(attrs = {'required': False, 'max_length': '10', 'placeholder': 'Digite su número de contácto telefónico'}))
	number_cellphone = forms.CharField(max_length = 10, label = 'Número Celular', widget = forms.TextInput(attrs = {'required': True, 'placeholder': 'Digite su número de contácto celular'}))
	username = forms.CharField(label = 'Usuario', widget = forms.TextInput(attrs = {'required': True, 'placeholder': 'Ingrese un usuario'}))
	password = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(attrs = {'required': True}))
	photo = forms.ImageField(label = 'Foto', required = False)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username = username).exists():
			raise forms.ValidationError('El usuario '+username+' ya se encuentra en uso, por favor ingrese uno nuevo')
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email = email).exists():
			raise forms.ValidationError('El email '+email+' ya se ecuentra en uso.')
		return email

	def clean_number_telephone(self):
		number_telephone = self.cleaned_data.get('number_telephone')
		if number_telephone:
			if ProfileUser.objects.filter(number_telephone = number_telephone).exists():
				raise forms.ValidationError('El número '+str(number_telephone)+' ya se ecuentra en uso.')
		return number_telephone

	def clean_number_cellphone(self):
		number_cellphone = self.cleaned_data.get('number_cellphone')
		if ProfileUser.objects.filter(number_cellphone = number_cellphone).exists():
			raise forms.ValidationError('El número '+str(number_cellphone)+' ya se ecuentra en uso.')
		return number_cellphone

	def save(self):
		first_name = self.cleaned_data.get('first_name')
		last_name = self.cleaned_data.get('last_name')
		email = self.cleaned_data.get('email')
		number_telephone = self.cleaned_data.get('number_telephone')
		number_cellphone = self.cleaned_data.get('number_cellphone')
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		photo = self.cleaned_data.get('photo')
		user = User.objects.create_user(username, email, password)
		user.first_name = first_name
		user.last_name = last_name
		user.save()
		profile = ProfileUser(user = user, photo = photo, number_telephone = number_telephone, number_cellphone = number_cellphone)
		profile.save()
