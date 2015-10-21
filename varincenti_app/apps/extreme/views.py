from django.contrib.auth.decorators import login_required
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
		pass
	else:
		form = ReservationForm(product_extreme = product.id)
	return render(request, 'extreme/reservation.html', {'title': title, 'product': product, 'form': form})