from datetime import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_protect
from . import forms
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm, RegisterForm, HotelSearchForm, HotelForm
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


## Admin Approvals Panel ---------------

def admin_approval(request):
    hotels = Hotel.objects.filter(admin_approved=False)
    reviews = Review.objects.filter(admin_approved=False)
    user = request.user
    return render(request, 'approval.html', {'hotels': hotels, 'user': user, 'reviews': reviews})

## Hotel Approval and Deletion ----------

def hotel_approvals(request):
    hotels = Hotel.objects.filter(admin_approved=False)
    user = request.user
    return render(request, 'hotel_approval.html', {'hotels': hotels, 'user': user})

def approve_hotel(request, pk):
    hotel = Hotel.objects.get(pk=pk)
    hotel.admin_approved = True
    hotel.save()
    return redirect('hotel_approvals')

def delete_hotel(request, pk):
    hotel = Hotel.objects.get(pk=pk)
    hotel.delete()
    return redirect('hotel_approvals')

## Review Approval and Deletion ----------

def review_approvals(request):
    if request.user.is_authenticated:
        hotels = Hotel.objects.filter(admin_approved=False)
        reviews = Review.objects.filter(admin_approved=False)
        user = request.user

    return render(request, 'review_approval.html', {'hotels': hotels, 'reviews': reviews, 'user': user})

def approve_review(request, pk):
    review = Review.objects.get(pk=pk)
    review.admin_approved = True
    review.save()
    messages.success(request, 'Changes successfully saved.')
    return redirect('review_approvals')

def delete_review(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('review_approvals')



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

def search_hotels(request):
    if request.method == 'POST':

        if request.POST.get('prefecture'):
            prefecture = Hotel.objects.filter(prefecture=request.POST.get('prefecture'))
        else:
            pass

        if request.POST.get('city'):
            city = Hotel.objects.filter(city=request.POST.get('city'))
        else:
            pass

        if request.POST.get('high_season'):
            high_season = Hotel.objects.filter(high_season=True)
        else:
            high_season = Hotel.objects.filter(high_season=True) | Hotel.objects.filter(high_season=False)

        if request.POST.get('dogs'):
            dogs = Hotel.objects.filter(dogs=True)
        else:
            dogs = Hotel.objects.filter(dogs=True) | Hotel.objects.filter(dogs=False)

        if request.POST.get('short_term'):
            short_term = Hotel.objects.filter(short_term=True)
        else:
            short_term = Hotel.objects.filter(short_term=True) | Hotel.objects.filter(short_term=False)

        if request.POST.get('food'):
            food = Hotel.objects.filter(food=True)
        else:
            food = Hotel.objects.filter(food=True) | Hotel.objects.filter(food=False)

        if request.POST.get('night_staff'):
            night_staff = Hotel.objects.filter(night_staff=True)
        else:
            night_staff = Hotel.objects.filter(night_staff=True) | Hotel.objects.filter(night_staff=False)



        results=city&prefecture&high_season&dogs&short_term&food&night_staff

        return render(request, 'results.html', {'results': results})

    else:
        form = HotelSearchForm()
        return render(request, 'search.html', {'form':form})

    context = {}
    return render(request, 'search.html', context)

