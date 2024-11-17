from django.db import models
import os, datetime, string, random
from django.utils import timezone
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import PIL
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse
from . import fuctions
from django.utils.text import slugify 
from django.utils.timezone import now
from django.core.files.base import ContentFile

# Create your models here.
# this will be used form the about us 
class staff(models.Model):
    name = models.CharField('staff fullname', max_length=200, null=False, blank=False)
    bio = models.TextField('staff biography', max_length=500, null=False, blank=False)
    country = models.CharField('staff country', max_length=200, null=False, blank=False, default='Nigeria')
    staff_pics = models.ImageField('staff image', upload_to='staff_pics',null=True, blank=True)
    staff_pics2 = models.ImageField('staff image2', upload_to='staff_pics', null=True, blank=True)
    yo_channels = models.URLField('youtube_channels', null=True, blank=True)
    fb_link = models.URLField('facebook_link', null=True, blank=True)
    instagram_link = models.URLField('instagram', null=True, blank=True)
    website_link = models.URLField('website_link',null=True, blank=True)

    def __str__(self):
        return self.name
    

class movies(models.Model):

    movies_category = [
        ('Chinese movies','Chinese movies'),
        ('Philipine movies','Philipine movies'),
        ('Korean drama','Korean drama'),
        ('Indian movies','Indian movies'),
        ('Nollywood','Nollywood'),
        ('Hollywood','Hollywood'),
        ('Animation movies','Animation movies'),
        ('Japanese movies','Japanese movies'),
        ('American movie','American movies'),
    ]
    movie_type = [
        ('Trending','Trending'),
        ('Documentary','documentary'),
        ('General','General'),
    ]
    Genres = [
       ('Action','Action'),
       ('Adventure','Adventure'),
       ('Adult','Adult'),
       ('Animation','Animation'),
       ('Comedy','Comedy'),
       ('Crimes','Crimes'),
       ('Documentary','Documentary'),
    ]

    movie_name = models.CharField('movies name',null=False, blank=False,unique=True, max_length=200)
    s_title = models.TextField('the search title for this movie can include the movie name and movie discription or bio',null=False, blank=False)
    title = models.TextField('a simple page title',null=False, blank=False)
    meta = models.TextField('meta discrption for the movie page somthing that discribes the movie',null=False, blank=False)
    discription = models.TextField('movies discription about the movie ', null=False, blank=False)
    movie_types = models.CharField('select the categories to clasifile the movie', max_length=200, choices=movies_category,default='American movies')
    fam = models.CharField('the image types select', max_length=200, null=False, choices=movie_type, blank=False, default='General')
    Genre = models.CharField('movies genre', max_length=200, null=False, blank=False, choices=Genres)
    views = models.BigIntegerField('number of views and visits, pls do not add this this will automatically add it self', null=True, blank=True, default=0)
    posted_by = models.CharField('add name of staff posting this vidie', null=False, blank=False, max_length=200)
    duration = models.CharField('mins of movie length the duration', null=False, blank=False, max_length=50)
    reales = models.IntegerField('movies reales date',null=True, blank=False, default=2020)
    pub_date = models.DateTimeField('published date')
    frame = models.ImageField('frame cover image of the movie',null=False, blank=False, upload_to='movie_pics')
    movie_file = models.FileField('file of the movie, if mocvie is seasonal please add the part one',null=False,blank=False, unique=True, upload_to='moviefiles')
    is_edited = models.BooleanField('do not add this its for the file and image editions', default=False)
    is_published = models.BooleanField('if movie is publised',default=False)
    thumbnail = models.ImageField('thumbnail do not add this ', upload_to='movie_thumbnails', null=True, blank=True)
    slug_name = models.SlugField('movie special slug do not add', null=True, blank=True, max_length=200, unique=True)
    search_str = models.TextField('movies search string this will auto generate', null=True, blank=True)
    spec_id = models.CharField('do not add it will auto generate, movies string',max_length=50, null=True, blank=True, unique=True)
    verifed = models.BooleanField('do not click this verification', default=False)

    class Meta:
        ordering = ['-pub_date']

    def was_publised_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        if self.is_published == False:
            return f'{self.movie_name} ------ (not_published)'
        else:
            return f'{self.movie_name} ----- (published)'
        
    def save(self , *args, **kwargs):

        if self.verifed == False:
            self.search_str = f'{self.title}'
            self.slug_name = fuctions.rand_string_generator(10)
            self.spec_id = f'{fuctions.rand_string_generator(7)}{self.movie_name}'
            self.verifed = True
        else:
            pass
        if self.is_edited == False:
            if self.frame:
                # editing the inage frame and moviefile
                in_img = Image.open(self.frame)
                in_img = in_img.convert("RGB")

                # resizing the frame

                i = in_img
                img_h = i.height-30 if i.height > 400 else i.height-10
                img_w = i.width-30  if i.width > 400 else i.width-10
                i = i.resize((img_w, img_h), PIL.Image.Resampling.LANCZOS)

                i_io = BytesIO()
                i.save(i_io, format='PNG')
                self.frame = InMemoryUploadedFile(i_io, None, f'Moviedome{self.movie_name}{fuctions.rand_string_generator(10)}.png', 'image/jpg', None, None)
                #adding thumbnails images
                i = Image.open(self.frame)
                i.thumbnail((180, 180), PIL.Image.Resampling.LANCZOS)
                i_io= BytesIO()
                i.save(i_io, format='PNG', quality=50)
                self.thumbnail = InMemoryUploadedFile(i_io, None, f'thumbnail-Moviedome{self.movie_name}{fuctions.rand_string_generator(10)}.png', 'image/png', None, None)

                self.is_edited 
            else:
                pass
            if self.movie_file:
                    origin_name = self.movie_file.name
                    extention = origin_name.split('.')[-1]

                    new_name = f'Moviedome_{self.movie_name}{fuctions.rand_string_generator(7)}{now().strftime('%Y%m%d%H%M%S')}.{extention}'

                    file_content = self.movie_file.read()

                    self.movie_file.save(new_name, ContentFile(file_content), save=False)
            else:
                pass
        else:
            pass
        return super(movies, self).save(*args, **kwargs)
    
