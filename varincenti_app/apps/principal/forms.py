from django.forms import *
from django import forms
from .models import *

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'
		widgets = {
			'name_complete': TextInput(attrs = {'id': 'left-label', 'placeholder': 'Ingrese su nombre completo'}),
			'email': EmailInput(attrs = {'id': 'left-label', 'placeholder': 'Ingrese su correo electronico'}),
			'subject': TextInput(attrs = {'id': 'left-label', 'placeholder': 'Ingrese un asunto'}),
			'message': Textarea(attrs = {'id': 'left-label', 'placeholder': 'Ingrese Mensaje', 'cols': 30, 'rows': 5})
		}
		labels = {
			'name_complete': 'Nombre completo',
			'email': 'Correo electronico',
			'subject': 'Asunto',
			'message': 'Mensaje'
		}
		error_messages = {
			'name_complete': {
				'required': 'Por favor ingrese su nombre completo'
			},
			'email': {
				'required': 'Por favor ingrese su correo electronico'
			},
			'subject': {
				'required': 'Por favor ingrese un asunto'
			},
			'message': {
				'required': 'Por favor ingrese su mensaje'
			},
		}