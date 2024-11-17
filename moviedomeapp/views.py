from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import series, movies
from django.db.models import F, Q
from . import fuctions
from django.db.models import Max


# Create your views here.

def base(request):
    return render(request, 'moviedomeapp/base.html')

def homepage(request):

    trending_movies = movies.objects.annotate(high=Max('views')).filter(fam__iexact='Trending').filter(is_published=True).order_by('?')[:5]
    trending_series = series.objects.annotate(high=Max('views')).filter(fam__iexact='Trending').filter(is_published=True).order_by('?')[:5]
    movie_views = movies.objects.filter(is_published=True).order_by('-pub_date')[:10]
    series_views = series.objects.filter(is_published=True).order_by('-pub_date')[:10] 


    context = {
        'movie_trend': trending_movies,
        'series_trend': trending_series,
        'movies': movie_views,
        'series': series_views,
    }

    return render(request, 'moviedomeapp/home.html',context=context)