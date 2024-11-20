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

def action(request):

    _series = series.objects.filter(series_type__iexact='Action').filter(is_published=True).order_by('-pub_date').all()

    context = {
        'serie': _series,
    }

    return render(request, 'moviedomeapp/series/action.html', context=context)

def adven(request):

    _series = series.objects.filter(series_type__iexact='Adventure').filter(is_published=True).order_by('-pub_date').all()

    context = {
        'serie': _series,
    }

    return render(request, 'moviedomeapp/series/adventure.html',context=context)

def comedy(request):

    _series = series.objects.filter(series_type__iexact='Comedy').filter(is_published=True).order_by('-pub_date').all()

    context = {
        'serie': _series,
    }

    return render(request, 'moviedomeapp/series/comedy.html',context=context)

def hor(request):

    _series = series.objects.filter(series_type__iexact='Horror').filter(is_published=True).order_by('-pub_date').all()

    context = {
        'serie': _series,
    }

    return render(request, 'moviedomeapp/series/horror.html',context=context)

def sus(request):

    _series = series.objects.filter(series_type__iexact='Suspense').filter(is_published=True).order_by('-pub_date').all()

    context = {
        'serie': _series,
    }

    return render(request, 'moviedomeapp/series/suspense.html',context=context)


def genaction(request):

    _movies = movies.objects.filter(Genre__iexact='Action').filter(is_published=True).all()
    _series = series.objects.filter(Genre__iexact='Action').filter(is_published=True).all()

    context = {
        'movies': _movies,
        'series': _series,
    }

    return render(request, 'moviedomeapp/genres/action.html')

def genadult(request):

    _movies = movies.objects.filter(Genre__iexact='Adult').filter(is_published=True).all()
    _series = series.objects.filter(Genre__iexact='Adult').filter(is_published=True).all()

    context = {
        'movies': _movies,
        'series': _series,
    }

    return render(request, 'moviedomeapp/genres/adult.html') 

def genadven(request):

    _movies = movies.objects.filter(Genre__iexact='Adventure').filter(is_published=True).all()
    _series = series.objects.filter(Genre__iexact='Adventure').filter(is_published=True).all()

    context = {
        'movies': _movies,
        'series': _series,
    }

    return render(request, 'moviedomeapp/genres/adventure.html')

def genanime(request):

    _movies = movies.objects.filter(Genre__iexact='Animation').filter(is_published=True).all()
    _series = series.objects.filter(Genre__iexact='Animation').filter(is_published=True).all()

    context = {
        'movies': _movies,
        'series': _series,
    }

    return render(request, 'moviedomeapp/genres/animation.html') 

def gencomedy(request):

    _movies = movies.objects.filter(Genre__iexact='Comedy').filter(is_published=True).all()
    _series = series.objects.filter(Genre__iexact='Comedy').filter(is_published=True).all()

    context = {
        'movies': _movies,
        'series': _series,
    }

    return render(request, 'moviedomeapp/genres/comedy.html')

def gencrime(request):

    _movies = movies.objects.filter(Genre__iexact='Crimes').filter(is_published=True).all()
    _series = series.objects.filter(Genre__iexact='Crimes').filter(is_published=True).all()

    context = {
        'movies': _movies,
        'series': _series,
    }

    return render(request, 'moviedomeapp/genres/crime.html')

def gendocument(request):

    _movies = movies.objects.filter(Genre__iexact='Documentary').filter(is_published=True).all()
    _series = series.objects.filter(Genre__iexact='Documentary').filter(is_published=True).all()

    context = {
        'movies': _movies,
        'series': _series,
    }

    return render(request, 'moviedomeapp/genres/documentary,html')