

from django.shortcuts import render,HttpResponse
from matplotlib.style import context
from .forms import ContactForm,ComentForm
from .models import Coment
from django.core.mail import send_mail
from django.conf import settings
def home_page(request):
     return render(request,"home.html",{})

def catalog_page(request):
     return render(request,"catalog.html",{})

def about_page(request):
     if request.POST:
          form = ComentForm(request.POST)
          if form.is_valid():
               form.save()
               return render(request,"about.html",{"massage":"Your Message has been sent"})
          else:
               return render(request,"about.html",{"er":str(form.errors)})
          
     return render(request,"about.html",{})

def contact_page(request):
     if request.POST:
          my_form = ContactForm(request.POST)
          if my_form.is_valid():
               name = request.POST['name']
      
               return render(request,"contact.html",{"massage":f"{name},ջան Ձեր հաղորդագրությունն ուղղարկված է։"})
          else:
               return render(request,"contact.html",{"massage":str(my_form.errors)})

     
     
          
            
   
     return render(request,"contact.html",{})

    
def part1(request):
     return render(request,"catalog-1.html",{})

    
def part2(request):
     return render(request,"catalog-2.html",{})

    
def part3(request):
     return render(request,"catalog-3.html",{})