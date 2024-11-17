
from django.urls import path
from . import views

# create your app urls here

urlpatterns = [
   path('', views.homepage, name="homepage"),
   path('basedir/', views.base, name='base page')
]