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
		form = ReservationForm(request.POST, instance = user, product_extreme = product.id)
		if form.is_valid():
			form.save()
			messages.add_message(request, 25, 'Exito en la Reserva, estaremos en contácto contigo.')
			return HttpResponseRedirect(reverse('make_reservation', kwargs = {'extreme_id': extreme_id}))
	else:
		form = ReservationForm(product_extreme = product.id, instance = user)
	return render(request, 'extreme/reservation.html', {'title': title, 'product': product, 'form': form})

@login_required(login_url = '/Login')
def reservations(request):
	title = 'Mis Reservas'
	if request.user.is_superuser:
		reservations = Reservation.objects.all().order_by('state')
	else:
		reservations = Reservation.objects.filter(user = request.user).order_by('state')
	return render(request, 'extreme/my-reservation.html', {'title': title, 'reservations': reservations})

@login_required(login_url = '/Login')
def detail_reservation(request, reservation_id):
	title = 'Reserva No.'+reservation_id
	try:
		if request.user.is_superuser:
			reservation = Reservation.objects.get(pk = reservation_id)
		else:
			reservation = Reservation.objects.get(pk = reservation_id, user = request.user)
	except Reservation.DoesNotExist:
		return HttpResponseRedirect('/404')
	return render(request, 'extreme/detail-reservation.html', {'title': title, 'reservation': reservation})

@login_required(login_url = '/Login')
def cancel_reservation(request, reservation_id):
	title = 'Cancelacion de la reserva'
	reservation = Reservation.objects.get(pk = reservation_id)
	if reservation.user == request.user or request.user.is_superuser:
		state_cancel = State.objects.get(pk = 3)
		reservation.state = state_cancel
		reservation.save(update_fields = ['state'])
		messages.add_message(request, 25, 'Exito al cancelar la reserva.')
	else:
		return HttpResponseRedirect('/404')
	return HttpResponseRedirect(reverse('reservations'))