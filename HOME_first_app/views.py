from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# imported by me
from datetime import datetime
from HOME_first_app.models import Contact
from django.contrib import messages

def home(request):
    # return HttpResponse('this is HOME page')
    return render(request, 'index.html')

def about(request):
    # return HttpResponse('this is ABOUT page')
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse('this is CONTACT page')
    if request.method =='POST':
        name = request.POST.get('name')
        email =request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc ,date=datetime.today())
        contact.save()
        
        messages.success(request, 'YOUR MESSAGE HAS BEEN SENT ! THANK YOU FOR CONTACTING ')  #THIS IS THE MESSAGE WHICH WILL BE DISPLAYED AFTER SUBMITTING FORM , WILL BE HANDLED FROM VIEWS.PY copy this from django documentaion/or search django messages framework
    
    return render(request, 'contact.html')

def links(request):
    # return HttpResponse('this is LINKS page')
    return render(request, 'links.html')


