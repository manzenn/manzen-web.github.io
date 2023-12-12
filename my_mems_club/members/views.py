from django.http import HttpResponse
from django.template import loader
from . import models
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def members(request):
  mymembers = models.Member.objects.all().values()
  template = loader.get_template('myfirst.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))      

def home(request):
    return render(request, 'home.html', {'user': request.user})

def another_page(request): 
    return render(request, 'another_page.html', {'user': request.user})

def js_game(request):
    return render(request, 'js_game.html', {'user': request.user})

def products(request):
    mymembers = models.Member.objects.all().values()
    myproducts = models.Product.objects.all().values()
    template = loader.get_template('products.html')
    context = {
        'mymembers': mymembers,
        'myproducts': myproducts,
    }
    return HttpResponse(template.render(context, request))   
    return render(request, 'products.html', {'user': request.user})