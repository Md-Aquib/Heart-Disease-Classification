from django.urls import path
from . import views

urlpatterns = [
    path('',views.UID),
    path('home',views.Home),
    path('result',views.result)
]