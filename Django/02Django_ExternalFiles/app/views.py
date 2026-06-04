from django.shortcuts import render

# Create your views here.

def productForm(request):
    return render(request, 'ProductForm.html')

def productTable(request):
    return render(request, 'ProductTable.html')