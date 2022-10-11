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
        context['photos'] = Photo.objects.filter(celeb=self.kwargs['pk'])
        return context

class BlindItemIndex(TemplateView):
    model: BlindItem
    template_name= 'blind_items_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blinds'] = BlindItem.objects.filter(celebs=self.kwargs['pk'])
        return context

class VideoIndex(TemplateView):
    model: Video
    template_name = 'video_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.filter(celebs=self.kwargs['pk'])
        return context

class ArticleIndex(TemplateView):
    model: Article
    template_name = 'article_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(celebs=self.kwargs['pk'])
        return context

class MessageBoardIndex(TemplateView):
    model: MessageBoard
    template_name = 'message_board_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message-boards'] = MessageBoard.objects.filter(celebs=self.kwargs['pk'])
        return context

class PhotoShow(DetailView):
    model = Photo
    template_name="photo_show.html"


    def get_context_data(self, **kwargs):
        context = super(PhotoShow, self).get_context_data(**kwargs)
        context ['photo']= Photo.objects.filter(photo_id=self.kwargs['photo_id'])
        return context
        
    # def get_context_data(self, **kwargs):
    #     context = super(PhotoShow, self).get_context_data(**kwargs)
    #     photo_id = Photo.objects.get(id=self.kwargs.get('photo_pk'))
    #     context['photo'] = photo_id
    #     return context