
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

   path('action/', views.action, name='action series'),
   path('adventures/', views.adven, name='adventure series'),
   path('comedy/', views.comedy, name='comedy series'),
   path('horror/', views.hor, name='horror series',),
   path('suspense/', views.sus, name='suspense series'),
   

   path('genres/action/', views.genaction, name='genres action'),
   path('genres/adult/', views.genadult, name='genres adult'),
   path('genres/adventure/', views.genadven, name='genres adventure'),
   path('genres/animation/', views.genanime, name='genres animation'),
   path('genres/comedy/', views.gencrime, name='genres crime'),
   path('genres/documemnt/', views.gendocument, name='genres ducumetation'),
]