from django.contrib import admin
from django.urls import include, path
from .views import AllHotels, HotelDetailView, AddReview, index, add_hotel, register_user, login_user, logout_user, AboutUs, search_hotels, admin_approval, hotel_approval
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', index.as_view(), name='index'),
    path('', index, name='index'),
    path('add', add_hotel, name='add_hotels'),
    path('register', register_user, name='register'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('search', search_hotels, name='search'),
    path('approval', admin_approval, name='approval'),
    path('hotel_approval', hotel_approval, name='hotel_approval'),
    path('all', AllHotels.as_view(), name="all_hotels"),
    path('about', AboutUs.as_view(), name="about"),
    path('hotel/<int:pk>', HotelDetailView.as_view(), name="hotel_detail"),
    path('hotel/<int:pk>/review', AddReview.as_view(), name="add_review"),
]