# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
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
	if request.method == 'POST':
		form = ReservationForm(request.POST, instance = request.user, product_extreme = product.id)
		if form.is_valid():
			save_form = form.save()
			messages.add_message(request, 25, 'Reserva Exitosa, continua ingresando los jugadores.')
			return HttpResponseRedirect(reverse('make_reservation_player', kwargs = {'reservation_id': save_form.id}))
	else:
		form = ReservationForm(product_extreme = product.id, instance = request.user)
	return render(request, 'extreme/reservation.html', {'title': title, 'product': product, 'form': form})

@login_required(login_url = '/Login')
def make_reservation_player(request, reservation_id):
	title = 'Agrega a tu equipo'
	players = Reservation_player.objects.filter(reservation = reservation_id)
	reservation_data = Reservation.objects.get(pk = reservation_id)
	reservation = Reservation_player(reservation = reservation_data)
	if request.method == 'POST':
		user = User.objects.get(username = request.POST['player_user'])
		request.POST = request.POST.copy()
		request.POST['player_user'] = user.pk
		form = ReservationPlayerForm(request.POST, instance = reservation)
		if form.is_valid():
			form.save()
			messages.add_message(request, 25, 'Usuario agregado exitosamente.')
			return HttpResponseRedirect(reverse('make_reservation_player', kwargs = {'reservation_id': reservation_id}))
		else:
			request.POST['player_user'] = user.username
			messages.add_message(request, 40, 'Ha ocurrido un error.')
		print(request.POST['player_user'])
	else:
		form = ReservationPlayerForm(instance = reservation)
	return render(request, 'extreme/reservation_player.html', {'title': title, 'players': players, 'form': form, 'reservation': reservation_data})

@login_required(login_url = '/Login')
def delete_reservation_player(request, reservation_player_id):
	reservation_player = Reservation_player.objects.get(pk = reservation_player_id)
	reservation_id = reservation_player.reservation
	user = reservation_player.reservation.user
	if user == request.user or request.user.is_superuser:
		reservation_player.delete()
		messages.add_message(request, 25, 'Jugador eliminado exitosamente.')
		return HttpResponseRedirect(reverse('make_reservation_player', kwargs = {'reservation_id': reservation_id}))
	else:
		return HttpResponseRedirect('/404')

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
	reservation = Reservation.objects.get(pk = reservation_id)
	if reservation.user == request.user or request.user.is_superuser:
		state_cancel = State.objects.get(pk = 3)
		reservation.state = state_cancel
		reservation.save(update_fields = ['state'])
		messages.add_message(request, 25, 'Exito al cancelar la reserva.')
	else:
		return HttpResponseRedirect('/404')
	return HttpResponseRedirect(reverse('reservations'))