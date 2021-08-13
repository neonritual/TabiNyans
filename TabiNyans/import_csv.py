

import pandas as pd
# import django
# django.setup()
# import models
from TabiNyans.models import Prefecture, City

#####################################
#Add CSV Data to Prefecture:

# csv_data = pd.read_csv('Prefectures.csv')

# print(csv_data["prefecture_en"])

# csv_data_iter = csv_data.iterrows()
#
# new_prefectures = [
#     Prefecture(
#         prefecture = row["prefecture_en"]
#     )
#     for index, row in csv_data_iter
# ]
#
# Prefecture.objects.bulk_create(new_prefectures)

#---#
# #Add CSV Data to City:
#
# for pref_name in Prefecture.objects.all():
#     csv = pd.read_csv("Cities.csv")
#     for index, row in csv.iterrows():
#         if row["prefecture_en"] == pref_name.prefecture:
#             new_city = City.objects.get_or_create(prefecture=pref_name, city=row["city_en"])
