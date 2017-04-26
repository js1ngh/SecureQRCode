from django.db import models
from django.contrib.auth.models import User
import qrcode

# Create your models here.

class EventAdmin(models.Model):
	#name = models.CharField(max_length=200
	User = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
	Phone = models.CharField(max_length=11)
	Venue = models.CharField(max_length=100)
	Category = models.ForeignKey('Categories')
	StartTime = models.DateTimeField('event start time')
	EndTime = models.DateTimeField('event end time')
	TicketCost = models.DecimalField(max_digits=7, decimal_places=2)

class EndUser(models.Model):
	FirstName = models.CharField(max_length=50)
	LastName = models.CharField(max_length=50)
	Phone = models.CharField(max_length=11)
	Email = models.EmailField(max_length=100)
	Password = models.CharField(max_length=50, blank=True)
	Event = models.ForeignKey('EventAdmin')

	def generate_qrcode(self):
		qr = qrcode.QRCode(
			version=1,
			error_correction=qrcode.constants.ERROR_CORRECT_L,
			box_size=6,
			border=0,
		)
		qr.add()
		qr.make(fit=True)
		img = qr.make_image(EMail)

class Categories(models.Model):
	Name = models.CharField(max_length=100)

class Venue(models.Model):
	Name = models.CharField(max_length=100)
	Address = models.CharField(max_length=100)
	City = models.CharField(max_length=50)
	State = models.CharField(max_length=50)
	Zip = models.CharField(max_length=5)
	Country = models.CharField(max_length=50)
	MaxCapacity = models.CharField(max_length=10)


