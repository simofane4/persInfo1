from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
# Create your views here.

def home(request):
    titredepage = 'home'
    context={
        'title': titredepage
    }
    return render(request,'home.html',context)

def about(request):
    context={
        'title': "about"

    }
    return render(request,'about.html',context)


def contact(request):
    contact = Contact.objects.all()
    context={
      
    'contacts' : contact ,

    }
    return render(request,"contact.html",context)

def add_contact(request):
    context= {}
    return render(request,'add_contact.htm',context)