class series(models.Model):

    series_category = [
        ('Animation','Animation'),
        ('Comedy','Comedy'),
        ('Adventure','Adventure'),
        ('Horror','Horror'),
        ('Action','Action'),
        ('Suspense','Suspense'),
    ]
    Genres = [
       ('Action','Action'),
       ('Adventure','Adventure'),
       ('Adult','Adult'),
       ('Animation','Animation'),
       ('Crimes','Crimes'),
       ('Comedy','Comedy'),
       ('Documentary','Documentary'),
    ]
    serie_type = [
        ('trending','trending'),
        ('Documentary','documentary'),
        ('General','General'),
    ]
    series_name = models.CharField('series name',null=False, blank=False,unique=True, max_length=200)
    s_title = models.TextField('the search title for this series can include the series name and series discription or bio',null=False, blank=False)
    title = models.TextField('a simple page title',null=False, blank=False)
    meta = models.TextField('meta discrption for the series page somthing that discribes the series',null=False, blank=False)
    discription = models.TextField('movies discription about the movie ', null=False, blank=False)
    series_type = models.CharField('select the categories to clasifile the series', max_length=200, choices=series_category,default='American movies')
    fam = models.CharField('the series types select', max_length=200, choices=serie_type, default='General')
    Genre = models.CharField('series genre', max_length=200, null=False, blank=False, choices=Genres)
    views = models.BigIntegerField('number of views and visits, pls do not add this this will automatically add it self', null=True, blank=True, default=0)
    posted_by = models.CharField('add name of staff posting this vidie', null=False, blank=False, max_length=200)
    duration = models.CharField('mins of movie length the duration', null=False, blank=False, max_length=50)
    reales = models.IntegerField('series reales date',null=True, blank=False, default=2020)
    pub_date = models.DateTimeField('published date')
    frame = models.ImageField('frame cover image of the series',null=False, blank=False, upload_to='series_pics')
    series_file = models.FileField('file of the seies, if series is seasonal please add the part one',null=False,blank=False, unique=True, upload_to='seriesfiles')
    is_edited = models.BooleanField('do not add this its for the file and image editions', default=False)
    is_published = models.BooleanField('if movie is publised',default=False)
    thumbnail = models.ImageField('thumbnail do not add this ', upload_to='movie_thumbnails', null=True, blank=True)
    slug_name = models.SlugField('series special slug do not add', null=True, blank=True, max_length=200, unique=True)
    search_str = models.TextField('series search string this will auto generate', null=True, blank=True)
    spec_id = models.CharField('do not add it will auto generate, movies string',max_length=50, null=True, blank=True, unique=True)
    verifed = models.BooleanField('do not click this verification', default=False)


    class Meta:
        ordering = ['-pub_date']

    def was_publised_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        if self.is_published == False:
            return f'{self.series_name} ------ (not_published)'
        else:
            return f'{self.series_name} ----- (published)'
        
    def save(self , *args, **kwargs):

        if self.verifed == False:
            self.search_str = f'{self.title}'
            self.slug_name = fuctions.rand_string_generator(10)
            self.spec_id = f'{fuctions.rand_string_generator(7)}{self.series_name}'
            self.verifed = True
        else:
            pass
        if self.is_edited == False:
            if self.frame:
                # editing the inage frame and moviefile
                in_img = Image.open(self.frame)
                in_img = in_img.convert("RGB")
                # resizing the frame
                i = in_img
                img_h = i.height-30 if i.height > 400 else i.height-10
                img_w = i.width-30  if i.width > 400 else i.width-10
                i = i.resize((img_w, img_h), PIL.Image.Resampling.LANCZOS)

                i_io = BytesIO()
                i.save(i_io, format='PNG')
                self.frame = InMemoryUploadedFile(i_io, None, f'Moviedome{self.series_name}{fuctions.rand_string_generator(10)}.png', 'image/jpg', None, None)

                #adding thumbnails images

                i = Image.open(self.frame)
                i.thumbnail((180, 180), PIL.Image.Resampling.LANCZOS)
                i_io= BytesIO()
                i.save(i_io, format='PNG', quality=50)
                self.thumbnail = InMemoryUploadedFile(i_io, None, f'thumbnail-Moviedome{self.series_name}{fuctions.rand_string_generator(10)}.png', 'image/png', None, None)

                self.is_edited = True
            else:
                pass
            if self.series_file:
                    origin_name = self.series_file.name
                    extention = origin_name.split('.')[-1]

                    new_name = f'Moviedome_{self.series_name}{fuctions.rand_string_generator(7)}{now().strftime('%Y%m%d%H%M%S')}.{extention}'

                    file_content = self.series_file.read()

                    self.series_file.save(new_name, ContentFile(file_content), save=False)
            else:
                pass
        else:
            pass
        return super(series, self).save(*args, **kwargs)

