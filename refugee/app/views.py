from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Refugee, NGO
from django.contrib.auth.decorators import login_required


def login(request):
    if request.user.is_authenticated:
        return render(request, 'app/profile.html', {})
    else:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return render(request, 'app/profile.html', {})
                else:
                    error = 'Your Rango account is disabled.'
                    return render(request, 'app/login.html', {'error': error})
            else:
                error = 'Incorrect Username or Password'
                return render(request, 'app/login.html', {'error': error})
        else:
            return render(request, 'app/login.html', {})


def logout(request):
    auth_logout(request)
    return redirect(reverse('app:login'))


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        FirstName = request.POST.get('fname', '')
        LastName = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        user = User.objects.create_user(username=username, email=email, first_name=FirstName, last_name=LastName)
        user.set_password(password)
        user.save()
        country = request.POST.get('country', '')
        bio = request.POST.get('bio', '')
        age = request.POST.get('age', '')
        mobileNo = request.POST.get('mobileNo', '')
        gender = request.POST.get('gender', '')
        passport = request.POST.get('passport', '')

        refugee = Refugee.objects.create(refugee=user, country=country, bio=bio, age=age, mobileNo=mobileNo,
                                         gender=gender, passport=passport)
        refugee.save()
    else:
        return render(request, 'app/registration.html', {})


def ngo_register(request):
    if request.user.is_authenticated:
        return render(request, 'app/test.html', {})
    if request.method == 'GET':
        return render(request, "app/ngo_register.html", {})
    name = request.POST.get("name")
    password = request.POST.get("password")
    email = request.POST.get("email")

    if User.objects.filter(username=name).exists():
        error = 'The NGO is already registered.'
        return render(request, 'app/ngo_register.html', {'error': error})
    user = User.objects.create_user(username=name, email=email)
    user.set_password(password)
    user.save()
    country = request.POST.get("country", "")
    ngo_id = request.POST.get("ngo_id", "")
    ngo = NGO.objects.create(user=user, name=name, country=country, ngo_id=ngo_id)
    ngo.save()
    auth_login(request, user)
    return redirect('app:ngo_profile', pk=user.id)


@login_required(login_url="app:ngo_login")
def ngo_profile(request, pk):
    ngo = get_object_or_404(NGO, id=pk)
    return render(request, 'app/ngo_profile.html', {'ngo': ngo})


def ngo_login(request):
    if request.user.is_authenticated:
        return redirect('app:ngo_profile', pk=request.user.ngo.id)
    if request.method == 'GET':
        return render(request, 'app/ngo_login.html', {})
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
        auth_login(request, user)
        return redirect('app:ngo_profile', pk=user.ngo.id)
    else:
        error = 'The NGO does not exist.'
        return render(request, 'app/ngo_login.html', {'error': error})


def ngo_logout(request):
    auth_logout(request)
    return redirect(reverse('app:ngo_login'))
