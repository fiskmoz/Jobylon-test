from django.shortcuts import render, redirect
from .models import Message
from django.db.models import Q
from .forms import MessageForm
from django.contrib.auth.models import User

# Defined for POST and GET. 
# GET returns and displays messages filtered by sender,receiver and then ordered by the creation date.
# POST checks if the form is valid and if so creates the new message and updates the site to include it.
def message_view(request, username):
    if request.user.username == username: 
        return redirect('home')
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST or None)
        if form.is_valid():
            instance  = form.save(commit=False)
            instance.Sender = request.user
            instance.Receiver = User.objects.get(username=username)
            instance.save()
            form = MessageForm()
    messages = Message.objects.filter(Q(Sender=request.user.username, Receiver= username) | Q(Sender=username, Receiver = request.user.username)).order_by('Date')
    return render(request, 'messaging/message.html', {'me':request.user.username, 'chatfriend': username, 'messages': messages, 'form': form})