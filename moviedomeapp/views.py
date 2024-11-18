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

# movies views

def chinesm(request):
    cmovie = movies.objects.filter(movie_types__iexact='Chinese movies').filter(is_published=True).order_by('-pub_date').all()

    context = {
        'cmovies':cmovie
    }

    return render(request, 'moviedomeapp/movies/chinesmovies.html', context=context)

def anime(request):
    cmovie = movies.objects.filter(movie_types__iexact='Animation movies').filter(is_published=True).order_by('-pub_date').all()

    context = {
        'cmovies':cmovie
    }

    return render(request, 'moviedomeapp/movies/animation.html', context=context)

def hollywood(request):
    cmovie = movies.objects.filter(movie_types__iexact='Hollywood').filter(is_published=True).order_by('-pub_date').all()

    context = {
        'cmovies':cmovie
    }

    return render(request, 'moviedomeapp/movies/hollywood.html', context=context)

def india(request):
    cmovie = movies.objects.filter(movie_types__iexact='Indian movies').filter(is_published=True).order_by('-pub_date').all()

    context = {
        'cmovies':cmovie
    }

    return render(request, 'moviedomeapp/movies/india.html', context=context)

def japan(request):
    cmovie = movies.objects.filter(movie_types__iexact='Japanese movies').filter(is_published=True).order_by('-pub_date').all()

    context = {
        'cmovies':cmovie
    }

    return render(request, 'moviedomeapp/movies/japan.html', context=context)

def korean(request):
    cmovie = movies.objects.filter(movie_types__iexact='Korean drama').filter(is_published=True).order_by('-pub_date').all()

    context = {
        'cmovies':cmovie
    }

    return render(request, 'moviedomeapp/movies/korean.html', context=context)


def philipin(request):
    cmovie = movies.objects.filter(movie_types__iexact='Philipine movies').filter(is_published=True).order_by('-pub_date').all()

    context = {
        'cmovies':cmovie
    }

    return render(request, 'moviedomeapp/movies/philipen.html', context=context)

def nollyhood(request):
    cmovie = movies.objects.filter(movie_types__iexact='Nollywood').filter(is_published=True).order_by('-pub_date').all()

    context = {
        'cmovies':cmovie
    }

    return render(request, 'moviedomeapp/movies/nollywood.html', context=context)

