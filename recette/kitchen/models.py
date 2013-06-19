from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
	name = models.CharField(max_length=128)
	basic_measure = models.CharField(max_length=32)
	type = models.CharField(max_length=32)
	brand = models.CharField(max_length=128)
	
	def __unicode__(self):
		return self.name
	
		
class Kitchen(models.Model):
	user = models.ForeignKey(User)
	ingredients = models.ManyToManyField(Ingredient, through='KitchenIngredientList')
	
	def __unicode__(self):
		return 'Kitchen of ' + self.user.username
	
	
class KitchenIngredientList(models.Model):
	ingredient = models.ForeignKey(Ingredient)
	kitchen = models.ForeignKey(Kitchen)

	def __unicode__(self):
		return 'Ingredients owned by ' + self.kitchen.user.username