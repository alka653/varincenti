from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.forms import ModelForm
from .backends import *
from .forms import *

"""
@premissions_check
def home(request, *args):
	return render(request, 'varincenti/home.html', *args)
"""

def home(request, *args):
	title = 'Bienvenido'
	return render(request, 'varincenti/home.html', {'title': title})

def mark(request):
	title = 'Nuestras Marcas'
	return render(request, 'varincenti/mark.html', {'title': title})

def contact(request):
	title = 'Contactenos'
	if request.method == 'POST':
		form = ContactForm(request.POST)
		form.user = request.user
		if form.is_valid():
			if form.save():
				messages.add_message(request, 25, 'Gracias por contactarse con nosotros')
				return HttpResponseRedirect('/Contactenos')
			else:
				messages.add_message(request, 40, '<strong>Error!</strong> Ha ocurrido un error')
	else:
		form = ContactForm()
	return render(request, 'varincenti/contact.html', {'form': form, 'title': title})