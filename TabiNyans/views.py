from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from . import forms

from django.http import HttpResponse


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




