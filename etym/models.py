from django.db import models
from django_google_maps import fields as map_fields

class Region(models.Model):
    name = models.CharField(max_length=164)
    # latitude = models.FloatField(default=0)
    # longitude = models.FloatField(default=0)
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=164)

    def __str__(self):
        return self.name

class Origin(models.Model):
    word = models.CharField(max_length=164)
    meaning = models.CharField(max_length=164)

    def __str__(self):
        return self.word

class Modern(models.Model):
    modern_word = models.CharField(max_length=164)

    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)

    def __str__(self):
        return self.modern_word
    

