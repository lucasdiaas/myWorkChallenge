from django.db import models

# Create your models here.

class Geofence(models.Model):
	desc = models.CharField(max_length=200)
	latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)
	longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)
	radius = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)

	objects = models.Manager()

