from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .models import app1Model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.models import auth
from django.views.generic import ListView, CreateView, DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator

# Create your views here.
"""def home(request):
    #serverTime=datetime.now()
    #return HttpResponse("<h1>Home Page<h1>")
    #return render(request,"home.html",{'currTime':serverTime})
    app1=app1Model.objects.all()
    return render(request,'home.html',{'app1':app1})"""
#List View
class app1ListView(ListView):    #class based view
    model=app1Model
    template_name='home.html'
    context_object_name='app1'
    #ordering=["name"]
    paginate_by=2

#Create View
class app1CreateView(LoginRequiredMixin, CreateView):
    model=app1Model
    template_name="app1model_form.html"
    fields=["name","completed"]
    #success_url='/'
    def setUser(self,request):
        app1=self.get_object()
        app1.owner=self.request.user

#Detail View
class app1DetailView(DetailView):
    model=app1Model
    template_name="app1_detail.html"

class app1UpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model=app1Model
    template_name='app1model_form.html'
    fields=['name','completed']
    


    #method to assign username to author for updating author name in todo
    def form_valid(self,form):
        form.instance.owner=self.request.user
        return super().form_valid(form)

    #function to edit todo based on ownership
    def test_func(self):
        #get current working todo
        app1=self.get_object()
        if self.request.user==app1.owner:
            return True
        return False

class app1DeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model=app1Model
    template_name='app1_confirm_delete.html'
    success_url='/'
    
    #function to permit editing post based on their ownership
    def test_func(self):
        #get current working todo
        app1=self.get_object()
        if self.request.user==app1.owner:
            return True
        return False


def about(request):
    #return HttpResponse("<h1>About Page<h1>")
    return render(request,"about.html")


def add(request):
    #n1=int(request.GET["num1"])
    #n2=int(request.GET["num2"])
    n1=int(request.POST["num1"])
    n2=int(request.POST["num2"])
    result=n1+n2
    return render(request,"add.html",{'result':result})

def register(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,"Account created for {}!".format(username))
            return redirect('/')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            #give permission to login
            auth.login(request,user)
            return redirect('/')

        else:
            messages.error(request,"Invalid Credentials!!")
            return redirect("login")

    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})

def logout(request):
    auth.logout(request)
    return render(request,"logout.html",{})


