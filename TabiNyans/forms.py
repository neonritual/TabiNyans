from django.forms import ModelForm
from TabiNyans.models import Hotel, Review


class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'prefecture', 'city', 'website_url', 'location_url',
                  'address', 'logo', 'hours', 'price', 'high_season',
                  'dogs', 'short_term', 'food', 'night_staff', 'specials',
                  'extra', 'images']

class ReviewForm(ModelForm):
    class Meta:
       model = Review
       fields = ['comment', 'rating']

