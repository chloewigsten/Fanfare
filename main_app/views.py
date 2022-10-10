from re import L
from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from .models import Celeb, Photo, BlindItem, Article, Video, MessageBoard

# Home View
class Home(TemplateView):
    template_name = ('home.html')

# About View 
class About(TemplateView):
    template_name = ('about.html')


# Celeb Index View 
class CelebList(TemplateView):
    template_name = 'celeb_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None: 
            context['celebs'] = Celeb.objects.filter(name__icontains=name)
            context['header'] = f"Showing all results for {name}"
        else:
            context['celebs'] = Celeb.objects.all()
        return context

class CreateCelebs(CreateView):
    model = Celeb
    fields = ['name', 'image', 'bio']
    template_name = 'create_celeb.html'
    success_url = '/celebs/'

class CelebShow(DetailView):
    model = Celeb
    template_name="celeb_show.html"

class CelebUpdate(UpdateView):
    model = Celeb
    fields = ['name', 'image', 'bio']
    template_name = 'update_celeb.html'
    success_url = "/celebs/"

class PhotoIndex(TemplateView):
    model: Photo
    template_name = 'photo_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        celeb_id = self.request.GET.get('photos')
        context['photos'] = Photo.objects.filter(celeb__exact=celeb_id)
        return context