

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Book

# Home view to display books
def home_view(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'book_review/book_list.html', {'books': books})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'book_review/login.html', {'form': form})

# Sign Up view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error in sign-up. Please try again.')
    else:
        form = UserCreationForm()
    return render(request, 'book_review/signup.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')
