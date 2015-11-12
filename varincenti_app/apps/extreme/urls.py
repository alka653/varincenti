from django.conf.urls import patterns, url

urlpatterns = patterns('varincenti_app.apps.extreme.views',
	url(r'^invite/$', 'invite', name = 'invite'),
	url(r'^$', 'home_extreme', name = 'home_extreme'),
	url(r'^search-camp/', 'search_camp', name = 'search_camp'),
	url(r'^Productos/', 'product_extreme', name = 'product_extreme'),
	url(r'^Reservas/$', 'reservations', name = 'reservations'),
	url(r'^Reservas/(?P<extreme_id>\d+)/$', 'make_reservation', name = 'make_reservation'),
	url(r'^Reservas/(?P<reservation_id>\d+)/Agregar-jugadores/$', 'make_reservation_player', name = 'make_reservation_player'),
	url(r'^Reservas/(?P<reservation_player_id>\d+)/Eliminar-jugadores/$', 'delete_reservation_player', name = 'delete_reservation_player'),
	url(r'^Reservas/No-(?P<reservation_id>\d+)/Detalle/$', 'detail_reservation', name = 'detail_reservation'),
	url(r'^Reservas/No-(?P<reservation_id>\d+)/Eliminar/$', 'delete_reservation', name = 'delete_reservation'),
	url(r'^Reservas/No-(?P<reservation_id>\d+)/Cancelar_reserva/$', 'cancel_reservation', name = 'cancel_reservation'),
)