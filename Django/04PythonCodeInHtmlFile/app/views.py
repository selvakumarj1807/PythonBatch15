from django.shortcuts import render

# Create your views here.

def index(request):
    userData = {
        'name': 'John Doe',
        'age': 15,
        'email': 'john.doe@example.com'
    }
    
    users = [
        {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'},
        {'name': 'Bob', 'age': 12, 'email': 'bob@example.com'},
        {'name': 'Charlie', 'age': 35, 'email': 'charlie@example.com'},
        {'name': 'David', 'age': 17, 'email': 'david@example.com'}
    ]
    
    return render(request, 'index.html', {'user': userData, 'users': users})