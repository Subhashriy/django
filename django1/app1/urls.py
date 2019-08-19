from django.urls import path
from . import views
from .views import app1ListView, app1CreateView, app1DetailView, app1UpdateView, app1DeleteView 

urlpatterns = [
    #path('',views.home,name="home"),
    path('',app1ListView.as_view(),name="home"), #class based views
    path('app1/new',app1CreateView.as_view(),name="create"),
    path('app1/<int:pk>/',app1DetailView.as_view(),name="details"),
    path('app1/<int:pk>/update/',app1UpdateView.as_view(),name="update"),
    path('app1/<int:pk>/delete/',app1DeleteView.as_view(),name="delete"),
    path('about/',views.about,name="about"),
    path('add',views.add,name="add"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout")
]
