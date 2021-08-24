from django.contrib import admin
from django.urls import include, path
from .views import AllHotels, AddReview, index, add_hotel, register_user, login_user, logout_user, \
    AboutUs, search_hotels, admin_approval, hotel_approvals, approve_hotel, delete_hotel, review_approvals, \
    approve_review, delete_review, detail_view
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
    path('approvals', admin_approval, name='approvals'),
    path('hotel_approvals', hotel_approvals, name='hotel_approvals'),
    path('approve_hotel/<int:pk>', approve_hotel, name="approve_hotel"),
    path('delete_hotel/<int:pk>', delete_hotel, name="delete_hotel"),
    path('review_approvals', review_approvals, name='review_approvals'),
    path('approve_review/<int:pk>', approve_review, name="approve_review"),
    path('delete_review/<int:pk>', delete_review, name="delete_review"),
    path('all', AllHotels.as_view(), name="all_hotels"),
    path('about', AboutUs.as_view(), name="about"),
    path('hotel/<int:pk>', detail_view, name="hotel_detail"),
    # path('hotel/<int:pk>', HotelDetailView.as_view(), name="hotel_detail"),
    path('hotel/<int:pk>/review', AddReview.as_view(), name="add_review"),
]