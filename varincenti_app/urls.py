from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('varincenti_app.apps.users.urls')),
	# url(r'^', include('varincenti_app.apps.principal.urls')),
	url('', include('social.apps.django_app.urls', namespace='social')),
	# url(r'^Marcas/ExtremeEntretairment/', include('varincenti_app.apps.extreme.urls')),
	url(r'^', include('varincenti_app.apps.extreme.urls')),
]