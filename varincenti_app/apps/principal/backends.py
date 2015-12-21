from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login

def premissions_check(view):
	def check(request, *args, **kwargs):
		title = None
		if request.user.groups.filter(name = 'Administrator').exists():
			return view(request, *args, **kwargs)
		else:
			return HttpResponseRedirect(reverse('home_extreme'))
	return check

def check_auth(view):
	def check(request, *args, **kwargs):
		if request.user.is_authenticated():
			return HttpResponseRedirect(reverse('home_extreme'))
		else:
			return view(request, *args, **kwargs)
	return check
