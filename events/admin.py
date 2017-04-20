from django.contrib import admin
from .models import EventAdmin, EndUser, Categories, Venue


# Register your models here.
admin.site.register(EventAdmin)
admin.site.register(Categories)
