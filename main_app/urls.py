from django.urls import path, include
from django.conf.urls import handler404, handler500, handler403, handler400
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('celebs/', views.CelebList.as_view(), name='celebs'),
    path('celebs/new', views.CreateCelebs.as_view(), name='create_celeb'),
    path('celebs/<int:pk>/', views.CelebShow.as_view(), name='celeb_show'), 
    path('celebs/<int:pk>/update', views.CelebUpdate.as_view(), name='update_celeb'),
    path('celebs/<int:pk>/photos/', views.PhotoIndex.as_view(), name='photo_index'),
    path('photos/<int:pk>', views.PhotoShow.as_view(), name='photo_show'),  
    path('celebs/<int:pk>', views.VideoIndex.as_view(), name='video_index'),
    path('videos/<int:pk>', views.VideoShow.as_view(), name='video_show'),
    path('celebs/<int:pk>/blind-items', views.BlindItemsIndex.as_view(), name='blind_item_index'),
    path('blind-items/<int:pk>', views.BlindItemShow.as_view(), name='blind_item_show'),
    path('celebs/<int:pk>/articles', views.ArticlesIndex.as_view(), name='article_index'), 
    path('articles/<int:pk>', views.ArticleShow.as_view(), name='article_show'),
    path('celebs/<int:pk>/message-boards', views.MessageBoardsIndex.as_view(), name='message_board_index'), 
    path('message-boards/<int:pk>', views.MessageBoardShow.as_view(), name='message_board_show'), 
]

# handler404 = "helpers.views.handle_not_found"

handler404 = views.error_404
