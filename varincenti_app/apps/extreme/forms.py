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
		date_reservation = self.cleaned_data.get('date_reservation')
		hour_reservation = self.cleaned_data.get('hour_reservation')
		camp_product = self.cleaned_data.get('camp_product')
		reservation = Reservation(user = user, date_reservation = date_reservation, hour_reservation = hour_reservation, camp_product = camp_product)
		reservation.save()
		reservation_player = Reservation_player(reservation = reservation, player_user = user)
		reservation_player.save()
		return reservation

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

class ProductForm(forms.Form):
	name = forms.CharField(label = 'Nombre del ExtremeEntertainment', widget = forms.TextInput(attrs = {'required': True, 'placeholder': 'Escribe el nombre del ExtremeEntertainment'}))
	tag = forms.CharField(label = 'Tag', widget = forms.TextInput(attrs = {'readonly': True}))
	photo = forms.ImageField(label = 'Foto', required = False)
	description = forms.CharField(label = 'Descripcion', widget = forms.TextInput(attrs = {'required': True, 'placeholder': 'Escribe una descripcion'}))
	conditions = forms.CharField(label = 'Condiciones', widget = forms.Textarea(attrs = {'required': True}))
	camp = forms.ModelMultipleChoiceField(label = 'Campo(s)', queryset = Place_camp.objects.all())

	def save(self):
		name = self.cleaned_data.get('name')
		tag = self.cleaned_data.get('tag')
		photo = self.cleaned_data.get('photo')
		description = self.cleaned_data.get('description')
		conditions = self.cleaned_data.get('conditions')
		camp = self.cleaned_data.get('camp')
		product = Product_extreme(name = name, tag = tag, photo = photo, description = description, conditions = conditions)
		product.save()
		for camps in camp:
			place_camp = Place_camp.objects.get(pk = camps.pk)
			camp_product = Camp_product(product_extreme = product, place_camp = place_camp)
			camp_product.save()
		return product

class CampForm(forms.ModelForm):
	class Meta:
		model = Place_camp
		fields = '__all__'
		widgets = {
			'name': TextInput(attrs = {'required': True, 'placeholder': 'Ingrese el nombre del campo'}),
			'direction': TextInput(attrs = {'required': True, 'placeholder': 'Ingrese la direccion del campo'}),
			'description': TextInput(attrs = {'placeholder': 'Ingrese una descripcion corta del campo'}),
			'ubication': TextInput(attrs = {'required': True, 'placeholder': 'Ingrese la ubicacion del campo'}),
		}
		labels = {
			'name': 'Nombre del Campo',
			'direction': 'Direccion del Campo',
			'description': 'Descripcion',
			'ubication': 'Ubication (Google Maps)',
			'photo': 'Foto'
		}