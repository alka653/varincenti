from django.contrib.auth.models import User, Group

def premissions_check(view):
	def check(request, *args, **kwargs):
		title = None
		if request.user.groups.filter(name = 'Administrator').exists():
			context = {'title': 'Bienvenido'}
		else:
			context = {'title': 'Hola'}
		args = args + (context, )
		return view(request, *args, **kwargs)
	return check