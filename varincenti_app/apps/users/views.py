# -*- encoding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .forms import *

def authenticate_user(request):
	title = 'Acceso'
	form = LoginForm()
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/Marcas/ExtremeEntretairment')
			else:
				messages.add_message(request, 40, 'Usuario inactivo')
		else:
			messages.add_message(request, 30, 'Usuario no existente')
	return render(request, 'users/login.html', {'form': form, 'title': title, 'template': 'none'})

def logout_user(request):
	logout(request)
	messages.add_message(request, 25, 'Exito al cerrar sesión')
	return HttpResponseRedirect('/Login')