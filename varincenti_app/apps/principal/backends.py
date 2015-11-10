from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.contrib.auth import login

def premissions_check(view):
	def check(request, *args, **kwargs):
		title = None
		if request.user.groups.filter(name = 'Administrator').exists():
			return view(request, *args, **kwargs)
		else:
			return HttpResponseRedirect('/Marcas/ExtremeEntretairment')
	return check

def check_auth(view):
	def check(request, *args, **kwargs):
		if request.user.is_authenticated():
			return HttpResponseRedirect('/Marcas/ExtremeEntretairment')
		else:
			return view(request, *args, **kwargs)
	return check
