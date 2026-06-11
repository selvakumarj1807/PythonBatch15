from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def app01Index(request):
    return render(request, 'app01Templates/index.html')

def app01About(request):
    return render(request, 'app01Templates/about.html')