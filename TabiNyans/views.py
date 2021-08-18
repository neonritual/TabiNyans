from datetime import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_protect
from . import forms
from django.http import HttpResponse
from .forms import ReviewForm
from .models import Hotel, Review
from django.views.generic import ListView, DetailView, CreateView


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

class AddReview(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review.html'

    def form_valid(self, form):
        form.instance.hotel = Hotel.objects.get(id=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)
    #
    def get_success_url(self):
        return reverse('hotel_detail',kwargs={ "pk": self.kwargs['pk'] })

