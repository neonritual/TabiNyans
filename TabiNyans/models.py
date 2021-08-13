from django.db import models

class Prefecture(models.Model):
    prefecture=models.CharField(max_length=50)

class City(models.Model):
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)

