from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class UserObjectMixin(object):
    
    def get_all_users(self):
        return User.objects.all()

class HomepageView(UserObjectMixin,TemplateView):
    template_name = 'home.html'
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        users = self.get_all_users()
        context = {
            'users': users
        }
        return render(request,self.template_name, context)

class SignupView(TemplateView):

    template_name = 'registration/signup.html'

    def get(self, request):
        form = UserCreationForm()
        context = {
            'form' : form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(user=username, password=raw_password)
            login(request, user)
            return redirect('home')
        context = {
            'form' : form,
        }
        return render(request, self.template_name, context)