class related(models.Model):
    movies_relationship = models.ForeignKey('movies', on_delete=models.PROTECT, null=True, blank=True)
    series_relationship = models.ForeignKey('series', on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField('type the movie or series name here the same way its writen in models', max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class seasonal(models.Model):
    main_movie = models.ForeignKey('movies', on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField('series/ movie name',null=False, blank=False,unique=True, max_length=200)
    s_title = models.TextField('the search title for this series / movie can include the movie name and series discription or bio',null=False, blank=False)
    title = models.TextField('a simple page title',null=False, blank=False)
    meta = models.TextField('meta discrption for the series page somthing that discribes the movie',null=False, blank=False)
    discription = models.TextField('movies discription about the movie / series ', null=False, blank=False)
    views = models.BigIntegerField('number of views and visits, pls do not add this this will automatically add it self', null=True, blank=True, default=0)
    posted_by = models.CharField('add name of staff posting this vidie', null=False, blank=False, max_length=200)
    duration = models.CharField('mins of movie length the duration', null=False, blank=False, max_length=50)
    reales = models.IntegerField('movies /series reales date',null=True, blank=False, default=2020)
    pub_date = models.DateTimeField('published date')
    frame = models.ImageField('frame cover image of the series / movies',null=False, blank=False, upload_to='series_pics')
    file = models.FileField(' add file by spcifing the movie and also the one its inheriting from u can add multiple files',null=False,blank=False, unique=True, upload_to='seriesfiles')
    is_edited = models.BooleanField('do not add this its for the file and image editions', default=False)
    is_published = models.BooleanField('if movie is publised',default=False)
    thumbnail = models.ImageField('thumbnail do not add this ', upload_to='movie_thumbnails', null=True, blank=True)
    slug_name = models.SlugField('movie / series special slug do not add', null=True, blank=True, max_length=200, unique=True)
    search_str = models.TextField('movies / series search string this will auto generate', null=True, blank=True)
    spec_id = models.CharField('do not add it will auto generate, movies string',max_length=50, null=True, blank=True, unique=True)
    verifed = models.BooleanField('do not click this verification', default=False)

    def was_publised_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        if self.is_published == False:
            return f'{self.name} ------ (not_published)'
        else:
            return f'{self.name} ----- (published)'
        
    def save(self , *args, **kwargs):

        if self.verifed == False:
            self.search_str = f'{self.title}'
            self.slug_name = fuctions.rand_string_generator(10)
            self.spec_id = f'{fuctions.rand_string_generator(7)}{self.name}'
            self.verifed = True
        else:
            pass
        if self.is_edited == False:
            if self.frame:
                # editing the inage frame and moviefile
                in_img = Image.open(self.frame)
                in_img = in_img.convert("RGB")

                # resizing the frame

                i = in_img
                img_h = i.height-30 if i.height > 400 else i.height-10
                img_w = i.width-30  if i.width > 400 else i.width-10
                i = i.resize((img_w, img_h), PIL.Image.Resampling.LANCZOS)

                i_io = BytesIO()
                i.save(i_io, format='PNG')
                self.frame = InMemoryUploadedFile(i_io, None, f'Moviedome{self.name}{fuctions.rand_string_generator(10)}.png', 'image/jpg', None, None)
                #adding thumbnails images
                i = Image.open(self.frame)
                i.thumbnail((180, 180), PIL.Image.Resampling.LANCZOS)
                i_io= BytesIO()
                i.save(i_io, format='PNG', quality=50)
                self.thumbnail = InMemoryUploadedFile(i_io, None, f'thumbnail-Moviedome{self.name}{fuctions.rand_string_generator(10)}.png', 'image/png', None, None)

                self.is_edited = True
            else:
                pass
            if self.file:
                    origin_name = self.file.name
                    extention = origin_name.split('.')[-1]

                    new_name = f'Moviedome_{self.name}{fuctions.rand_string_generator(7)}{now().strftime('%Y%m%d%H%M%S')}.{extention}'

                    file_content = self.file.read()

                    self.file.save(new_name, ContentFile(file_content), save=False)
            else:
                pass
        else:
            pass

        return super(seasonal, self).save(*args, **kwargs)
    



    



        








    




