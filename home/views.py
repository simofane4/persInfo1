from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm
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
    form = ContactForm
    context= {
        'form': form,
    }
    return render(request,'add_contact.html',context)
