from django.contrib import admin
from django.urls import include, path
from . import views
from .views import AllHotels, HotelDetailView, AddReview
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_hotel, name='add_hotels'),
    path('all', AllHotels.as_view(), name="all_hotels"),
    path('hotel/<int:pk>', HotelDetailView.as_view(), name="hotel_detail"),
    path('hotel/<int:pk>/review', AddReview.as_view(), name="add_review"),
]