from email.message import Message
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


# Celeb Model

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

class CelebShow(DetailView):
    model = Celeb
    template_name="celeb_show.html"

class CreateCelebs(CreateView):
    model = Celeb
    fields = ['name', 'image', 'bio']
    template_name = 'create_celeb.html'
    success_url = '/celebs/'

class CelebUpdate(UpdateView):
    model = Celeb
    fields = ['name', 'image', 'bio']
    template_name = 'update_celeb.html'
    success_url = "/celebs/"


# Photo Model

class PhotoIndex(TemplateView):
    model: Photo
    template_name = 'photo_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Photo.objects.filter(celeb=self.kwargs['pk'])
        return context

class PhotoShow(DetailView):
    model = Photo
    template_name="photo_show.html"

    def get_context_data(self, **kwargs):
        context = super(PhotoShow, self).get_context_data(**kwargs)
        return context


# Video Model 

class VideoIndex(TemplateView):
    model: Video
    template_name = 'video_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.filter(celeb=self.kwargs['pk'])
        return context

class VideoShow(DetailView):
    model = Video
    template_name="video_show.html"

    def get_context_data(self, **kwargs):
        context = super(VideoShow, self).get_context_data(**kwargs)
        return context


# Blind Items Model

class BlindItemsIndex(TemplateView):
    model: BlindItem
    template_name = 'blind_item_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blinds'] = BlindItem.objects.filter(celeb=self.kwargs['pk'])
        return context

class BlindItemShow(DetailView):
    model = BlindItem
    template_name="blind_item_show.html"

    def get_context_data(self, **kwargs):
        context = super(BlindItemShow, self).get_context_data(**kwargs)
        return context

# Articles Model

class ArticlesIndex(TemplateView):
    model: Article
    template_name = 'article_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(celeb=self.kwargs['pk'])
        return context

class ArticleShow(DetailView):
    model = Article
    template_name="article_show.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleShow, self).get_context_data(**kwargs)
        return context


# Message Board Model 

class MessageBoardsIndex(TemplateView):
    model: MessageBoard
    template_name = 'message_board_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messageboards'] = MessageBoard.objects.filter(celeb=self.kwargs['pk'])
        return context

class MessageBoardShow(DetailView):
    model = MessageBoard
    template_name="message_board_show.html"

    def get_context_data(self, **kwargs):
        context = super(MessageBoardShow, self).get_context_data(**kwargs)
        return context



