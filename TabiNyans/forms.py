from django.forms import ModelForm
from TabiNyans.models import Hotel


class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'prefecture', 'city',
                  'address', 'logo', 'hours', 'price', 'high_season',
                  'dogs', 'short_term', 'food', 'night_staff', 'specials',
                  'extra', 'images']
