from django.urls import path, include 
from . import views

urlpatterns = [
    path('<username>/', views.message_view, name='usermessaging'),  #Shows page depending on what user you want to message
]