from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('celebs/', views.CelebList.as_view(), name='celebs'),
    path('celebs/new', views.CreateCelebs.as_view(), name='create_celeb'),
    path('celebs/<int:pk>/', views.CelebShow.as_view(), name='celeb_show'), 
    path('celebs/<int:pk>/update', views.CelebUpdate.as_view(), name='update_celeb'),
    path('celebs/<int:pk>/photos/', views.PhotoIndex.as_view(), name='photo_index'), 
]