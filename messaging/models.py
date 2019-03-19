from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User

class Message(models.Model):
    Sender = models.ForeignKey(User,to_field='username', on_delete=models.CASCADE, related_name='sender_set')
    Receiver = models.ForeignKey(User,to_field='username', on_delete=models.CASCADE, related_name='receiver_set')
    Message = models.CharField(max_length=1000, default="UNDEFINED")
    Date = models.CharField(max_length=250, default=timezone.now())