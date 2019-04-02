from django.urls import path, include 
from .views import MessageView

urlpatterns = [
    path('<username>/', MessageView.as_view(), name='usermessaging'),  #Shows page depending on what user you want to message
]