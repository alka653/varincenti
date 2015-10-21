# -*- encoding: utf-8 -*-
from django.forms import *
from django import forms
from .models import *

class ReservationForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = '__all__'
		widgets = {
			'name_complete': TextInput(attrs = {'placeholder': 'Ingrese su nombre completo'}),
			'number_telephone': TextInput(attrs = {'placeholder': 'Ingrese su numero telefonico'}),
			'number_cellphone': TextInput(attrs = {'placeholder': 'Ingrese su numero celular'}),
			'email': EmailInput(attrs = {'placeholder': 'Ingrese su correo electronico'}),
		}
		labels = {
			'name_complete': 'Nombre Completo',
			'number_telephone': 'Número Telefónico',
			'number_cellphone': 'Número Celular',
			'email': 'Correo Electrónico',
			'date': 'Fecha de Reserva',
			'product_extreme': 'Producto',
		}

	def __init__(self, *args, **kwargs):
		product_extreme = kwargs.pop('product_extreme', '')
		super(ReservationForm, self).__init__(*args, **kwargs)
		self.fields['camp_product'] = forms.ModelChoiceField(label = 'Campo', queryset = Camp_product.objects.filter(product_extreme = product_extreme), empty_label = 'Seleccione un Campo')