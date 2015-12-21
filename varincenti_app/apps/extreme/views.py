# -*- encoding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from varincenti_app.apps.principal.backends import *
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.contrib import messages
from django.shortcuts import render
from django.conf import settings
from requests import request
from .models import *
from .forms import *
import json

def home_extreme(request):
	title = 'Extreme Entretairment'
	body = 'extreme'
	return render(request, 'extreme/home.html', {'title': title})

def product_extreme(request):
	if request.user.is_superuser:
		product = Product_extreme.objects.all()
	else:
		product = Product_extreme.objects.filter(state = 9)
	title = 'Nuestros productos'
	return render(request, 'extreme/product.html', {'title': title, 'products': product, 'row': 0})

@login_required(login_url = '/Login')
def invite(request):
	friends = get_friends(request.user)
	return render(request, 'extreme/invite.html', {'friends': friends, 'SOCIAL_AUTH_FACEBOOK_KEY': settings.SOCIAL_AUTH_FACEBOOK_KEY})

def get_friends(user):
	facebook = user.social_auth.get(provider='facebook')
	url = 'https://graph.facebook.com/v2.5/me/taggable_friends?'.format(facebook.uid)
	friends = request('GET', url, params={'access_token': facebook.extra_data['access_token']}).json()
	print(friends)
	return friends['data']

@login_required(login_url = '/Login')
def make_reservation(request, extreme_id):
	title = 'Reservaciones'
	product = Product_extreme.objects.get(pk = extreme_id)
	if request.method == 'POST':
		if request.user.profileuser.state.id != 7:
			form = ReservationForm(request.POST, instance = request.user, product_extreme = product.id)
			if form.is_valid():
				save_form = form.save()
				messages.add_message(request, 25, 'Reserva Exitosa, continua ingresando los jugadores.')
				return HttpResponseRedirect(reverse('make_reservation_player', kwargs = {'reservation_id': save_form.id}))
		else:
			form = ReservationForm(product_extreme = product.id, instance = request.user)
			messages.add_message(request, 40, 'No puedes realizar la reserva, tienes multa.')
			return render(request, 'extreme/reservation.html', {'title': title, 'product': product, 'form': form})
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
		state_cancel = State.objects.get(pk = 4)
		reservation.state = state_cancel
		date_now = datetime.now().strftime('%Y-%m-%d')
		date_reser = reservation.date_reservation - timedelta(days = 3)
		print(date_now)
		if str(date_now) >= str(date_reser):
			messages.add_message(request, 40, 'Ya no puedes cancelar la reserva.')
		else:
			reservation.save(update_fields = ['state'])
			messages.add_message(request, 25, 'Exito al cancelar la reserva.')
	else:
		return HttpResponseRedirect('/404')
	return HttpResponseRedirect(reverse('reservations'))

@csrf_exempt
def search_camp(request):
	response = {}
	if request.method == 'POST':
		camp_product = Camp_product.objects.get(pk = request.POST.get('id'))
		response['ubication'] = str(camp_product.place_camp.ubication)
		response['photo'] = str(camp_product.place_camp.photo)
		response['name'] = str(camp_product.place_camp.name)
	else:
		response['error'] = 'Ha ocurrido un error'
	return HttpResponse(json.dumps(response), content_type = 'application/json')

@premissions_check
def delete_reservation(request, reservation_id):
	reservation = Reservation.objects.get(pk = reservation_id)
	reservation.delete()
	messages.add_message(request, 25, 'Reserva eliminada exitosamente.')
	return HttpResponseRedirect(reverse('reservations'))

@premissions_check
def new_extreme(request):
	title = 'Agregar nuevo extreme'
	if request.method == 'POST':
		response = {}
		form = ProductForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			extreme = form.save()
			response['name'] = extreme.name
			response['description'] = extreme.description
			response['pk'] = extreme.pk
			response['state'] = extreme.state.name
			response['class_tag'] = extreme.state.class_tag
			response['photo'] = str(extreme.photo)
		else:
			response['response'] = "Error al guardar"
		return HttpResponse(json.dumps(response), content_type = 'application/json')
	else:
		form = ProductForm()
	return render(request, 'extreme/new-extreme.html', {'title': title, 'form': form})

@premissions_check
def edit_extreme(request, product_id):
	pass

@csrf_exempt
def new_camp(request):
	title = 'Agregar Campo'
	if request.method == 'POST':
		response = {}
		form = CampForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()
			response['response'] = "Exito al guardar"
		else:
			response['response'] = "Error al guardar"
		return HttpResponse(json.dumps(response), content_type = 'application/json')
	else:
		form = CampForm()
		return render(request, 'extreme/new-camp.html', {'title': title, 'form': form})