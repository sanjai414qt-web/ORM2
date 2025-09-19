from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_name=models.CharField()
    car_brand= models.CharField()
    release_date = models.DateField()
    car_color=models.CharField()


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_brand', 'release_date', 'car_color')

