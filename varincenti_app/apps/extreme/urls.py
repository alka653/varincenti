from django.conf.urls import patterns, url

urlpatterns = patterns('varincenti_app.apps.extreme.views',
	url(r'^$', 'home_extreme', name = 'home_extreme'),
	url(r'^Productos/', 'product_extreme', name = 'product_extreme'),
	url(r'^Reservas/(?P<extreme_id>\d+)/$', 'make_reservation', name = 'make_reservation'),
	url(r'^Reservas/$', 'reservations', name = 'reservations'),
	url(r'^Reservas/No-(?P<reservation_id>\d+)/Detalle/$', 'detail_reservation', name = 'detail_reservation'),
	url(r'^Reservas/No-(?P<reservation_id>\d+)/Cancelar_reserva/$', 'cancel_reservation', name = 'cancel_reservation'),
)