from django.shortcuts import render
from django.contrib.auth.models import User
from .models import NGO


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
    ngo = NGO.objects.create(user=user, country=country, ngo_id=ngo_id)
    ngo.save()
    return render(request, "app/ngo_profile.html", {})
