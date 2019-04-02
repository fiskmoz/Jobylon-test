from django.shortcuts import render, redirect
from .models import Message
from django.db.models import Q
from .forms import MessageForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView

# Defined a mixin for the TemplateView. This can be used to reduce redundancy by having this class
# define and be called upon when accessing Message objects.

class MessageObjectMixin(object):
    
    def filter_messages(self, sender, receiver):
        return Message.objects.filter(Q(Sender=sender, Receiver= receiver) | Q(Sender=receiver, Receiver = sender)).order_by('Date')

# Defined for POST and GET. 
# GET returns and displays messages filtered by sender,receiver and then ordered by the creation date.
# POST checks if the form is valid and if so creates the new message and updates the site to include it.

class MessageView(MessageObjectMixin,TemplateView): 

    template_name = 'messaging/message.html' 

    def get(self, request, username):
        if request.user.username == username: 
            return redirect('home')
        form = MessageForm()
        messages = self.filter_messages(request.user.username, username)
        context = {
            'me':request.user.username, 
            'chatfriend': username, 
            'messages': messages, 
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, username):
        if request.user.username == username: 
            return redirect('home')
        form = MessageForm(request.POST or None)
        if form.is_valid():
            instance  = form.save(commit=False)
            instance.Sender = request.user
            instance.Receiver = User.objects.get(username=username)
            instance.save()
        form = MessageForm()
        messages = self.filter_messages(request.user.username, username)
        context = {
            'me':request.user.username, 
            'chatfriend': username, 
            'messages': messages, 
            'form': form
        }
        return render(request, self.template_name, context)