from django.contrib.auth.models import User
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from csv import DictReader
import pandas as pd

class Prefecture(models.Model):
    prefecture=models.CharField(max_length=50)

    def __str__(self):
        return self.prefecture

class City(models.Model):
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100, verbose_name='Hotel Name')
    location_url = models.URLField(max_length=400, verbose_name='Google Maps URL', default='https://google.com')
    prefecture = models.ForeignKey(Prefecture, on_delete=models.SET_NULL, blank=True, null=True)
    city = ChainedForeignKey(
        City,
        chained_field="prefecture",
        chained_model_field="prefecture",
    )
    address = models.CharField(max_length=100, verbose_name='Address')
    logo = models.ImageField(upload_to='logos/', verbose_name='Hotel Logo', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hours = models.CharField(max_length=100, verbose_name='Open Hours', blank=True)
    price = models.CharField(max_length=100, verbose_name='Nightly Price', blank=True)
    high_season = models.BooleanField(verbose_name='High Season Rates')
    dogs = models.BooleanField(verbose_name='Dogs on Premises')
    short_term = models.BooleanField(verbose_name='Short Term Available')
    food = models.BooleanField(verbose_name='Food Available')
    night_staff = models.BooleanField(verbose_name='24HR Staff')
    specials = models.CharField(max_length=200, verbose_name='Special Services', blank=True)
    extra = models.CharField(max_length=200, verbose_name='Other Information', blank=True)
    images = models.ImageField(upload_to='hotel_image/', verbose_name='Hotel Image', blank=True, null=True)
    admin_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.hotel_name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING)
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment = models.CharField(max_length=500)
    rating = models.IntegerField(choices=RATING_CHOICES)