from django.shortcuts import render

# Create your views here.

def message_view(request, username):
    return render(request, 'home.html')