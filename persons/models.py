from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=255)
	age = models.IntegerField()
	description = models.CharField(max_length=255)
	country = models.ForeignKey(Country)

	def __str__(self):
		return self.name