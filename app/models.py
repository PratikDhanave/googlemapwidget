from django.contrib.gis.db import models
# Create your models here.

class City(models.Model):
	shape = models.PolygonField()
  