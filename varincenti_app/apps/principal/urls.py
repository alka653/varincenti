from django.conf.urls import patterns, url

urlpatterns = patterns('varincenti_app.apps.principal.views',
	url(r'^$', 'home', name = 'home'),
	url(r'^Marcas/$', 'mark', name = 'mark'),
	url(r'^Contactenos/$', 'contact', name = 'contact'),
	url(r'^404/$', 'page_404', name = 'page_404'),
)