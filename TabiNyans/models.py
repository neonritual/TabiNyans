from django.db import models
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

# with open('Prefectures.csv', 'r') as read_obj:
#     csv_dict_reader = DictReader(read_obj)
#     for row in csv_dict_reader:
#             pref = row['prefecture_en']
#             add_prefecture = Prefecture(prefecture=pref)
#             add_prefecture.save()

# with open('Prefectures.csv', 'r') as read_obj:
#     csv_dict_reader = DictReader(read_obj)
#     for row in csv_dict_reader:
#             pref = row['prefecture_en']
#             print(pref)

