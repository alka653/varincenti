# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import render
from .models import *
from .forms import *

def home_extreme(request):
	title = 'Extreme Entretairment'
	body = 'extreme'
	return render(request, 'extreme/home.html', {'title': title})

def product_extreme(request):
	product = Product_extreme.objects.all()
	title = 'Nuestros productos'
	return render(request, 'extreme/product.html', {'title': title, 'products': product, 'row': 0})

@login_required(login_url = '/Login')
def make_reservation(request, extreme_id):
	title = 'Reservaciones'
	product = Product_extreme.objects.get(pk = extreme_id)
	user = Reservation(user = request.user)
	if request.method == 'POST':
		form = ReservationForm(request.POST, instance = user)
		if form.is_valid():
			if form.save():
				messages.add_message(request, 25, 'Exito en la Reserva, estaremos en contácto contigo.')
				return HttpResponseRedirect(reverse('make_reservation', kwargs = {'extreme_id': extreme_id}))
			else:
				messages.add_message(request, 40, '<strong>Error!</strong> Ha ocurrido un error')
	else:
		form = ReservationForm(product_extreme = product.id, instance = user)
	return render(request, 'extreme/reservation.html', {'title': title, 'product': product, 'form': form})