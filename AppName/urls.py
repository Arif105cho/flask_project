from django.urls import path
from .views import *

app_name='AppName'

urlpatterns=[
    path('home/',HomeView.as_view()),
    path('index/',home_view,name='index'),
    path('signin/',LoginIn.as_view(),name='signin'),

]