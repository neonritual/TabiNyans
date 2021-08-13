

import pandas as pd
import django
django.setup()
# import models
from TabiNyans.models import Prefecture, City

#####################################
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
#######################################################

#---#
# csv = pd.read_csv("Cities.csv")
# City.objects.filter(prefecture=pref_var)
#
# City(
#
# )


