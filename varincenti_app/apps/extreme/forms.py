# -*- encoding: utf-8 -*-
from varincenti_app.apps.users.models import ProfileUser
from django.contrib.auth.models import User
from datetime import timedelta, time
from django.forms import *
from django import forms
from .models import *

class CustomDateInput(widgets.TextInput):
	input_type = 'date'

class ReservationForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = '__all__'
		widgets = {
			'date_reservation': TextInput,
			'hour_reservation': TimeInput,
		}
		labels = {
			'camp_product': 'Campo',
			'date_reservation': 'Fecha de la Reserva',
			'hour_reservation': 'Hora de la Reserva',
		}
		exclude = ('state', 'date', 'user')

	def __init__(self, *args, **kwargs):
		product_extreme = kwargs.pop('product_extreme', None)
		super(ReservationForm, self).__init__(*args, **kwargs)
		if product_extreme:
			self.fields['camp_product'] = forms.ModelChoiceField(label = 'Campo', queryset = Camp_product.objects.filter(product_extreme = product_extreme), empty_label = 'Seleccione un Campo')

	def save(self):
		user = User.objects.get(username = self.instance)
		print(user)
		date_reservation = self.cleaned_data.get('date_reservation')
		hour_reservation = self.cleaned_data.get('hour_reservation')
		camp_product = self.cleaned_data.get('camp_product')
		reservation = Reservation(user = user, date_reservation = date_reservation, hour_reservation = hour_reservation, camp_product = camp_product)
		reservation.save()
		reservation_player = Reservation_player(reservation = reservation, player_user = user)
		reservation_player.save()
		return reservation
	"""
	def clean_camp_product(self):
		camp_product = self.cleaned_data.get('camp_product')
		date_reservation = datetime.strptime(str(self.cleaned_data.get('date_reservation')), '%Y-%m-%d')
		hour_reservation = datetime.strptime(str(self.cleaned_data.get('hour_reservation')), '%H:%M:%S')
		hour_reservation_2 = hour_reservation + timedelta(minutes = 59)
		hour_reservation = hour_reservation - timedelta(minutes = 59)
		print(camp_product)
		if Reservation.objects.filter(date_reservation = date_reservation, hour_reservation__range = [hour_reservation, hour_reservation_2], camp_product = camp_product).exists():
			raise forms.ValidationError('Campo '+str(camp_product)+' ocupado. Escoge otra fecha y/o campo')
		return camp_product
	"""

class ReservationPlayerForm(forms.ModelForm):
	class Meta:
		model = Reservation_player
		fields = '__all__'
		widgets = {
			'player_user': TextInput(attrs = {'required': True, 'placeholder': 'Escribe el nombre de usuario del jugador'}),
		}
		exclude = ('reservation',)

	def clean_player_user(self):
		reservation = Reservation.objects.get(pk = str(self.instance))
		player_user = self.cleaned_data.get('player_user')
		user = User.objects.get(username = player_user)
		if user.profileuser.state.id == 7:
			raise forms.ValidationError('El usuario '+user.username+' se encuentra en estado '+str(user.profileuser.state))
		else:
			if Reservation_player.objects.filter(reservation = reservation, player_user = user).exists():
				raise forms.ValidationError('El usuario '+user.username+' ya se encuentra agregado.')
		return player_user