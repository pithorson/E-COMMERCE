from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactMessageForm
#from .models import User
# Create your views here.
def home(request):
   return render(request,"index.html")

def shop(request):
   return render(request,"shop.html")

def about(request):
   return render(request,"about.html")

def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "contact.html")
    else:
        form = ContactMessageForm()

    return render(request, "contact.html", {'form': form})

def product(request):
    return render(request,"product1.html")

