
from django.urls import path
from . import views

# create your app urls here

urlpatterns = [
   path('', views.homepage, name="homepage"),
   path('basedir/', views.base, name='base page'),

   path('animation/', views.anime, name='animationpage'),
   path('chinese/', views.chinesm, name='chinese movies'),
   path('hollywood/', views.hollywood, name='hollywood page'),
   path('india/', views.india, name='indiapages'),
   path('japan/', views.japan, name='japan movies'),
   path('korean/', views.korean, name='korean movies'),
   path('Philipine/', views.philipin, name='philipin page'),
   path('nollyhood/', views.nollyhood, name='nollyhood pages'),
   
]