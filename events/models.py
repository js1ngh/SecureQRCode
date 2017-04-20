from django.db import models

# Create your models here.

class Event(models.Model):
	name = models.CharField(max_length=200)
	date = models.DateTimeField('event date')
	location = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Person(models.Model):
	event = models.ForeignKey(Event)
	name = models.CharField(max_length=200)

