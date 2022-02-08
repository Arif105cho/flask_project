from django.shortcuts import render,redirect
from .models import SignUp,Login
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .forms import SignUpForm,LoginForm
from django.contrib.auth.models import auth,User
# Create your views here.

def Home(request):
    return HttpResponse("<h2>Hello</h2>")


def index(request):
    return render(request,'home.html')

class HomeView(View):
    def get(self,request):
        user=SignUp.objects.all()#fetch the data from model
        return render(request,'home.html',context={'user':user})# return context in html page using jinja

    def post(self,request):
        user=SignUp.objects.all()
        form=SignUpForm(data=request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')  # return context in html page using ninja
        return render(request,'home.html',context={'from':form})


class LoginIn(View):
    def get(self,request):
        user=Login.objects.all()#fetch the data from model
        return render(request,'home.html',context={'user':user})# return context in html page using jinja


def home_view(request):
    context = {}
    context['form'] = LoginForm()
    return render(request, "home.html", context)
