# -*- encoding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.conf import settings
from django.forms import *
from django import forms
from .models import *

class LoginForm(forms.Form):
	username = forms.CharField(label = 'Usuario', widget = forms.TextInput(attrs = {'class': 'form', 'placeholder': 'Ingresa tu usuario', 'autocomplete': 'off'}))
	password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form', 'placeholder': 'Ingresa tu Contraseña', 'autocomplete': 'off'}), label = 'Contraseña')

class RegisterForm(forms.Form):
	first_name = forms.CharField(label = 'Nombres', widget = forms.TextInput(attrs = {'class': 'form', 'required': True, 'placeholder': 'Ingrese su nombre'}))
	last_name = forms.CharField(label = 'Apellidos', widget = forms.TextInput(attrs = {'class': 'form', 'required': True, 'placeholder': 'Ingrese sus apellidos'}))
	email = forms.EmailField(label = 'Correo Electrónico', widget = forms.TextInput(attrs = {'class': 'form', 'required': True, 'placeholder': 'Ingrese su correo electrónico', 'type': 'email'}))
	number_telephone = forms.CharField(required = False, max_length = 10, label = 'Número Telefónico', widget = forms.TextInput(attrs = {'class': 'form', 'required': False, 'max_length': '10', 'placeholder': 'Digite su número de contácto telefónico'}))
	number_cellphone = forms.CharField(max_length = 10, label = 'Número Celular', widget = forms.TextInput(attrs = {'class': 'form', 'required': True, 'placeholder': 'Digite su número de contácto celular'}))
	username = forms.CharField(label = 'Usuario', widget = forms.TextInput(attrs = {'class': 'form', 'required': True, 'placeholder': 'Ingrese un usuario'}))
	password = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(attrs = {'class': 'form', 'required': True, 'placeholder': 'Ingrese su contraseña'}))
	birthdate = forms.CharField(label = 'Fecha de Nacimiento', widget = forms.TextInput(attrs = {'class' : 'form'}))
	photo = forms.ImageField(label = 'Foto', required = False)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username = username).exists():
			raise forms.ValidationError('El usuario ya se encuentra en uso.')
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email = email).exists():
			raise forms.ValidationError('El email ya se ecuentra en uso.')
		return email

	def clean_number_telephone(self):
		number_telephone = self.cleaned_data.get('number_telephone')
		if number_telephone:
			if ProfileUser.objects.filter(number_telephone = number_telephone).exists():
				raise forms.ValidationError('El número ya se ecuentra en uso.')
		return number_telephone

	def clean_number_cellphone(self):
		number_cellphone = self.cleaned_data.get('number_cellphone')
		if ProfileUser.objects.filter(number_cellphone = number_cellphone).exists():
			raise forms.ValidationError('El número ya se ecuentra en uso.')
		return number_cellphone

	def save(self):
		first_name = self.cleaned_data.get('first_name')
		last_name = self.cleaned_data.get('last_name')
		email = self.cleaned_data.get('email')
		birthdate = self.cleaned_data.get('birthdate')
		number_telephone = self.cleaned_data.get('number_telephone')
		number_cellphone = self.cleaned_data.get('number_cellphone')
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		photo = self.cleaned_data.get('photo')
		user = User.objects.create_user(username, email, password)
		user.first_name = first_name
		user.last_name = last_name
		user.save()
		profile = ProfileUser(user = user, photo = photo, number_telephone = number_telephone, number_cellphone = number_cellphone, birthdate = birthdate)
		profile.save()
