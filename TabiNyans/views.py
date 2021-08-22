from datetime import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_protect
from . import forms
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm, RegisterForm
from .models import Hotel, Review
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout




def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'index.html', context)


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
        return reverse('hotel_detail', kwargs={"pk": self.kwargs['pk']})


def register_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                login(request, new_user)
                return redirect('index')
            else:
                messages.error(request, "Error")


        context = {'form': form}
        return render(request, 'register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')

class AboutUs(TemplateView):
    template_name = "about.html"
#
# def search_hotels(request):
#     if request.method == 'POST':
#         prefecture = request.POST.get('prefecture')
#         city = request.POST.get('city')
#         results = Hotel.objects.filter(prefecture=prefecture) AND
#
#
#
#     context = {}
#     return render(request, 'search.html', context)