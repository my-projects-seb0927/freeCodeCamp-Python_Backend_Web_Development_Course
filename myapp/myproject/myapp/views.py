from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
  features = Feature.objects.all()
  return render(request, 'index.html', {'features': features})

def register(request):
  if request.method == 'POST': #Content is being sent
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    
    if password == password2: #If passwords are equal
      if User.objects.filter(email=email).exists(): #If an email alredy exists
        messages.info(request, 'Email Alredy Used')
        return redirect('register')
      elif User.objects.filter(username=username).exists(): #If an user alredy exists
        messages.info(request, 'Username Alredy Used')
        return redirect('register')
      else: #Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save();
        return redirect('login')
    else:
      messages.info(request, 'Password Not The Same')
      return redirect('register')
  else:
    return render (request, 'register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None: #User is registered
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Credentials Invalid')
      return redirect ('login')
  else:
    return render (request, 'login.html')

def logout(request):
  auth.logout(request)
  return redirect('/')


def counter(request):
  #It gets the data from the element called "text"
  #In this case: <form> element
  text = request.POST['text']
  amount_of_words = len(text.split())
  return render(request, 'counter.html', {'amount': amount_of_words})
