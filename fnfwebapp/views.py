from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import views as auth_views


from django.http import JsonResponse



def home(request):

    products = Products.objects.all()
    categories = Category.objects.all()

    # Check if a category is selected
    selected_category = request.GET.get('category')
    searched = request.POST.get('q')

    if selected_category:
        # Filter food items by the selected category
        products = Products.objects.filter(category__slug=selected_category)
        return products
    elif searched:
        products = Products.objects.filter(title__icontains=searched)
    
    return render (request, 'foodnfries.html', {'products':products,'categories':categories})

def product_all(request):
    products = Products.objects.all()
    return render(request, 'home.html', {'products': products})


def signup(request):
    return  render(request, "signup.html" )

def login(request):
    return  render(request, "login.html" )

def addToCart(request):
    return  render(request, "addToCart.html" )

def orderSummary(request):
    return  render(request, "orderSummary.html" )

def findFood(request):
    return  render(request, "trackButton.html" )

def searchFood(request):
    if request.method == 'POST':
            search = request.POST ['search'] 
        
            return  render (request, "searchFood.html"  )
    else:
            return  render(request, "searchFood.html" )

    















# def book(request):
#     return  render(request, "book.html" )


# # def clients(request):
#     return  render(request, "clients.html" )

# def fnfhome(request):
#     return  render(request, "foodnfries.html" )

