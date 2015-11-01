# -*- encoding: utf-8 -*-
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
		exclude = ('state', 'date', 'user', 'detail')

	def __init__(self, *args, **kwargs):
		product_extreme = kwargs.pop('product_extreme', None)
		super(ReservationForm, self).__init__(*args, **kwargs)
		if product_extreme:
			self.fields['camp_product'] = forms.ModelChoiceField(label = 'Campo', queryset = Camp_product.objects.filter(product_extreme = product_extreme), empty_label = 'Seleccione un Campo')

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