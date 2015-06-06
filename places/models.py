from django.db import models
from .widgets import LocationField


class Place(models.Model):
    name = models.CharField(max_length=255)
    qr_code = models.CharField(max_length=500, blank=True)
    coverage = models.IntegerField(default=1000)
    location = LocationField(blank=True, max_length=255)

    def save(self, *args, **kwargs):
        super(Place, self).save(*args, **kwargs)
        size = "120x120"
        value = "http://localhost:8000/places/%s" % (self.id)
        qr_url = "http://chart.apis.google.com/chart?chs=%s&cht=qr&chl=%s&choe=UTF-8&chld=H|0" % (size, value)
        self.qr_code = qr_url
        super(Place, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class TypePlace(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class PlaceOfInterest(models.Model):
    name = models.CharField(max_length=255)
    types = models.ManyToManyField(TypePlace)
    location = LocationField(blank=True, max_length=255)

    def __unicode__(self):
        return self.name
