from varincenti_app.apps.principal.models import State
from django.contrib.auth.models import User
from datetime import datetime
from django.db import models

class ProfileUser(models.Model):
	user = models.OneToOneField(User, primary_key = True)
	photo = models.ImageField(upload_to = 'image/users/', default = 'image/users/none.png', blank = True)
	photo_2 = models.TextField(blank = True, null = True)
	number_telephone = models.CharField(max_length = 10, blank = True, null = True)
	number_cellphone = models.CharField(max_length = 10, unique = True)
	state = models.ForeignKey(State, blank = True, null = True, default = 8)
	def __str__(self):
		return str(self.user)