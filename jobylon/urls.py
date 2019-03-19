from django.contrib import admin
from django.urls import path, include 

from . import views

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')), 
    path('auth/register/', views.signup_view, name='signup'),
    path('admin/', admin.site.urls),
    path('messaging/', include('messaging.urls')),
    path('', views.homepage_view, name='home'), 
]
