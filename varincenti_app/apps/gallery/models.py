from django.db import models

class Type_gallery(models.Model):
	name = models.CharField(max_length = 50)
	def __str__(self):
		return self.name

class Gallery(models.Model):
	name = models.CharField(max_length = 50)
	date = models.DateTimeField(auto_now = True)
	description = models.CharField(max_length = 200, blank = True)
	photo = models.ImageField(upload_to = 'image/gallery/')
	type_gallery = models.ForeignKey(Type_gallery)
	def __str__(self):
		return self.name