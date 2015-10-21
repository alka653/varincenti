from django.db import models

class Product_extreme(models.Model):
	name = models.CharField(max_length = 50)
	description = models.CharField(max_length = 100)
	tag = models.CharField(max_length = 250)
	conditions = models.CharField(max_length = 3000)
	photo = models.ImageField(upload_to = 'image/extreme/product/')
	def __str__(self):
		return self.name

class Place_camp(models.Model):
	name = models.CharField(max_length = 100)
	direction = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200, blank = True)
	def __str__(self):
		return self.name

class Camp_product(models.Model):
	product_extreme = models.ForeignKey(Product_extreme, blank = False, null = True)
	place_camp = models.ForeignKey(Place_camp, blank = False, null = True)
	def __str__(self):
		return str(self.place_camp)

class Reservation(models.Model):
	name_complete = models.CharField(max_length = 50)
	number_telephone = models.CharField(max_length = 10, blank = True)
	number_cellphone = models.CharField(max_length = 10)
	email = models.EmailField()
	date = models.DateTimeField(auto_now = False)
	camp_product = models.ForeignKey(Camp_product, blank = False, null = True)
	def __str__(self):
		return self.asunto