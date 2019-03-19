from django.shortcuts import render, redirect
from messaging.models import Message
from django.db.models import Q
from .forms import MessageForm
from django.contrib.auth.models import User

# Create your views here.

def message_view(request, username):
    if request.user.username == username: 
        return redirect('home')
    if request.method == "POST":
        form = MessageForm(request.POST or None)
        if form.is_valid():
            formmessage = form.cleaned_data['message']
            message = Message(Sender=request.user, Receiver = User.objects.get(username=username), Message = formmessage)
            message.save()
    messages = Message.objects.filter(Q(Sender=request.user.username) | Q(Sender=username)).order_by('Date')
    form = MessageForm()
    return render(request, 'messaging/message.html', {'me':request.user.username, 'chatfriend': username, 'messages': messages, 'form': form})
        