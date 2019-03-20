from django.contrib import admin
from messaging.models import Message

# Registered message models to admin panel
admin.site.register(Message)
