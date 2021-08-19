from django.contrib import admin
from django.urls import include, path
from .views import AllHotels, HotelDetailView, AddReview, index, add_hotel, register_user, login_user, logout_user
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index.as_view(), name='index'),
    path('add', add_hotel, name='add_hotels'),
    path('register', register_user, name='register'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('all', AllHotels.as_view(), name="all_hotels"),
    path('hotel/<int:pk>', HotelDetailView.as_view(), name="hotel_detail"),
    path('hotel/<int:pk>/review', AddReview.as_view(), name="add_review"),
]