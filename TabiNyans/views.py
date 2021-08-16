from datetime import timezone
from urllib import request
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from . import forms
from django.http import HttpResponse
from .models import Hotel


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
    return render(request, 'add_hotel.html',  {'form': form})

def all_hotels(request):
    hotels = Hotel.objects.all
    return render(request, 'all_hotels.html', {'hotels': hotels} )




