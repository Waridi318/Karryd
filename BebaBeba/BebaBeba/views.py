from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import TransportationForm, SignUpForm


def home(request):
    return render(request, 'home.html')


def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('loggedin')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def usersignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('loggedin')
    else:
        form = SignUpForm()
    return render(request, 'sign-up.html', {'form': form})


def userlogout(request):
    logout(request)
    return redirect('home')


def loggedin(request):
    return render(request, 'loggedin.html')


# def signin(request):
#     return render(request, 'sign-up.html')


def calculate_amount_function(weight, from_destination, to_destination):
    amount = 0
    for i in range(100):
        while i <= weight:
            if from_destination == 'Koja':
                if to_destination == 'RiverRoad':
                    amount = amount + 1
                else:
                    amount = amount + 2
            else:
                if to_destination == 'RiverRoad':
                    amount = amount + 3
                else:
                    amount = amount + 4

    return amount


def calculate_amount(request):
    if request.method == 'POST':
        form = TransportationForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            from_destination = form.cleaned_data['current_location']
            to_destination = form.cleaned_data['destination']

            amount = calculate_amount_function(weight, from_destination, to_destination)

            return render(request, 'results.html', {'amount': amount})
        else:
            form = TransportationForm()

        return render(request, 'loggedin.html', {'form': form})


def results(request):
    return render(request, 'results.html')
