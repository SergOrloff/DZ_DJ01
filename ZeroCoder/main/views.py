from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    return render(request, 'main/contact.html')

def beast(request):
    return render(request, 'main/beast.html')

def index(request):
    return render(request, 'main/index.html')
def new(request):
    return render(request, 'main/new.html')