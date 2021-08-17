from datetime import timezone
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from . import forms
from django.http import HttpResponse
from .forms import ReviewForm
from .models import Hotel
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy


def index(request):
    return HttpResponse("Hello, world. Welcome to TabiNyans.")


@csrf_protect
def add_hotel(request):
    if request.method == 'POST':
        form = forms.HotelForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.author = request.user
            temp.save()
            return HttpResponse("Submission complete.")
    else:
        form = forms.HotelForm()
    return render(request, 'add_hotel.html', {'form': form})


class AllHotels(ListView):
    model = Hotel
    template_name = 'all_hotels.html'


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotel.html'

#
# def hotel_detail(request, slug):
#     template_name = 'hotel.html'
#     hotel = get_object_or_404(Hotel, slug=id)
#     reviews = hotel.reviews.filter(admin_approved=True)
#     new_review = None
#     if request.method == 'POST':
#         review_form = ReviewForm(data=request.POST)
#         if review_form.is_valid():
#             new_review = review_form.save(commit=False)
#             new_review.hotel = hotel
#             new_review.save()
#         else:
#             review_form = ReviewForm()
#
#         return render(request, template_name, {'hotel': hotel,
#                                                'reviews': reviews,
#                                                'new_review': new_review,
#                                                'review_form': review_form,
#                                                'slug': hotel.pk
#                                                })


# class HotelReview(Edit)
#     form_class = ReviewForm
#
#
