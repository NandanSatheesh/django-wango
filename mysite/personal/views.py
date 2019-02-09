from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):

    return render(request , 'personal/home.html' )

def contact(request):

    return render(request, 'personal/contact.html', {'content': ['You can email me at nandan.199776@gmail.com',]})
