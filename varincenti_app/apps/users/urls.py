from django.conf.urls import patterns, url

urlpatterns = patterns('varincenti_app.apps.users.views',
	url(r'^Login/$', 'authenticate_user', name = 'login'),
	url(r'^Logout/$', 'logout_user', name = 'logout'),
	url(r'^Registrarme/$', 'register_user', name = 'register'),
)