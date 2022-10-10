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
    path('celebs/<int:pk>/photos/<int:celeb_id>', views.PhotoShow.as_view(), name='photo_show'),
    path('celebs/<int:pk>/blind-items/', views.BlindItemIndex.as_view(), name='blind_items_index'), 
    # path('celebs/<int:pk>/blind-items/<int:celeb_id>/<int:id>', views.BlindItemShow.as_view(), name='blind_items_show'), 
    path('celebs/<int:pk>/articles', views.ArticleIndex.as_view(), name='article_index'),
    path('celebs/<int:pk>/videos', views.Video.as_view(), name='video_index'),
    path('celebs/<int:pk>/message-board', views.MessageBoard.as_view(), name='message_board_index')
]