
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [

    path('create/',CreateUser.as_view(),name='create'),
    path('list/', ListUser.as_view(), name='list'),
    path('update/<int:pk>', UpdateUser.as_view(), name='update'),
    path('delete/<int:pk>', DeleteUser.as_view(), name='update'),

    path('create1/',CreateUser1.as_view()),
    path('login/',LoginClass.as_view())
]