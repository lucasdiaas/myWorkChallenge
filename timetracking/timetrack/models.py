from django.db import models

# Create your models here.

class TimeTrack(models.Model):
	latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)
	longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)
	date = models.DateTimeField(auto_now_add=True)

	objects = models.Manager()