from django.shortcuts import render

# Create your views here.

def app03Index(request):
    return render(request, 'app03Templates/index.html')