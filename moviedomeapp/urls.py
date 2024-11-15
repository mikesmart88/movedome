
from django.urls import path
from . import views

# create your app urls here

urlpatterns = [
   path('', views.base, name="homepage")
]