# -*- encoding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from varincenti_app.apps.principal.backends import *
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib import messages
from .models import *
from .forms import *
import json

@check_auth
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
				return HttpResponseRedirect(reverse('home_extreme'))
			else:
				messages.add_message(request, 40, 'Usuario inactivo')
		else:
			messages.add_message(request, 30, 'Usuario no existente')
	return render(request, 'users/login.html', {'form': form, 'title': title, 'template': ' ', 'body': 'back'})

def logout_user(request):
	logout(request)
	messages.add_message(request, 25, 'Exito al cerrar sesión')
	return HttpResponseRedirect(reverse('login'))

@csrf_exempt
@check_auth
def register_user(request):
	title = 'Registro'
	if request.method == 'POST':
		form = RegisterForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()
			messages.add_message(request, 25, 'Te has Registrado')
			return HttpResponseRedirect(reverse('register'))
		else:
			messages.add_message(request, 30, 'Ha ocurrido un error')
	else:
		form = RegisterForm()
	return render(request, 'users/register.html', {'form': form, 'title': title, 'template': ' ', 'body': 'back'})

def find_player(request):
	if request.is_ajax:
		word = request.GET.get('term','')
		users = User.objects.filter(username__icontains = word)
		results = []
		for user in users:
			response = {}
			response['label'] = user.username+' - '+user.first_name+' '+user.last_name
			response['value'] = user.username
			results.append(response)
		data_json = json.dumps(results)
	else:
		data_json = 'fail'
	mimetype = "application/json"
	return HttpResponse(data_json, mimetype)