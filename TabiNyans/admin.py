from django.contrib import admin
from .models import Prefecture, City, Hotel, Review, Likes

admin.site.register(Hotel)
admin.site.register(Review)
admin.site.register(Likes)